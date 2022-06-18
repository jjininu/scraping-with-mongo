import json

from flask import Flask,render_template,request


import mongodb
import scraping
from scraping import *
from mongodb import *

app  = Flask(__name__)

@ app.route('/',methods = ["GET","POST"])
def home_page():
    return render_template('home.html')


@app.route('/result',methods = ["GET","POST"])
def result():

    price1 = request.form["content1"]
    price2 = request.form["content2"]
    price = {'$lte' : int(price2)}
    input = {price1:price}


    data = retrive_data("House_data",input)
    result_addess = [i  for i in data]
    return render_template('result.html',result=result_addess)






if __name__ == '__main__':
    app.run(debug=True)
