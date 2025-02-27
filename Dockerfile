# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Ensure .env.template is created only if it doesn't exist
RUN test -f .env.template || echo '# API Keys\n' \
    'OPENAI_API_KEY="your_openai_api_key_here"\n' \
    'XAI_API_KEY="your_xai_api_key_here"\n\n' \
    '# LLM Configuration\n' \
    'LLM_PROVIDER=openai\n' \
    'LLM_MODEL=gpt-4\n\n' \
    '# Application Configuration\n' \
    'DEBUG=True\n' \
    'PORT=8000' > .env.template

# Clean install with exact versions
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .