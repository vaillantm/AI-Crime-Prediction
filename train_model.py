import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("rwanda_crime.csv")

# Show available columns
print("📋 Columns in CSV:", df.columns.tolist())

# Target and features (update this list based on actual CSV columns)
label_column = "Crime Detail"
features = ["Year", "Province", "Number of Cases"]  # Removed 'Quarter'

# Check if required columns exist
missing_cols = [col for col in features + [label_column] if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns in dataset: {missing_cols}")

# Prepare features and label
X = pd.get_dummies(df[features])  # One-hot encode categorical features
y = LabelEncoder().fit_transform(df[label_column])  # Encode target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "crime_model.pkl")
joblib.dump(LabelEncoder().fit(df[label_column]), "label_encoder.pkl")
joblib.dump(X.columns.tolist(), "model_features.pkl")

print("✅ Model trained and saved successfully.")
