#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:47:10 2018

@author: raunak
"""

from flask import Flask,render_template,url_for
app = Flask(__name__)
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
def hello():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('About.html',title="about")


if __name__ == "__main__":
    app.run(debug=True)
