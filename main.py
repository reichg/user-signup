from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if len(request.form['username']) < 3 or len(request.form['password']) < 3 or len(request.form['username']) > 20 or len(request.form['password']) > 20 or (" " in request.form['username']) or (" " in request.form['password']):
            return render_template('index.html') 
        else:
            return successful_login()
        
        
        
    return render_template('index.html')


@app.route('/welcome')
def successful_login():
    if request.form['username'] == request.form['username']:
        return render_template('welcome.html')
    else:
        return redirect(url_for('index'))




app.run(debug=True)
