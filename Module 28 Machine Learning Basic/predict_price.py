# import pandas
# from sklearn.linear_model import LinearRegression
# # import matplotlib.pyplot as plt
# data = pandas.read_csv('iphone_price.csv')
# model = LinearRegression()
# # plt.scatter(data['version'], data['price'])
# # plt.show()
# model.fit(data[['version']], data[['price']])
# predicted_price = model.predict([[22]])
# print (predicted_price)

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ["a","b","c","d","e"])
print(s["a"])

