# weather-whatsapp-alert

This project sends daily weather updates via WhatsApp using the Twilio API and OpenWeatherMap API.

## Table of Contents
- Overview
- Installation
- Usage
- Files
- Automation
- License

## Overview

The Weather WhatsApp Alert project fetches weather data for a specified location and sends a daily update via WhatsApp. This project demonstrates the integration of external APIs and the use of environment variables for secure configuration.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JakeHulme1/weather-whatsapp-alert.git
   cd weather-whatsapp-alert
2. **Create a virtual environment byrunning the following in the terminal in project folder:**
  python -m venv .venv
  source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
3. **Install the required packages by running the following:**
  pip install -r requirements.txt
4. **Set up environment variables.**
  - Add Twilio and OpenWeatherMap credintials into the .env folder (you will needto create an account on Twilio and OpenWeatherMap for the API keys)
  - Add the Twilio Sandbox nmber and the user's whatsapp number into the .env file

## Usage

1. Run the script:
  python main.py

2. What it does:
  - Fetches the current weather data for a specified location (location specified in main.py) from the OpenWeatherMap API.
  - Sends a WhatsApp message with the weather update to the specified number using the Twilio API.

## Files

- weather.py: Contains the main logic for fetching weather data and sending WhatsApp messages.
- .env: Stores environment variables (not included in the repository for security reasons).
- requirements.txt: Lists all the dependencies required for the project.
- .gitignore: Specifies files and directories to be ignored by Git, including .env and .venv.

## Automation

To automate the script to run daily at a certain time, you can use a task scheduler like Task Scheduler on Windows.

Using Task Scheduler (Windows):
1. Open Task Scheduler and create a new task.
2. Set the trigger to daily at your desired time.
3. Set the action to start a program and point it to the Python executable in your virtual environment and the weather.py script.
