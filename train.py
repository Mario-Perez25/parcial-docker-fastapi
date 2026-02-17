import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Dataset estático
data = {
    "edad": [20, 25, 30, 35, 40],
    "ingresos": [2000, 2500, 3000, 3500, 4000],
    "compra": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["edad", "ingresos"]]
y = df["compra"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "modelo.pkl")
print("Modelo entrenado y guardado como modelo.pkl")
