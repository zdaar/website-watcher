# Website Watcher

A simple Docker-based app to monitor websites and send Pushover notifications when their status changes.

## Overview

Website Watcher helps you keep an eye on multiple websites, showing their status in a straightforward web interface and notifying you via Pushover when a site goes down or comes back up.

## Features

- Monitor multiple websites simultaneously
- Web interface for status updates
- Pushover notifications for status changes
- Easy setup with Docker
- Pre-load websites to monitor

## Requirements

- Docker and Docker Compose
- Pushover account (for notifications)

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/zdaar/website-watcher.git
   cd website-watcher
   ```

2. Create a `.env` file in the project root based on `.env.example`:

   ```
   PUSHOVER_USER_KEY=your_key_here
   PUSHOVER_API_TOKEN=your_token_here
   PUSHOVER_DEVICES=your_device_name
   WEBSITES_TO_MONITOR=https://example.com,https://example.org
   ```

3. Build and start the Docker container:

   ```
   docker-compose up --build
   ```

4. Access the app at `http://localhost:9988`

## Usage

1. Open `http://localhost:9988` in your browser
2. Enter a URL you want to monitor
3. Click "Start Monitoring"
4. Repeat for additional sites

The web interface updates every 5 seconds, and the app checks each site every minute. You'll receive a Pushover notification when a site's status changes from Up to Down or from Down to Up.

## Customization

- Modify check frequency: Edit the sleep timer in `app/models.py`
- Adjust the UI: Modify `templates/index.html`
- Pre-load websites: Add URLs to the `WEBSITES_TO_MONITOR` variable in your `.env` file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
