from flask import Flask, render_template, request, redirect
import sqlite3

from database import init_db

app = Flask(__name__)

# Create database on startup
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save_memory():

    memory = request.form["memory"]

    conn = sqlite3.connect("memvault.db")

    conn.execute(
        "INSERT INTO memories(content) VALUES(?)",
        (memory,)
    )

    conn.commit()
    conn.close()

    return "Memory Saved Successfully!"
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

if __name__ == "__main__":
    app.run(debug=True)