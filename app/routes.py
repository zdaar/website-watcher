from flask import render_template, request, jsonify, url_for, redirect
from app import app
from app.models import Website
import os

websites = {}


@app.before_first_request
def initialize_websites():
    initial_websites = os.getenv("WEBSITES_TO_MONITOR", "").split(",")
    for url in initial_websites:
        url = url.strip()
        if url and url not in websites:
            website = Website(url)
            website.start_monitoring()
            websites[url] = website


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        if url not in websites:
            website = Website(url)
            website.start_monitoring()
            websites[url] = website
    return render_template("index.html", websites=websites)


@app.route("/status")
def status():
    return jsonify({url: website.status for url, website in websites.items()})


@app.route("/remove/<path:url>", methods=["POST"])
def remove_website(url):
    if url in websites:
        del websites[url]
    return redirect(url_for("index"))


@app.route("/test_notification")
def test_notification():
    website = Website("https://example.com")
    website._send_notification("Test notification from Website Monitor")
    return "Test notification sent"
