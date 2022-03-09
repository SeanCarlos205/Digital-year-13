from flask import render_template, url_for, flash, redirect
from main_app import app
from main_app.forms import RegistrationForm, LoginForm
from main_app.models import User, Post


posts = [
    
    {
        'author': 'Sean Carlos',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 15, 2022'        
    },
    
    {
        'author': 'Joem Ama',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 17, 2022'        
    },
    
    {
        'author': 'Jenna Tolls',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'February 18, 2022'        
    }
    
]

#Route for home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

#Route for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

#Route for registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#Route for login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password123':
            flash('You have been logged in!', 'success')
            return redirect(url_for(home))
        else:
            flash('Login failed. Please check your username and password', 'danger6')
    return render_template('login.html', title='Login', form='forms')