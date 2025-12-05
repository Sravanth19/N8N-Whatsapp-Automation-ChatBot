#!/bin/bash

# Test script for WhatsApp webhook
# Usage: ./test-webhook.sh <webhook_url>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <webhook_url>"
    echo "Example: $0 http://localhost:5678/webhook/whatsapp"
    exit 1
fi

WEBHOOK_URL=$1

# Sample WhatsApp webhook payload
PAYLOAD='{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "123456789",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "1234567890",
              "phone_number_id": "1234567890"
            },
            "contacts": [
              {
                "profile": {
                  "name": "Test User"
                },
                "wa_id": "1234567890"
              }
            ],
            "messages": [
              {
                "id": "wamid.test",
                "from": "1234567890",
                "timestamp": "1234567890",
                "text": {
                  "body": "Hello, this is a test message"
                },
                "type": "text"
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}'

echo "Testing webhook at: $WEBHOOK_URL"
echo "Payload:"
echo "$PAYLOAD"
echo ""

curl -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD"

echo ""
echo "Test completed."
