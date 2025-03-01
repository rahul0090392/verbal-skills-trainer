# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# ✅ Install additional system dependencies for STT & TTS
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    ffmpeg \
    libsndfile1 \
    pocketsphinx \
    pocketsphinx-en-us \
    espeak \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*


# ✅ Ensure `.env.template` exists
RUN test -f .env.template || echo '# API Keys\n' \
    'OPENAI_API_KEY="your_openai_api_key_here"\n' \
    'XAI_API_KEY="your_xai_api_key_here"\n\n' \
    '# LLM Configuration\n' \
    'LLM_PROVIDER=openai\n' \
    'LLM_MODEL=gpt-4\n\n' \
    '# Application Configuration\n' \
    'DEBUG=True\n' \
    'PORT=8000' > .env.template

RUN pip install --upgrade pip && \
    pip install --no-cache-dir pocketsphinx SpeechRecognition pydub soundfile -r requirements.txt

# Copy the application code to the container
COPY . .


