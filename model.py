import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("dataset.csv")
y = df["mg_total"]
X= df.drop("mg_total", axis=1)

#split
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model
model = RandomForestRegressor()
model.fit(X_train, y_train)

from sklearn.metrics import r2_score

y_pred = model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, y_pred):.3f}")

import joblib
joblib.dump(model, "model.pkl")
print("Model salvat!")