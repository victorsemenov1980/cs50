import os
import flask
from flask import (Blueprint, send_from_directory, abort, request, current_app, render_template, redirect,url_for)               
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_login import UserMixin
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import requests
import json
app = Flask(__name__)



# Check for environment variable
if not os.getenv('DATABASE_URL'):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/",methods=["GET","POST"])
def index():
    log_in_message="Kindly log in below if already registered" 
    if request.method=="POST":
        email=request.form.get('email') 
        password=request.form.get('password')
        data=db.execute("SELECT * FROM users WHERE email = :a",{"a":email}).fetchone()
        if data==None:
            log_in_message="Wrong user. Try again, or register."
            return render_template ("index.html",log_in_message=log_in_message)
        else:
            if data.email==email and data.password==password:
                session["username"]=email
                return redirect(url_for("search"))
            else:
                log_in_message="Wrong password. Try again."
                return render_template ("index.html",log_in_message=log_in_message)
    return render_template('index.html',log_in_message=log_in_message)
        


@app.route("/search",methods=["GET","POST"])

def search():
    username=session.get('username')
    output=""
    session['book']=[]
    if request.method=="POST":
        session['book']=[]
        
        search=request.form.get('search')
        data=db.execute("SELECT * FROM books WHERE author iLIKE '%"+search+"%' OR title iLIKE '%"+search+"%' OR isbn iLIKE '%"+search+"%'").fetchall()
        for i in data:
            session['book'].append(i)
        if len(session['book'])==0:
            output='no books found'
    return render_template ("search.html",output=output,data=session['book'])

@app.route("/isbn/<string:isbn>",methods=["GET","POST"])

def book(isbn):
    output=""
    username=session.get('username')
    session["reviews"]=[]
    existing_review=db.execute("SELECT * FROM reviews WHERE isbn = :isbn AND user_email= :user_email",{"user_email":username,"isbn":isbn}).fetchone()
    if request.method=="POST" and existing_review==None:
        review=request.form.get('review') 
        rating=request.form.get('rating')
        db.execute("INSERT INTO reviews (isbn, review, rating, user_email) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":review,"c":rating,"d":username})
        db.commit()
    if request.method=="POST" and existing_review!=None:
        output="Sorry. You Only one review is allowed per book"
    
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "LQ1D378SOCttnAhqzexeMA", "isbns": isbn})
    average_rating=res.json()['books'][0]['average_rating']
    work_ratings_count=res.json()['books'][0]['work_ratings_count']
    reviews=db.execute("SELECT * FROM reviews WHERE isbn = :isbn",{"isbn":isbn}).fetchall() 
    for rev in reviews:
        session['reviews'].append(rev)  
    data=db.execute("SELECT * FROM books WHERE isbn = :isbn",{"isbn":isbn}).fetchone()
    return render_template("book.html",data=data,reviews=session['reviews'],average_rating=average_rating,ratings_count=work_ratings_count,username=username,output=output)

@app.route("/api/<string:isbn>")

def api(isbn):
    data=db.execute("SELECT * FROM books WHERE isbn = :isbn",{"isbn":isbn}).fetchone()
    
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "LQ1D378SOCttnAhqzexeMA", "isbns": isbn})
    average_rating=res.json()['books'][0]['average_rating']
    work_ratings_count=res.json()['books'][0]['work_ratings_count']
    x = {
    "title": data.title,
    "author": data.author,
    "year": data.year,
    "isbn": isbn,
    "review_count": work_ratings_count,
    "average_score": average_rating
    }
    
    api=json.dumps(x)
    return render_template("api.json",api=api)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("/"))
   

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        email=request.form.get('email') 
        password=request.form.get('password')
        data=db.execute("SELECT * FROM users WHERE email = :a",{"a":email}).fetchone()
        if data==None:
            db.execute("INSERT INTO users (email,password) VALUES (:a,:b)",{"a":email,"b":password})
            db.commit()
            session["username"]=email
            return redirect(url_for("search"))
        else:
            log_in_message="User already exist. Please log in"
            return render_template('cannotRegister.html',log_in_message=log_in_message)
    return render_template('register.html')

