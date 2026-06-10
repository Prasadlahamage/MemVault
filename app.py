from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
from database import init_db
import pytz


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

@app.route("/save", methods=["POST"])
def save_memory():

    memory = request.form["memory"]
    india = pytz.timezone("Asia/Kolkata")
    timestamp = datetime.now(india).strftime(
    "%d-%m-%Y %H:%M"
)

    conn = sqlite3.connect("memvault.db")

    conn.execute(
        """
        INSERT INTO memories
        (content, created_at)
        VALUES (?, ?)
        """,
        (memory, timestamp)
    )

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
if __name__ == "__main__":
    app.run(debug=True)