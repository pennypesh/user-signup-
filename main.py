from flask import Flask, request
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask (__name__)
app.config['DEBUG']= True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/welcome", methods=['POST'])
def welcome():
    user_name = request.form['user_name']
    password = request.form['password']
    verify =request.form['verify']
    email = request.form['email']
        
            
        

    user_name_error=''
    password_error=''
    verify_error=''
    email_error=''

    #Verify username
    if user_name =='':
        user_name_error="Please enter a valid username"
    elif len(user_name)<3 or len(user_name)>20:
        user_name_error="Username must be between 3 and 20 characters long"
        user_name = ''
    elif ' ' in user_name:
        user_name_error= "Your username cannot contain any spaces"
        


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
    if not user_name_error and not password_error and not verify_error and not email_error:
        template = jinja_env.get_template('welcome.html')
        return template.render(name=user_name)


    else:
        template = jinja_env.get_template('index.html')
        return template.render(name=user_name, user_name_error = user_name_error,password_error = password_error, verify_error=verify_error, email = email, email_error = email_error)

app.run()