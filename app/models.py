import requests
import threading
import time
import os
import logging

logger = logging.getLogger(__name__)


class Website:
    def __init__(self, url):
        self.url = url
        self.status = "Unknown"
        self.previous_status = "Unknown"
        self.thread = None
        self.pushover_user_key = os.getenv("PUSHOVER_USER_KEY")
        self.pushover_api_token = os.getenv("PUSHOVER_API_TOKEN")
        self.pushover_devices = os.getenv("PUSHOVER_DEVICES")
        self.last_notification_status = "Unknown"

    def start_monitoring(self):
        self.thread = threading.Thread(target=self._monitor)
        self.thread.daemon = True
        self.thread.start()

    def _monitor(self):
        while True:
            try:
                response = requests.get(self.url, timeout=5)
                new_status = (
                    "Up"
                    if response.status_code == 200
                    else f"Down (Status code: {response.status_code})"
                )
            except requests.RequestException as e:
                new_status = f"Down ({type(e).__name__})"

            if new_status != self.status:
                if (self.status == "Up" and new_status.startswith("Down")) or (
                    self.status.startswith("Down") and new_status == "Up"
                ):
                    if new_status != self.last_notification_status:
                        self._send_notification(
                            f"Website {self.url} changed from {self.status} to {new_status}"
                        )
                        self.last_notification_status = new_status
                self.previous_status = self.status
                self.status = new_status

            time.sleep(60)  # Check every minute

    def _send_notification(self, message):
        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": self.pushover_api_token,
            "user": self.pushover_user_key,
            "message": message,
        }
        if self.pushover_devices:
            data["device"] = self.pushover_devices

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            logger.info(f"Notification sent: {message}")
        except requests.RequestException as e:
            logger.error(f"Failed to send notification: {e}")
