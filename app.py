from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Sarina - DevOps Task 2</h1>
    <p>Deployed successfully with Dokku 🚀</p>
    """
