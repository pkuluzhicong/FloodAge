from flask import Flask, url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
	#return 'hello'
	return '<h1>Hello World!</h1>'
	
#@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

@app.route('/login',methods=['POST','GET'])
def login():
	error = None
	if request.method == 'Post':
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	return render_template('login.html',error=error)


@app.route('/user/<int:username>',methods=['GET','POST'])
def show_user_profile(username):
	return 'User %s' % username

if __name__ == '__main__':
	app.run(debug=True)
	

