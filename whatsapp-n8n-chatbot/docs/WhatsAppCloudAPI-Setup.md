# WhatsApp Cloud API Setup Guide

This guide will help you set up the WhatsApp Cloud API for your chatbot project.

## Prerequisites

- A Facebook Developer account
- A WhatsApp Business Account
- A phone number to use for WhatsApp Business

## Step 1: Create a Facebook App

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Click "Create App"
3. Select "Business" as the app type
4. Fill in your app details and create the app

## Step 2: Add WhatsApp to Your App

1. In your app dashboard, click "Add Product"
2. Find "WhatsApp" and click "Set Up"
3. Follow the setup wizard

## Step 3: Configure WhatsApp Business API

1. In the WhatsApp section, go to "API Setup"
2. Add your phone number
3. Verify the phone number via SMS
4. Note down your Phone Number ID and Access Token

## Step 4: Set Up Webhook

1. In the WhatsApp settings, go to "Webhook"
2. Add your webhook URL (your n8n webhook URL)
3. Set a verify token (this should match your WHATSAPP_VERIFY_TOKEN env var)
4. Subscribe to the "messages" field

## Step 5: Test the Setup

1. Send a message to your WhatsApp Business number
2. Check your n8n logs to see if the webhook is receiving messages
3. Use the test script to verify webhook functionality

## Important Notes

- The permanent access token expires after 24 hours initially
- You need to request a permanent token for production use
- Webhooks must be HTTPS in production
- Rate limits apply to API calls

## Troubleshooting

- **Webhook not receiving messages**: Check webhook URL and verify token
- **Invalid token**: Ensure your access token is correct and not expired
- **Phone number not verified**: Complete the verification process
- **API errors**: Check the WhatsApp Business API documentation for error codes

For more detailed information, refer to the [WhatsApp Business API Documentation](https://developers.facebook.com/docs/whatsapp/).
