from flask import Flask, render_template_string, request
from webhook import ai_agent
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>AI Agent Chat</title></head>
<body>
    <h2>Chat with AI Agent</h2>
    <form method="POST">
        <label for="query">Your Message:</label><br>
        <input type="text" id="query" name="query" required><br><br>
        <input type="submit" value="Send">
    </form>
    {% if user_input %}
        <p><strong>You:</strong> {{ user_input }}</p>
        <p><strong>AI:</strong> {{ ai_response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    user_input = ""
    ai_response = ""
    if request.method == "POST":
        user_input = request.form["query"]
        ai_response = ai_agent(user_input)
    return render_template_string(HTML, user_input=user_input, ai_response=ai_response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
