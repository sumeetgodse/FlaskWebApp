import requests
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=7abf3130a23c1df287e6622038944c8b'

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":    
        return redirect(url_for("result"))
    else:
        return render_template("home.html")

@app.route("/result",methods=["POST","GET"])
def result():
    city=request.form['loc']
    results=requests.get(url.format(city)).json()
    weather={
        'city':city,
        'country':results['sys']['country'],
        'temp':results['main']['temp'],
        'info':results['weather'][0]['description'],
        'icon':results['weather'][0]['icon']
    }
    print(weather)
    return render_template("result.html",weather=weather)

if __name__=="__main__":
    app.run()