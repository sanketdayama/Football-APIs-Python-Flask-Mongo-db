from flask import Flask,jsonify,request, session, redirect
import uuid
from app import db

class User:

    def start_session(self, user):
        del user['password']
        session['logged in'] = True
        session['user'] = user
        return jsonify(user), 200 

    def signup(self):
        
        user = {
        "_id":uuid.uuid4().hex,
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "password":request.form.get('password')

        }

        if db.Users.insert_one({"email": user['email']}):
            return jsonify({"error":"Email already exists"})
        if db.Users.insert_one(user):
            return self.start_session(user)
        return jsonify({"error":"signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')