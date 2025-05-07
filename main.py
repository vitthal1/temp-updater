from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS from all domains

# Store temperature in memory
temp_storage = {"temp": "Not Set"}

# Minimal HTML form
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Set Temperature</title>
</head>
<body style="font-family: Arial; padding: 30px;">
    <h2>Set Room Temperature (°C)</h2>
    <form method="POST">
        <input name="temp" type="number" min="16" max="30" required>
        <input type="submit" value="Set">
    </form>
    {% if temp %}
        <h3 style="color: green;">✅ Temperature set to {{ temp }} °C</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def set_temp():
    if request.method == "POST":
        temp = request.form.get("temp")
        if not temp:
            return "❌ Temperature not provided", 400
        temp_storage["temp"] = temp
        return render_template_string(html_form, temp=temp)
    return render_template_string(html_form)

@app.route("/temp", methods=["GET"])
def get_temp():
    return jsonify({"temperature": temp_storage["temp"]}), 200

# Optional: A simple health check
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
