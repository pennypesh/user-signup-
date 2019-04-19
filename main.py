from flask import Flask, request,render_template
import cgi
import os
import re

app = Flask (__name__)
app.config['DEBUG']= True

@app.route("/")
def index():    
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    user_name = request.form['user']
    password = request.form['pass']
    verify =request.form['secondpass']
    email = request.form['email']
        
            
        

    user_error=''
    password_error=''
    verify_error=''
    email_error=''

    #Verify username
    if user_name =='':
        user_error="Please enter a valid username"
    elif len(user_name)<3 or len(user_name)>20:
        user_error="Username must be between 3 and 20 characters long"
        user_name = ''
    elif ' ' in user_name:
        user_error= "Your username cannot contain any spaces"
        


    #verify first password
    if password =='':
        password_error = "Please enter a valid password"
    elif len(password)<3 or len(password)>20:
        password_error="Password must be between 3 and 20 characters long."
    elif " "in password:
         password_error="Your password cannot contain spaces."
    
    #verify second password
    if verify == '' or verify != password:
        verify_error="Please ensure that passwords match."
        verify = ''

    #verify email
    if email !='':
        match= re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match==None:
            email_error="Not a valid email address."    
    
    #without errors
    if not user_error and not password_error and not verify_error and not email_error:    
        return render_template('welcome.html',name=user_name)


    else:    
        return render_template('index.html',name=user_name, user_name_error = user_error,password_error = password_error, verify_error=verify_error, email = email, email_error = email_error)

app.run()