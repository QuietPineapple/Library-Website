from flask import Flask, request, redirect
import requests


app=Flask(__name__) 
url='https://www.googleapis.com/books/v1/volumes'


res = requests.get(url)
print(res)


"""@app.route('/login', methods=["POST"])
def login():
    pass"""