import joblib
import pandas as pd
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("model\data.csv")
# print(df)

X = df[["Weight"]]
y = df["Species"]

clf = GaussianNB()
clf.fit(X, y)
joblib.dump(clf, "clf.pkl")