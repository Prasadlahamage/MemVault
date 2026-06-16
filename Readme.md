# MemVault

MemVault is a personal logging and knowledge management application built with Flask and SQLite.

It allows users to capture daily entries, experiences, thoughts, achievements, and learnings in a simple and organized manner. The long term vision is to evolve MemVault into a private, AI powered personal knowledge vault capable of understanding, organizing, and retrieving meaningful insights from daily logs.

---

## Features

### Current Features

* Create entries
* View saved entries
* Edit existing entries
* Delete entries
* SQLite backed storage
* Local timestamp support
* Recent entries displayed on the homepage
* AI powered fact extraction using Gemini
* Structured fact storage for future insights and analytics

### AI Fact Extraction

When a new entry is saved, MemVault automatically analyzes the content and extracts structured information.

Example Entry:

```text
Today I walked 8000 steps.
My weight is 73kg.
Had chicken biryani.
Worked on MemVault.
```

Example Extracted Facts:

```json
{
  "steps": 8000,
  "weight": "73kg",
  "food": "chicken biryani"
}
```

These facts are stored separately from the original entry, enabling future analytics, intelligent retrieval, and insight generation.

---

## Tech Stack

### Backend

* Flask
* SQLite

### AI

* Google Gemini API

### Future Integrations

* ChromaDB
* Ollama
* Qwen
* LangGraph
* Docker
* Terraform

---

## Project Structure

```text
MemVault/
│
├── app.py
├── database.py
├── memvault.db
│
├── ai/
│   ├── __init__.py
│   ├── llm.py
│   └── extractor.py
│
├── templates/
│   ├── index.html
│   ├── memories.html
│   ├── edit.html
│   └── facts.html
│
├── static/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/MemVault.git
cd MemVault
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Database

MemVault uses SQLite for local storage.

The database is automatically created on startup.

### memories

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| content    | TEXT    |
| created_at | TEXT    |

### facts

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| memory_id  | INTEGER |
| fact_type  | TEXT    |
| fact_value | TEXT    |

The `facts` table stores AI extracted information separately from the original entries.

---

## Development Roadmap

### Version 0.1

* [x] Create entries
* [x] View entries
* [x] Edit entries
* [x] Delete entries
* [x] Local timestamp support

### Version 0.2

* [x] Gemini integration
* [x] AI fact extraction
* [x] Structured facts database
* [ ] Ask MemVault interface
* [ ] Entry search

### Version 0.3

* [ ] Semantic search
* [ ] ChromaDB integration
* [ ] Weekly insights
* [ ] Monthly reflections
* [ ] Personal analytics dashboard

### Version 0.4

* [ ] User authentication
* [ ] Multi-user support
* [ ] Private user vaults
* [ ] Entry categorization

### Version 1.0

* [ ] Personal AI assistant
* [ ] Context aware retrieval
* [ ] Long term knowledge management
* [ ] Habit and trend analysis
* [ ] Reflection generation
* [ ] Deployment and cloud infrastructure

---

## Vision

MemVault aims to become a private, user controlled knowledge vault that helps individuals capture experiences, track personal growth, preserve context, and retrieve meaningful information from their past.

The project is being built with a strong focus on privacy, ownership, AI assisted organization, and long term personal knowledge management.

In parallel, MemVault will also serve as an end to end engineering project featuring containerization, CI/CD, infrastructure automation, monitoring, observability, and cloud deployment practices.

---

## License

MIT License
