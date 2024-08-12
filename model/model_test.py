import pandas as pd
import joblib

X = pd.DataFrame([[3.5]], columns=["Weight"])
clf = joblib.load('model\clf.pkl')
prediction = clf.predict(X)[0]
print(prediction)