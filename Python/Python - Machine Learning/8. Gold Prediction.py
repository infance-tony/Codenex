import numpy as np
import pandas as pd

from google.colab import files
files.upload()

gold=pd.read_csv('gld_data.csv')
gold

gold.info()

print(gold.head())
print(gold.shape)

gold.isnull().sum()

from matplotlib import pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,6))
sns.histplot(gold['GLD'])
plt.title('GLD')
plt.show()

plt.figure(figsize=(6,6))
sns.barplot(x='USO',y='SLV',data=gold)

sns.scatterplot(x='SPX', y='GLD', data=gold)

x=gold.drop(['Date','EUR/USD'],axis=1)
y=gold['EUR/USD']

print(x)

print(y)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=1)
x_train

x_test.to_csv('gold_test.csv',index=False)
files.download('gold_test.csv')

# Linear Regression

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

from sklearn import metrics

training_data_prediction=model.predict(x_train)
r2_train=metrics.r2_score(y_train,training_data_prediction)
print('R squared value:',r2_train)
test_data_prediction=model.predict(x_test)
r2_test=metrics.r2_score(y_test,test_data_prediction)
print('R squared value:',r2_test)

# RandomForest regressor

from sklearn.ensemble import RandomForestRegressor

regressor=RandomForestRegressor(n_estimators=100)
regressor.fit(x_train,y_train)

training_data_prediction=regressor.predict(x_train)
r2_train=metrics.r2_score(y_train,training_data_prediction)
print('R squared value:',r2_train)
test_data_prediction=regressor.predict(x_test)
r2_test=metrics.r2_score(y_test,test_data_prediction)
print('R squared value:',r2_test)

input_data=(2057.639893,113.07,19.51,15.03)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=regressor.predict(input_data_reshaped)
print(prediction[0])

y_test 