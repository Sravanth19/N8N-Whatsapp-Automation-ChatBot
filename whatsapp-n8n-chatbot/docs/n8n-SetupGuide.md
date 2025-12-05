# n8n Setup Guide

This guide will help you install and configure n8n for the WhatsApp chatbot project.

## Prerequisites

- Node.js (version 16 or higher)
- npm or yarn
- Basic command line knowledge
- Docker and Docker Compose (optional, for containerized setup)

## Installation Options

### Option 1: npm Installation (Recommended for Development)

1. Install n8n globally:
   ```bash
   npm install -g n8n
   ```

2. Start n8n:
   ```bash
   n8n
   ```

3. Access n8n at http://localhost:5678

### Option 2: Docker Installation (Recommended for Production)

1. Pull the n8n Docker image:
   ```bash
   docker pull n8n/n8n
   ```

2. Run n8n in a Docker container:
   ```bash
   docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -v ~/.n8n:/home/node/.n8n \
     n8n/n8n
   ```

3. For production with Docker Compose, create a `docker-compose.yml`:
   ```yaml
   version: '3.8'
   services:
     n8n:
       image: n8n/n8n:latest
       ports:
         - "5678:5678"
       environment:
         - N8N_BASIC_AUTH_ACTIVE=true
         - N8N_BASIC_AUTH_USER=user
         - N8N_BASIC_AUTH_PASSWORD=password
       volumes:
         - ~/.n8n:/home/node/.n8n
   ```

   Then run:
   ```bash
   docker-compose up -d
   ```

## Initial Configuration

1. Open http://localhost:5678 in your browser
2. Create an account or log in
3. Set up your workspace

## Importing Workflows

1. In n8n, go to "Workflows" in the left sidebar
2. Click "Import from File"
3. Import each JSON file from the `n8n-workflows/` directory:
   - `whatsapp-webhook.json`
   - `openai-integration.json`
   - `send-message.json`

## Configuring Credentials

1. Go to "Credentials" in the left sidebar
2. Add the following credentials:

   **WhatsApp API:**
   - Type: HTTP Request
   - Name: WhatsApp API
   - Base URL: https://graph.facebook.com/v17.0
   - Headers:
     - Authorization: Bearer {{ $env.WHATSAPP_ACCESS_TOKEN }}

   **OpenAI API:**
   - Type: OpenAI
   - Name: OpenAI Chat
   - API Key: {{ $env.OPENAI_API_KEY }}

## Setting Up Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp environment/.env.example .env
   ```

2. Fill in your actual values in the `.env` file

3. For Docker setups, pass environment variables:
   ```bash
   docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     --env-file .env \
     -v ~/.n8n:/home/node/.n8n \
     n8n/n8n
   ```

## Connecting Workflows

To create a complete chatbot workflow:

1. Create a new workflow or modify existing ones
2. Connect the nodes in this order:
   - Webhook (receives WhatsApp messages)
   - OpenAI Integration (generates responses)
   - Send Message (sends reply back to WhatsApp)

3. Set up data flow between nodes using expressions like:
   - `{{ $json.body.entry[0].changes[0].value.messages[0].text.body }}` for message text
   - `{{ $json.choices[0].message.content }}` for OpenAI response

## Testing the Setup

1. Start n8n if not already running
2. Activate all workflows (green play button)
3. Test the webhook: `./scripts/test-webhook.sh http://localhost:5678/webhook/whatsapp`
4. Check n8n execution logs for successful processing

## Production Deployment

For production deployment:

1. Use Docker Compose with proper environment variables
2. Set up a reverse proxy (nginx) for SSL termination
3. Configure persistent storage for workflows and data
4. Set up monitoring and logging
5. Enable authentication and access controls

## Troubleshooting

- **Port already in use**: Change port with `n8n --port 5679`
- **Permission issues**: Ensure proper file permissions for `.n8n` directory
- **Workflow not saving**: Check disk space and file permissions
- **Import fails**: Verify JSON syntax and n8n version compatibility

For more detailed information, refer to the [official n8n documentation](https://docs.n8n.io/).
