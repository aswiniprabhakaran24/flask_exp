from flask import Flask

app = Flask(__name__)

@app.route("/sai")
def index():
    return "Flask Working fine"
    
if __name__== "__main__":
    app.run()	