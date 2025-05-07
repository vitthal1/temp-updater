# temp_flask_app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

temp_storage = {"temp": "Not Set"}

html_form = """
<h2>Set Temperature</h2>
<form method="POST">
    <input name="temp" type="number" min="16" max="30" required>
    <input type="submit" value="Set">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def set_temp():
    if request.method == "POST":
        temp_storage["temp"] = request.form["temp"]
        return f"<h3>✅ Temperature set to {temp_storage['temp']} °C</h3>"
    return render_template_string(html_form)

@app.route("/temp", methods=["GET"])
def get_temp():
    return temp_storage["temp"]
