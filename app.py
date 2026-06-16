from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

from database import init_db
from ai.extractor import extract_facts

app = Flask(__name__)

# Create database on startup
init_db()


@app.route("/")
def home():

    conn = sqlite3.connect("memvault.db")

    recent_memories = conn.execute(
        """
        SELECT *
        FROM memories
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        memories=recent_memories
    )

@app.route("/query", methods=["POST"])
def query():

    question = request.form["question"]

    conn = sqlite3.connect("memvault.db")

    if "weight" in question.lower():

        result = conn.execute(
            """
            SELECT fact_value
            FROM facts
            WHERE fact_type = 'weight'
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()

        conn.close()

        answer = (
            result[0]
            if result
            else "No weight data found."
        )

        return render_template(
            "answer.html",
            answer=answer
        )

    conn.close()

    return render_template(
        "answer.html",
        answer="I don't know yet."
    )
@app.route("/save", methods=["POST"])
def save_memory():

    memory = request.form["memory"]

    # Local timestamp
    timestamp = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    conn = sqlite3.connect("memvault.db")
    cursor = conn.cursor()

    # Save entry
    cursor.execute(
        """
        INSERT INTO memories
        (content, created_at)
        VALUES (?, ?)
        """,
        (memory, timestamp)
    )

    memory_id = cursor.lastrowid

    try:
        facts = extract_facts(memory)

        for key, value in facts.items():

            cursor.execute(
                """
                INSERT INTO facts
                (memory_id, fact_type, fact_value)
                VALUES (?, ?, ?)
                """,
                (
                    memory_id,
                    key,
                    str(value)
                )
            )

    except Exception as e:

        print("Fact extraction failed:", e)

    conn.commit()
    conn.close()

    return redirect("/memories")


@app.route("/delete/<int:memory_id>", methods=["POST"])
def delete_memory(memory_id):

    conn = sqlite3.connect("memvault.db")

    conn.execute(
        "DELETE FROM memories WHERE id = ?",
        (memory_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/memories")


@app.route("/memories")
def memories():

    conn = sqlite3.connect("memvault.db")

    rows = conn.execute(
        "SELECT * FROM memories ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "memories.html",
        memories=rows
    )


@app.route("/edit/<int:memory_id>")
def edit_memory(memory_id):

    conn = sqlite3.connect("memvault.db")

    memory = conn.execute(
        "SELECT * FROM memories WHERE id = ?",
        (memory_id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        memory=memory
    )


@app.route("/update/<int:memory_id>", methods=["POST"])
def update_memory(memory_id):

    updated_content = request.form["memory"]

    conn = sqlite3.connect("memvault.db")

    conn.execute(
        """
        UPDATE memories
        SET content = ?
        WHERE id = ?
        """,
        (updated_content, memory_id)
    )

    conn.commit()
    conn.close()

    return redirect("/memories")

@app.route("/facts")
def facts():

    conn = sqlite3.connect("memvault.db")

    rows = conn.execute(
        """
        SELECT *
        FROM facts
        ORDER BY id ASC
        """
    ).fetchall()

    conn.close()

    return render_template(
        "facts.html",
        facts=rows
    )


@app.route("/ask")
def ask_page():

    return render_template("ask.html")

if __name__ == "__main__":
    app.run(debug=True)
