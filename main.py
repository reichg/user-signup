from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    cred_error=''
    pass_error=''
    email_error=''
    if request.method == 'POST':
        if request.form['username'] == None:
            cred_error = 'Cannot be blank!'
        if request.form['password'] == None:
            pass_error = 'Cannot be blank!'
        if  len(request.form['username']) < 3 or len(request.form['username']) > 20:
            cred_error = 'Has to be 3 to 20 characters'
        if  len(request.form['password']) < 3 or len(request.form['password']) > 20:
            pass_error = 'Has to be 3 to 20 characters'
        if " " in request.form['username']:
            cred_error = 'No spaces allowed'
        if " " in request.form['password']:
            pass_error = 'No spaces allowed'
        if request.form['password'] != request.form['verify']:
            pass_error = 'Passwords must match'
        if request.form['email'] != "":
            count_x = 0
            count_y = 0
            for char in request.form['email']:
                if char == ".":
                    count_x += 1
                if char == "@":
                    count_y += 1
                if char == " ":
                    email_error = 'No spaces allowed!'
                   
            if count_x != 1 or count_y != 1:
                email_error = "Must contain 1 '@' and 1 '.' character" 
                
                 
                
        if not cred_error and not pass_error and not email_error:
            return redirect(url_for('welcome', userName=request.form['username']))
        else:
            return render_template('login.html', email_error=email_error, pass_error=pass_error, cred_error=cred_error)
    
    return render_template('login.html')
            

            

@app.route("/welcome", methods=['GET','POST'])
def welcome():
    username = request.args.get('userName')
    return render_template('welcome.html', userName=username)

           
           
app.run(debug=True)
