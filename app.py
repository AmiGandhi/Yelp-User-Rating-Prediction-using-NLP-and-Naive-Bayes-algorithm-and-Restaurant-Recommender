from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split	


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	
	review= pd.read_csv("yelp_data\\review_reduced.csv")
	X = review['text']
	y=review['stars']
	# Features and Labels
	bow_transformer = CountVectorizer().fit(X)
	X = bow_transformer.transform(X)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
	sm = SMOTE(random_state=2)
	X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())
	nb = MultinomialNB()
	nb.fit(X_train, y_train)
	
	if request.method == 'POST':
		comment = request.form['comment']
		data = comment
		data_transformed = bow_transformer.transform([data])
		my_prediction = nb.predict(data_transformed)[0]
	return render_template('result.html',prediction	 = my_prediction)


if __name__ == '__main__':
	app.run(debug=True)