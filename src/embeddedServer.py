from flask import Flask
from flask import render_template

class eServer():
    
    def __init__(self, port):
        self.app = Flask(__name__)
        self.port = port

        @self.app.route("/")
        def index():
            return render_template(r"eServer.html")
    
    def start(self):
        self.app.run(host="0.0.0.0", port=self.port)


if __name__ == "__main__":
    es = eServer()
    es.start()
