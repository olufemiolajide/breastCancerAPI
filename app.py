from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

application = Flask(__name__, template_folder='templates')
app = application

@application.route("/")

@application.route("/cancer")
def cancer():
    return render_template("cancer.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = joblib.load(r"C:\Users\OOlajide\Working Folder\Udemy\zz Other Tutorials\Github - Good Projects\Health-App-main\Breast_Cancer API\cancer_model.pkl")
        result = loaded_model.predict(to_predict)
    return result[0]

@application.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #cancer
        if(len(to_predict_list)==5):
            result = ValuePredictor(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "Your risk of developing breast cancer is higher than national average. Please speak to your GP soon"
    else:
        prediction = "Your risk of breast cancer is relatievely low"
    return(render_template("result.html", prediction_text=prediction))       

if __name__ == "__main__":
#    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)