# YouTube Transcription Pipeline (n8n + OpenAI Whisper)

n8n OpenAI Automation

Turn video into text, instantly. A fully automated workflow that extracts audio from YouTube videos, processes it through OpenAI's state-of-the-art Whisper model, and delivers highly accurate transcriptions.

📖 Overview
In the age of video content, accessing the information inside a video file can be difficult. This project bridges the gap between video media and text analysis.

By leveraging n8n for orchestration and OpenAI Whisper for intelligence, this tool automatically converts YouTube URLs into distinct, searchable, and editable text formats. It is perfect for content creators, researchers, and developers looking to archive or analyze video content programmatically.

✨ Key Features
🔗 Seamless Extraction: Accepts YouTube URLs and automatically handles audio extraction.
🧠 High-Fidelity Transcription: Uses the whisper-1 model to achieve near-human accuracy in speech-to-text conversion.
⚡ Event-Driven: Can be triggered manually, via webhook, or through a form interface.
📂 Automated Formatting: Cleans up the raw JSON response into readable text.
🌍 Multi-Language Capable: Automatically detects and transcribes various input languages.
🛠️ Tech Stack
Workflow Automation: n8n
AI Model: OpenAI API (Whisper)
Audio Processing: FFmpeg / yt-dlp
Data Handling: JSON
⚙️ How It Works
YouTube Transcription Workflow

Input: The workflow receives a YouTube video URL.
Download & Extract: The system downloads the video and extracts the audio track using command-line tools.
Process: The audio is optimized to meet API file size limits.
Transcribe: The audio file is sent to the OpenAI Whisper API.
Output: The resulting transcript is returned to the user or saved to a database/document.
🚀 Getting Started
Prerequisites
An instance of n8n (Self-hosted or Cloud).
OpenAI API Key (with access to the Whisper model).
Python/FFmpeg installed on the environment running n8n (for the audio extraction step).
Installation
Clone/Download the workflow JSON file from this repository.
Open your n8n dashboard.
Click "Import from File" and select the JSON file.
Configure Credentials:
Open the OpenAI node and paste your API Key.
Activate the workflow.
🔮 Future Improvements
 Summarization: specific integration with GPT-4 to summarize the transcript immediately after generation.
 Speaker Identification: Implementing diarization to distinguish between different voices.
 Notion/Docs Integration: Automatically save the finished transcript to a workspace.
📝 License
This project is licensed under the MIT License.
