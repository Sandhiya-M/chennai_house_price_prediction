from flask import Flask,request,jsonify
app=Flask(__name__)
import util


@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/predict_home_price',methods=['POST','GET'])

def predict_home_price():
    area=float(request.form['area'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    age=int(request.form['age'])
    response=jsonify({
        'estimated_price': util.get_estimated_price(location,area,bhk,bath,age)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__=="__main__":
    print("Server started")
    util.load_saved_artifactes()
    app.run()
