from tasks import *
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/time/')
def show_time():
	update.delay()
	result = print_now.delay()
	return result.wait().isoformat()

if __name__ == '__main__':
	app.run(debug=True)
