import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder 

data = pd.read_csv('data/bank_churn_dataset.csv')

encode = LabelEncoder()
data['Gender'] = encode.fit_transform(data['Gender'])

X = data.drop(columns=['Exited', 'CustomerId'])
Y = data['Exited']

scale = StandardScaler()
X = scale.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

model = DecisionTreeClassifier(max_depth=4)
model.fit(x_train, y_train)

joblib.dump(model,'models/model.joblib')
