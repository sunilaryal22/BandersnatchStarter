from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib 
from sklearn.exceptions import NotFittedError
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
class Machine:
    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])

        # Initialize the model without a pipeline or scaler for simplicity
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('clf' , RandomForestClassifier(n_estimators=100))])
    
        # Fit the model
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):

        # Predict the class label for the input
        predictions = self.model.predict(pred_basis)
        
        confidence = self.model.predict_proba(pred_basis).max()  # Max probability per row

    
        return *predictions, confidence

    def save(self, path: str):
        """Save the model to a file."""
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")

    # this supposed to be a static method
    def open(path: str):
        """Load the model from a file."""
        model = joblib.load(path)
        print(f"Model loaded from {path}")
        return model

    def info(self):
        """Return the name of the model."""
        return self.name
