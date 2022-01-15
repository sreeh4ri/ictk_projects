# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 13:47:19 2022
@author: sreeh4ri
"""
from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, flash, abort
import json
import os.path
from werkzeug.utils import secure_filename
import constants

# App
app = Flask(__name__)
app.secret_key = constants.APP_SECRET


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if 'POST' == request.method:
        return store_url(request)
    else:
        return redirect(url_for('home'))


@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists(constants.URL_FILE):
        with open(constants.URL_FILE) as url_file:
            urls = json.load(url_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', filename='/user-uploads/' + urls[code]['file']))
    return abort(404)


@app.errorhandler(404)
def code_not_found(error):
    return render_template('code-not-found.html'), 404


def store_url(request):
    """Store URLs to a JSON file"""
    urls = {}
    # Check for existing file
    if os.path.exists(constants.URL_FILE):
        with open(constants.URL_FILE) as url_file:
            urls = json.load(url_file)
    # Check for duplicates
    if request.form['code'] in urls.keys():
        flash('Entered short code is already taken.')
        return redirect(url_for('home'))
    # Check code type
    if 'url' in request.form.keys():
        urls[request.form['code']] = {'url': request.form['url']}
    else:
        f = request.files['file']
        file_name = request.form['code'] + secure_filename(f.filename)
        f.save(constants.FILE_LOC + file_name)
        urls[request.form['code']] = {'file': file_name}
    # Update storage
    with open(constants.URL_FILE, 'w') as url_file:
        json.dump(urls, url_file)
    return render_template('your-url.html', code=request.form['code'])
