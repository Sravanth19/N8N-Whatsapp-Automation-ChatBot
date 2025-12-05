#!/usr/bin/env python3
"""
Example script to send a WhatsApp message using the Cloud API
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')
PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
RECIPIENT_PHONE = os.getenv('RECIPIENT_PHONE', '1234567890')  # Replace with actual recipient

def send_message(message_text, recipient_phone):
    """
    Send a text message via WhatsApp Cloud API

    Args:
        message_text (str): The message to send
        recipient_phone (str): Recipient's phone number in international format

    Returns:
        dict: API response
    """

    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_phone,
        "type": "text",
        "text": {
            "body": message_text
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    message = "Hello from WhatsApp n8n Chatbot!"
    result = send_message(message, RECIPIENT_PHONE)

    if result:
        print("Message sent successfully!")
        print(f"Message ID: {result.get('messages', [{}])[0].get('id')}")
    else:
        print("Failed to send message.")
