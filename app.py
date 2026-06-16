from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Rasbeena's Dockerized Flask Application"

@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "application": "flask-app"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
