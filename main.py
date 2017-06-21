from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == None or request.form['password'] == None or request.form['verify'] == None or len(request.form['username']) < 3 or len(request.form['username']) > 20 or len(request.form['password']) < 3 or len(request.form['password']) > 20 or " " in request.form['username'] or " " in request.form['password']:
            return render_template('login.html')
        elif request.form['password'] != request.form['verify']:
            return render_template('login.html')
        elif request.form['email'] == "":
            return redirect(url_for('welcome'))
        else:
            count_x = 0
            count_y = 0
            for char in request.form['email']:
                if char == ".":
                    count_x += 1
                elif char == "@":
                    count_y += 1
                elif char == " ":
                    return render_template('login.html')

            if count_x == 1 and count_y == 1:
                return redirect(url_for('welcome'))
    return render_template('login.html')
    

@app.route("/welcome", methods=['GET','POST'])
def welcome():
    #username = request.form['username']
    return render_template('welcome.html')

           
           
app.run(debug=True)
