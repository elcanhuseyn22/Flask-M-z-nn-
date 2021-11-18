from flask import Flask,render_template,request
import requests
app = Flask(__name__)

api_key = "e463b8836b5b7ca7cbe09646f80d378f"
url = "http://data.fixer.io/api/latest?access_key="+api_key

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        
        firstCurrency = request.form.get("firstCurrency") #usd
        secondCurrency = request.form.get("secondCurrency") #azn

        amount = request.form.get("amount") #100

        response = requests.get(url)

        infos = response.json()

        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue/firstValue)*float(amount)

        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amunt"] = amount
        currencyInfo["result"] = result
        return render_template('index.html',info = currencyInfo)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)