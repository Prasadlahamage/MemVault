# MemVault

MemVault is a personal memory management application built with Flask and SQLite.

It allows users to capture, manage, and revisit daily memories in a simple and organized manner. The long-term vision is to evolve MemVault into an AI-powered personal memory vault capable of understanding, organizing, and retrieving meaningful insights from daily logs.

---

## Features

### Current Features

* Create memories
* View saved memories
* Edit existing memories
* Delete memories
* Store memories in SQLite
* Local timestamp support (IST)
* Recent memories displayed on the homepage

### Planned Features

* AI-powered memory summarization
* Fact extraction (weight, steps, food, activities, etc.)
* Semantic memory search
* Weekly and monthly reflections
* Long-term memory insights
* ChromaDB integration
* Local LLM integration using Ollama
* Agentic memory workflows

---

## Tech Stack

### Backend

* Flask
* SQLite

### Future Integrations

* Ollama
* Qwen 3
* ChromaDB
* LangGraph

---

## Project Structure

```text
MemVault/
│
├── app.py
├── database.py
├── memvault.db
│
├── templates/
│   ├── index.html
│   ├── memories.html
│   └── edit.html
│
├── static/
│
├── requirements.txt
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

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Database

MemVault uses SQLite for local storage.

The database file is created automatically on startup if it does not exist.

Current schema:

### memories

| Column     | Type    |
| ---------- | ------- |
| id         | INTEGER |
| content    | TEXT    |
| created_at | TEXT    |

---

## Development Roadmap

### Version 0.1

* [x] Create memory
* [x] View memories
* [x] Edit memory
* [x] Delete memory
* [x] Local timestamp support

### Version 0.2

* [ ] AI memory summarization
* [ ] Fact extraction
* [ ] Search memories

### Version 0.3

* [ ] Long-term memory system
* [ ] Semantic search
* [ ] Memory insights

### Version 1.0

* [ ] Personal AI memory assistant
* [ ] Context-aware memory retrieval
* [ ] Habit and trend analysis
* [ ] Reflection generation

---

## Vision

MemVault aims to become a private, local-first AI memory system that helps users capture experiences, track personal growth, and retrieve meaningful information from their past without relying on external cloud-based AI services.

The project is designed with privacy, ownership, and long-term personal knowledge management in mind.

---

## License

MIT License
