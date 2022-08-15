#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:34:42 2022

@author: monica
"""

posts = [
    {
     'author':'ddg',
     'title': 'love1',
     'content': 'first meet',
     'date_posted':'march 21, 2020'
     },
    {
     'author':'mnk',
     'title': 'love2',
     'content': 'second meet',
     'date_posted':'march 21, 2022'
     }
]

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')



if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=1)
