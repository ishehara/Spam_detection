Spam Detection Web Application
A simple web application that detects whether uploaded text is spam or not using Machine Learning. The application uses the Multinomial Naive Bayes classifier and CountVectorizer for text preprocessing, implemented through scikit-learn's Pipeline functionality.
Features

Simple and intuitive web interface
Upload text files for spam detection
Real-time classification results
Built with Flask backend and HTML frontend
Utilizes scikit-learn's ML pipeline for efficient processing

Tech Stack

Backend Framework: Flask
Frontend: HTML
Machine Learning: scikit-learn
Model: Multinomial Naive Bayes
Text Preprocessing: CountVectorizer
Implementation: Pipeline

Model Details
The spam detection model uses:

MultinomialNB: A probabilistic model particularly suited for text classification
CountVectorizer: Converts text into a bag-of-words representation
Pipeline: Combines preprocessing and model training into a single workflow
