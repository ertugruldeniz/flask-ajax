from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/index")
def index():
     name = "Merhaba Ben Ertuğrul"
     numbers=[1,2,3,4,5,6,7,8,9,10]
     return render_template("index.html",name=name,numbers=numbers) #


@app.route("/toplam",methods=["GET","POST"])
def toplam():
    if request.method=="POST":
        json = request.get_json()
        number1 = json['number1']
        number2 = json['number2']
        return jsonify(toplam=int(number1)+int(number2))

    else:
        return render_template("toplam.html")



if __name__=="__main__":
    app.run(debug=True)