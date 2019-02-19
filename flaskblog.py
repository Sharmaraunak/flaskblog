#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:47:10 2018

@author: raunak
"""

from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '5bcc0f9e34c15efa9fefb136c16730ec'
posts = [
            {
                'author':'Raunak Sharma',
                'title':'blog post 1',
                'content':'my first post',
                'date':'September 16 2018'
            },
            {
                'author':'Raunak Sharma',
                'title':'blog post 1',
                'content':'my first post',
                'date':'September 16 2018'

            }
        ]

@app.route("/")
def home():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('About.html',title="about")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {{form.username.data}}!","success")
        return redirect(url_for('home'))
    return render_template('register.html',title="Register",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title="Login",form=form)
    


if __name__ == "__main__":
    app.run(debug=True)
