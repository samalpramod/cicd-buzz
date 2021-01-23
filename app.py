import os
from flask import Flask
from buzz import generate_buzz

app = Flask(__name__)

@app.route("/")
def generate():
	page = "<html><body><h1>"
	page += generate_buzz.generate_buzz()
	page += "</h1></body></html>"
	
	return page
	
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(os.getenv('PORT',5000)))