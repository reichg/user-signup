from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('welcome.html')
         
    else:
        return render_template('index.html') 


@app.route('/welcome')
def successful_login():
    if request.form['username'] == request.form['username']:
        return render_template('welcome.html')
    else:
        return redirect(url_for('index'))




app.run(debug=True)
