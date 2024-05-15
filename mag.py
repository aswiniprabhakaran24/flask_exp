from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/statuspage",methods=["GET"])
def statuspage():
    status = request.args.get("textinput")
    return render_template("statuspage.html", status = status)
 
@app.route("/inputpage")
def input():
	return render_template("inputpage.html") 
    
if __name__ == "__main__":
	app.run()