import sys
from pathlib import Path
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.model import SpaceClassifier

class TestSpaceModel(unittest.TestCase):
    
    def setUp(self):
        self.classifier = SpaceClassifier(model_type='logreg')
        # Ttraining dataset
        X_train = ["star shine bright", "galaxy spiral", "planet rock gas"]
        y_train = ["Star", "Galaxy", "Planet"]
        self.classifier.train(X_train, y_train)

    def test_prediction(self):
        # Checking if model is predicting correctly
        text = "shine bright"
        prediction = self.classifier.predict(text)
        self.assertIsInstance(prediction, str)
        # Checking if prediction is one of the classes
        self.assertIn(prediction, ["Star", "Galaxy", "Planet"])

    def test_probabilities(self):
        text = "spiral galaxy"
        probs = self.classifier.predict_proba(text)
        
        self.assertIsInstance(probs, dict)
        # Check if probabilities sum up to 100
        total_prob = sum(probs.values())
        self.assertGreater(total_prob, 99.0)

if __name__ == '__main__':
    unittest.main()