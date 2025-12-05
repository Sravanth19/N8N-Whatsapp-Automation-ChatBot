# 🤖 WhatsApp AI Chatbot (n8n + OpenAI)

![n8n](https://img.shields.io/badge/n8n-Workflow-ff6b6b?style=for-the-badge&logo=n8n&logoColor=white)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Cloud_API-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT_4-412991?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-Scripting-FFD43B?style=for-the-badge&logo=python&logoColor=blue)


> **A scalable, event-driven chatbot pipeline.** This project integrates the WhatsApp Cloud API with OpenAI via n8n to create an intelligent, automated conversational agent capable of handling real-world queries.

---

## 📂 Project Structure

The repository is organized to separate workflows, documentation, and operational scripts for easy maintenance and scalability.

```text
whatsapp-n8n-chatbot/
│
├── README.md                     # Project Overview & Quick Start
├── architecture/                 # Visual diagrams of the system
│   ├── system-diagram.png        # High-level architecture view
│   ├── workflow-diagram.png      # Detailed n8n flow visualization
│
├── n8n-workflows/                # Importable JSON workflow files
│   ├── whatsapp-webhook.json     # Handles incoming messages
│   ├── openai-integration.json   # Processes logic via AI
│   ├── send-message.json         # Dispatches replies to WhatsApp
│
├── scripts/                      # Utility scripts for testing
│   ├── test-webhook.sh           # Curl command to simulate incoming events
│   ├── send-message-example.py   # Python script to test sending manually
│
├── environment/                  # Configuration templates  
│   ├── .env.example              # Template for environment variables
│   ├── config.md                 # Configuration documentation
│
├── docs/                         # Detailed setup guides
│   ├── WhatsAppCloudAPI-Setup.md # Step-by-step Meta Developer setup
│   ├── n8n-SetupGuide.md         # Importing and activating workflows
│   ├── Troubleshooting.md        # Common errors and fixes
│
└── LICENSE                       # MIT License  
```
---

## 📖 Overview

Building a chatbot often requires complex backend servers and database management. This project simplifies that process by using **n8n** as a visual orchestrator. 

It acts as a bridge between:
1.  **WhatsApp Users:** Who send messages via their mobile devices.
2.  **OpenAI (GPT):** Which processes the text and generates human-like responses.
3.  **WhatsApp Cloud API:** Which delivers the AI's response back to the user.

This architecture is serverless (when using n8n Cloud) or self-hostable, making it highly cost-effective and customizable.

## ✨ Key Features

* **⚡ Real-time Webhooks:** Instant message reception using n8n's webhook nodes.
* **🧠 Contextual AI:** Uses OpenAI's GPT models to understand intent and context, not just keywords.
* **🛠 Modular Design:** The logic is split into three distinct workflows (Webhook, AI, Sender) to allow for easier debugging and independent updates.
* **🧪 Developer Tools:** Includes Python and Shell scripts to test your API connections without needing to spam your actual WhatsApp account.

---

## ⚙️ Architecture


 🔄 n8n Workflow Diagram

![n8n Workflow](https://github.com/Sravanth19/N8N-Whatsapp-Automation-ChatBot/raw/261b91c521ac8217a651eeb847c226869ffedd5e/n8n_Flow_Whatapp_Message%20_Automation.png)

1.  **Ingest:** User sends a message -> Meta Cloud API -> n8n Webhook.
2.  **Process:** n8n formats the text -> Sends to OpenAI API.
3.  **Respond:** OpenAI returns text -> n8n formats payload -> Sends to WhatsApp API.

---

## 🚀 Getting Started

### Prerequisites

* **n8n Instance:** You need n8n installed (locally via npm/Docker) or an n8n Cloud account.
* **Meta Developer Account:** A configured WhatsApp Business App with a phone number ID.
* **OpenAI API Key:** To access GPT-3.5 or GPT-4.
* **Python 3.x:** (Optional) Required only if you want to run the testing scripts.

### 📥 Installation Guide

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Sravanth19/whatsapp-n8n-chatbot.git](https://github.com/Sravanth19/whatsapp-n8n-chatbot.git)
    cd whatsapp-n8n-chatbot
    ```

2.  **Configure Environment**
    * Navigate to the `environment/` folder.
    * Copy `.env.example` to a new file named `.env`.
    * Update the values:
        ```ini
        WHATSAPP_TOKEN=your_meta_access_token
        PHONE_NUMBER_ID=your_phone_number_id
        OPENAI_API_KEY=sk-...
        ```

3.  **Import Workflows**
    * Open your n8n dashboard.
    * Navigate to **Workflows** > **Import from File**.
    * Select all three JSON files from the `n8n-workflows/` directory.

4.  **Connect Webhooks**
    * Copy the "Production URL" from your n8n Webhook node.
    * Paste it into your Meta Developer App dashboard under **WhatsApp** > **Configuration** > **Callback URL**.

---

## 🧪 Testing & Verification

We have provided scripts to help you verify your setup before going live.

**1. Test the Webhook (Simulate a Message):**
Use the shell script to send a fake WhatsApp payload to your n8n instance.
```bash
./scripts/test-webhook.sh

```
---


# 🔧 Troubleshooting

Common issues and how to fix them.

## 1. Webhook Verification Failed
**Error:** Meta says "The callback URL or verify token couldn't be validated."
**Fix:**
* Ensure your n8n workflow is **Active**.
* Ensure the `Verify Token` you typed in the Meta Dashboard matches exactly what is in your n8n Webhook node settings.
* Check if your n8n instance is publicly accessible (if hosting locally, use a tunnel like `ngrok`).

## 2. Messages Not Delivering
**Error:** n8n says "Success", but no message appears on WhatsApp.
**Fix:**
* **Token Expiry:** If you are using a Temporary Access Token, it expires every 24 hours. Refresh it in the Meta Dashboard.
* **Sandbox Mode:** If your app is in Development mode, you can only send messages to numbers that have been verified in the Meta Dashboard.
* **Conversation Window:** You can only reply to a user within 24 hours of their last message.

## 3. OpenAI Errors
**Error:** `429 Too Many Requests` or `Quota Exceeded`.
**Fix:**
* Check your OpenAI billing settings. You must have credits/balance available.
* If using GPT-4, ensure your account has access to it. If not, switch the model in n8n to `gpt-3.5-turbo`.

## 4. Infinite Loop
**Error:** The bot replies to itself endlessly.
**Fix:**
* Add a filter node in n8n immediately after the Webhook to check if the incoming message is `from_me=true`. If so, stop the workflow.
---
<div align="center">

### 👤 Created by Sravanth Gutipalli

[![LinkedIn](https://img.shields.io/badge/Connect-Sravanth%20Gutipalli-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sravanth-gutipalli-99215a266)

</div>


