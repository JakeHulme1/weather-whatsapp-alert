from twilio.rest import Client
import os
from dotenv import load_dotenv
from weather import get_weather

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_whatsapp_number = os.environ['FROM_WHATSAPP_NUMBER']  # Twilio sandbox number
to_whatsapp_number = os.environ['TO_WHATSAPP_NUMBER']  # User's WhatsApp number
openweather_api_key = os.getenv('OPENWEATHER_API_KEY')

# Check if all necessary environment variables are set
if not account_sid or not auth_token or not openweather_api_key:
    raise ValueError("Missing environment variables. Please check your .env file.")

# Function to send WhatsApp message using Twilio API
def send_whatsapp_message(sid, token, from_number, to_number, msg):
    client = Client(sid, token)
    print(f"Sending message from {from_number} to {to_number}")
    msg = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    print(f"Message SID: {msg.sid}")  # Print the message SID for tracking
    return msg.sid

# Get the weather data and send the message
rain_chance = get_weather(openweather_api_key, 'London')
message = f"Today's chance of rain: {rain_chance}"
send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, message)