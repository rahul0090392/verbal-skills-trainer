# Verbal Communication Skills Trainer

## 🚀 Project Overview
This is a **FastAPI-based application** designed to help learners improve their **verbal communication skills** using AI-powered chat and voice interactions. The project supports **text-based conversations, voice input analysis, and structured training modules**.

## 📦 Project Structure
```
app/
│── api/
│   ├── llm_client.py   # Handles interaction with OpenAI/xAI
│── modules/
│   ├── chat.py         # Chat processing logic
│   ├── voice.py        # Voice processing logic (speech-to-text, text-to-speech)
│── templates/
│   ├── chat.html       # UI for chat module
│── static/
│   ├── css/            # CSS stylesheets
│   ├── js/             # JavaScript files
│── main.py             # FastAPI application entry point
│── Dockerfile          # Docker configuration
│── docker-compose.yml  # Docker Compose setup
│── requirements.txt    # Python dependencies
│── .env.template       # Environment variable template
```

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/rahul0090392/verbal-skills-trainer
cd verbal-skills-trainer
```

### 2️⃣ Setup Environment Variables
Create a **`.env`** file from the provided template:
```sh
cp .env.template .env
```
Edit `.env` and add your API keys:
```ini
OPENAI_API_KEY="your_openai_api_key_here"
XAI_API_KEY="your_xai_api_key_here"
LLM_PROVIDER=openai  # or xai
LLM_MODEL=gpt-4
DEBUG=True
PORT=8000
```

### 3️⃣ Build & Run with Docker
Run the following commands:
```sh
docker-compose build
docker-compose up -d
```
This will:
- Build the FastAPI application inside a **Docker container**
- Start the application on **port 8000**
- Automatically reload the app on code changes

### 4️⃣ Access the Application
- Open the chat UI: [http://localhost:8000/](http://localhost:8000/)
- Open the API documentation (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative API docs (ReDoc): [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📜 API Documentation (Swagger)
FastAPI provides an **interactive Swagger UI** for testing endpoints.

### **📝 Endpoints**
#### 1️⃣ **Chat API**
**`POST /api/chat`**  
Sends a message to the AI and receives a response.
```json
{
    "message": "How can I improve my speaking skills?",
    "mode": "Coach"
}
```
_Response:_
```json
{
    "response": "To improve speaking skills, practice clarity and confidence."
}
```

#### 2️⃣ **Health Check**
**`GET /health`**  
Returns the status of the application.
```json
{
    "status": "OK"
}
```

---

## 🛑 Stopping the Application
To stop the running containers, use:
```sh
docker-compose down
```


## 👨‍💻 Contributors
- Your Name - [GitHub](https://github.com/rahul0090392)

---

## 📝 License
MIT License

