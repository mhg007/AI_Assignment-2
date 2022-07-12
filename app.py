import pickle
import re
from flask import Flask,render_template, request
import numpy as np
# import music
model = pickle.load(open('model_DT.pkl', 'rb'))
app = Flask(__name__)
@app.route("/")
def hello():
    # if request.method == 'POST':
    #     gender = request.form['gender']
    #     genre = music.genre(gender)
    #     print(genre)

    return render_template("index.html")

@app.route("/submit", methods = ["POST"])
def submit():
    print("HI")
    arr = [float(x) for x in request.form.values()]
    final = [np.array(arr)]
    for x in arr:
        print(x)
    print(final)
    prediction = model.predict(final)
    print(prediction)
    print("HI")

    return render_template("submit.html", prediction = prediction)
    
 
if __name__ == "__main__":
    app.run(debug=True)
    