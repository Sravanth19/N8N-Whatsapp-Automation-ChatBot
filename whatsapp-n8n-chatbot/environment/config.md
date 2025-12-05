# Configuration Guide

This guide explains how to configure the WhatsApp n8n Chatbot project.

## Environment Variables

Copy the `.env.example` file to `.env` and fill in your values:

```bash
cp .env.example .env
```

### Required Variables

- **WHATSAPP_ACCESS_TOKEN**: Your WhatsApp Cloud API access token
- **WHATSAPP_PHONE_NUMBER_ID**: Your WhatsApp phone number ID
- **WHATSAPP_VERIFY_TOKEN**: Token used to verify webhook requests
- **OPENAI_API_KEY**: Your OpenAI API key for chat responses

### Optional Variables

- **N8N_WEBHOOK_URL**: URL where n8n is running (default: http://localhost:5678/webhook/whatsapp)
- **DATABASE_URL**: Database connection string if using persistent storage
- **LOG_LEVEL**: Logging level (DEBUG, INFO, WARNING, ERROR)

## Getting API Tokens

### WhatsApp Cloud API

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create a new app or use existing one
3. Add WhatsApp product
4. Generate permanent access token
5. Get your phone number ID from the API setup

### OpenAI

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create an account or log in
3. Navigate to API Keys section
4. Create a new secret key

## Security Notes

- Never commit your `.env` file to version control
- Rotate API keys regularly
- Use environment-specific tokens (dev/staging/prod)
- Limit token permissions to minimum required

## Testing Configuration

After setting up your environment variables:

1. Start n8n: `npx n8n`
2. Import workflows from `n8n-workflows/` directory
3. Test webhook: `./scripts/test-webhook.sh http://localhost:5678/webhook/whatsapp`
4. Send test message: `python scripts/send-message-example.py`

## Troubleshooting

- **Invalid token errors**: Check your access tokens are correct and not expired
- **Webhook not working**: Verify n8n is running and webhook URL is correct
- **OpenAI errors**: Ensure API key has sufficient credits and correct permissions
