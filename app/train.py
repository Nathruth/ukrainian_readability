import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#Load the data
cleaned_data = pd.read_csv('../data/cleaned_data.csv')

# Split features and the target
X = cleaned_data[['words', 'sentences', 'letters', 'avg_word_len', 'avg_sent_len', 'syllables', 'avg_word_syl']]
y = cleaned_data['level']
le = LabelEncoder()
y_encoded = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(
   X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# Train model RF
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)
model.fit(X_train, y_train)

# Print results
from sklearn.metrics import classification_report, accuracy_score

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Train the model  XGBoost
from xgboost import XGBClassifier

xgb = XGBClassifier(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)
xgb.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Check params
from sklearn.model_selection import GridSearchCV

params = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), params, cv=3, scoring='accuracy')
grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)
print("Best score:", grid.best_score_)



# Save model
with open("../model/ukrainian_readability_model.pkl", "wb") as f:
    pickle.dump((model, le), f)
print("Model trained and saved, Master.")