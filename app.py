from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")

def home():
    return f"This is from {socket.getfqdn()}"   # this gets the domain name 

if __name__ == "__main__":
    app.run(debug=True)