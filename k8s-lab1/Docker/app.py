import sys
from flask import Flask

app = Flask(__name__)
VERSION = "1.0.1"

@app.route('/')
def home():
    return f"Backend v{VERSION} is running on Kubernetes!"

if __name__ == "__main__":
    print(f"Starting python-backend v{VERSION}")
    sys.stdout.flush()
    app.run(host="0.0.0.0", port=5000)
