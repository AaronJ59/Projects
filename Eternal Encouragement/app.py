from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from helpers import synonym_check, image_find, popup_info
import os
import sqlite3
import random

# Configure application
app = Flask(__name__)



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route('/')
def home():
    session.clear()
    return render_template('homepage.html')


@app.route('/verses', methods=["POST", "GET"])
def verses():
    conn = sqlite3.connect("verses.db")
    cur = conn.cursor()

    if 'verses_loaded' not in session:
        session['verses_loaded'] = False

    if 'num_of_dict' not in session:
        session['num_of_dict'] = 0


    if request.method == "POST" and not session['verses_loaded']:

        user_input = request.form.get('text-form-field').lower()
        if not user_input:
            cur.close()
            conn.close()
            return redirect('/error')
        emotion_list = synonym_check(user_input)
        # if condition where synonym_check returns an error
        if emotion_list == "error":
            cur.close()
            conn.close()
            return redirect('/error')

        verses_lod = []
        for emotion in emotion_list:
             result = cur.execute("SELECT verse, reference FROM verses WHERE emotion = ?", (emotion,))
             verses = result.fetchall()

             for verse, reference in verses:
                 session['num_of_dict'] += 1
                 dict = {"verse": verse, "reference": reference}
                 verses_lod.append(dict)

        cur.close()
        conn.close()
        session['verses_loaded'] = True
        session['verses_list_of_dict'] = verses_lod
        random.shuffle(verses_lod)

        session['dict_num'] = 0
    if request.method == "POST" and session['verses_loaded']:
        if session['dict_num'] < session['num_of_dict']:
            VERSES_LOD = session['verses_list_of_dict'][session['dict_num']]
            IMAGE_PATH = image_find(VERSES_LOD['reference']).lower()
            AUTHOR_NAME = image_find(VERSES_LOD['reference'])
            AUTHOR_INFO = popup_info(IMAGE_PATH)
            session['dict_num'] += 1
        else:
            session['dict_num'] = 0
            print(session['verses_list_of_dict'])
            VERSES_LOD = session['verses_list_of_dict'][session['dict_num']]
            IMAGE_PATH = image_find(VERSES_LOD['reference']).lower()
            AUTHOR_NAME = image_find(VERSES_LOD['reference'])
            AUTHOR_INFO = popup_info(IMAGE_PATH)

        return render_template("verses.html", verses_lod=VERSES_LOD, image_path=IMAGE_PATH, author_info=AUTHOR_INFO, author_name=AUTHOR_NAME)


    else:
        return redirect('/')


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
