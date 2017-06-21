from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid creds'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


@app.route("/welcome")
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

           
           

app.run(debug=True)
