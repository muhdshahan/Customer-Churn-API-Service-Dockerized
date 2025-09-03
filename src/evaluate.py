import joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('data/bank_churn_dataset.csv')

encode = LabelEncoder()
df['Gender'] = encode.fit_transform(df['Gender'])

X = df.drop(columns=['Exited', 'CustomerId'])
Y = df['Exited']

scale = StandardScaler()
X = scale.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)


model = joblib.load('models/model.joblib')

y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")