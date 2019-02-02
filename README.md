The repository contains all the required files and the data for performing User Rating Prediction and Restaurant Recommendation.

The file structure is as follows: User_Rating_Prediction_using_NLP_and_Restaurant_Recommendation - Copy.ipynb - This fle contains the code for User rating prediction and restaurant recommendation.

YELP_EDA.ipynb - This file contains the Exploratory Data Analysis performed on the yelp dataset before making any predictions or recommendations to have an idea of the data available.

The data has been fetched from https://www.kaggle.com/yelp-dataset/yelp-dataset 
Steps to process data:
Once you download the zip file, write the following commands to exactly get the amount of rows that have been used in this project.
Extract all the files under yelp_data and while reading each file, make sure to add the nrows = 100000 parameter while reading individual files in Pandas Dataframe. So, the syntax would be: import pandas as pd review = pd.read_csv('yelp_data\review.csv', nrows=100000) 

app.py - Contains the code which invokes a flask application where the user can enter any text in the text box in the form of a review to get a possible prediction based on natural language processing performed on the text entered. For running this file, you need to have flask installed. If you don't have it installed, you can do pip import flask or python -m pip install flask from command line. Once flask is installed, you can open your terminal and write the command python app.py which would give you a localhost IP address. Copy that IP address on your browser and hit enter. You will get redirected to a web page which would allow you to enter text into a box followed with a predict button. Once you hit the predict button, wait for sometime as the model gets trained for predicting the possible user review which he/she will give to the restaurant based on his/her reviews.

home.html - HTML file containing the UI for the home page to enter the user review and submit it

result.html - HTML file containing UI for the result predicted user rating based on the input user review

styles.css - Stylesheet for the webpage designed

OVERVIEW:

• Predicted user ratings by implementing NLP on yelp user reviews and recommended food related restaurants to the user. 
• Examined user review text with various techniques involved in text mining and text analysis
• Handled imbalanced dataset using SMOTE technique for the positively skewed data in order to improve the accuracy. 
• Predicted user ratings on a baseline model where only punctuation's in the review is removed and compared to pre-processed model consisting of entire text preprocessing on user reviews
• Trained the model to predict ratings using Naïve Bayes Algorithm and evaluated the performance based on confusion matrix and classification report consisting of precision, recall and f1-measure
• Arrived at a conclusion that baseline model predicts user rating better than another model which proved that it is not always necessary to pre-process text before making any predictions and it completely depends on the data that we work on.

• Further, predicted the user ratings for food related restaurants using various models like BaselineOnly, KNNBaseline (user-based and item-based collaborative filtering method) and matrix factorization methods like Singular-Value Decomposition (SVD) and SVDpp. 
• Evaluated the performance by calculating the average RMSE and MAE on 3-fold cross validation. 
• Implemented Review based restaurant recommendation to recommend top-N restaurants to the user.

• Created a web application and deployed it on docker to find the predicted user rating based on the input user reveiw text.

Language: Python

Libraries used : scikit-learn, statsmodels, nltk, wordcloud, surprise, networkx, pandas, numpy, matplotlib, seaborn

Recommender System Techniques: Content-Based Recommendation and Collaborative Filtering

NLP: Tokenization, POS tagging, Stemming, Lemmatization, Bag of Words, ngrams

Data Visualization: Tableau and Python Libraries
