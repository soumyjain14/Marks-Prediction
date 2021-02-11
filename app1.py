from flask import Flask, render_template, redirect, request
import joblib

model=joblib.load("model.pkl")

app1=Flask(__name__)

@app1.route('/')
def hello():
	return render_template("index.html")

@app1.route('/',methods=['POST'])
def marks():
	if request.method == 'POST':
		hours=float(request.form['hours'])
		marks=str(model.predict([[hours]]))
		marks=marks[2:-2]


	#return "<h1> Your marks are: {}".format(marks)-one method
	return render_template("index.html",your_marks=marks)
	




if __name__=='__main__':
	app1.run(debug=True)