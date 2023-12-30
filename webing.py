from flask import Flask, render_template, request, redirect , url_for
import csv

app = Flask(__name__)

def saveing_csv(data):
    with open('database_web.csv', newline='', mode='a') as database:
        email=data['email']
        sub=data['subject']
        mes=data['message']
        fieldnames=['email','subject','message']
        spamwriter = csv.DictWriter(database, fieldnames=fieldnames)
        #spamwriter.writeheader()
        spamwriter.writerow({'email':email,'subject':sub,'message':mes})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page>')
def where(page):
    return render_template(page)  

@app.route('/thankyou.html')
def check():
    return render_template('/thankyou.html')

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if(request.method=='POST'):
        data= request.form.to_dict()
        name=str(data.get('email')).split('@')
        name=name[0]
        saveing_csv(data)
        return   render_template('/thankyou.html',name1=name)
    else:
        return'something went wrong'  
