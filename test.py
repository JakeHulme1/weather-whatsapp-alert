from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:+447788230000'  # Your WhatsApp number

def send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    return message.sid

# Example usage
rain_chance = "50% chance of rain today"
message = f"Today's weather update: {rain_chance}"
send_whatsapp_message(account_sid, auth_token, from_whatsapp_number, to_whatsapp_number, message)