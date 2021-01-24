import os
import signal
from flask import Flask, render_template
from buzz import generate_buzz

app = Flask(__name__)

#signal.signal(signal.SIGINT, lambda s, f:os,_exit(0))
signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate():
	#page = "<html><body><h1>"
	#page += generate_buzz.generate_buzz()
	#page += "</h1></body></html>"
	buzz = generate_buzz.generate_buzz()
	return render_template('index.html',buzz=buzz)
	
	return page
	
if __name__ == "__main__":
	#app.run(host='0.0.0.0',port=int(os.getenv('PORT',5000)))
	app.run(host='0.0.0.0',port=os.getenv('PORT'))