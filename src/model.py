import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

class SpaceClassifier:
    
    def __init__(self, model_type='logreg'):
        self.model_type = model_type
        
        if model_type == 'nb':
            clf = MultinomialNB()
        elif model_type == 'logreg':
            clf = LogisticRegression(max_iter=1000, class_weight='balanced')
        else:
            raise ValueError("Unknown model type. Choose 'nb' or 'logreg'.")

        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english', max_features=15000, ngram_range=(1, 2))),
            ('clf', clf)
        ])
        
    def train(self, X_train, y_train):
        print(f"Training {self.model_type.upper()} model...")
        self.pipeline.fit(X_train, y_train)
        print("Training complete.")

    def evaluate(self, X_test, y_test):
        predictions = self.pipeline.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)
        return acc, report

    def predict(self, text):
        if isinstance(text, str):
            text = [text]
        return self.pipeline.predict(text)[0]
    
    def predict_proba(self, text):
        if isinstance(text, str):
            text = [text]
        
        probs = self.pipeline.predict_proba(text)[0]
        
        classes = self.pipeline.classes_
        
        result = {c: round(p * 100, 2) for c, p in zip(classes, probs)}
        return result

    def save(self, filepath):
        joblib.dump(self.pipeline, filepath)
        print(f"Model saved to {filepath}")

    def load(self, filepath):
        self.pipeline = joblib.load(filepath)
        print(f"Model loaded from {filepath}")