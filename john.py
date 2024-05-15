from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    name = "Aswini"
    notification = 6
    mail = 2
    return render_template("dashboard.html",name_temp = name,notification_temp = notification,mail_temp = mail)
   
if __name__ == "__main__":
	app.run()