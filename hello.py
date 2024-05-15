from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pageone")
def pageone():
	return render_template("firstpage.html")
    
@app.route("/pagetwo")
def pagetwo():
    return render_template("secondpage.html")
    
if __name__ == "__main__":
	app.run()