from main import *
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def q_6():
    df.isna().sum()
    df.describe()
    df_1 = df.filter(['Customer_Age', 'Gender', 'Education_Level', 'Marital_Status', 'Income_Category'])
    df_1.Gender.replace({'F': 0, 'M': 1}, inplace=True)
    df_1.drop(df_1[df_1.Marital_Status == 'Unknown'].index, inplace=True)
    df_1.Marital_Status.replace({'Married': 0, 'Single': 1, 'Divorced': 2}, inplace=True)
    df_1.drop(df_1[df_1.Education_Level == 'Unknown'].index, inplace=True)
    df_1.Education_Level.replace(
        {'Graduate': 0, 'High School': 1, 'Uneducated': 2, 'College': 3, 'Post-Graduate': 4, 'Doctorate': 5},
        inplace=True)
    df_1.drop(df_1[df_1.Income_Category == 'Unknown'].index, inplace=True)
    df_1.Income_Category.replace({'Less than $40K': 0, '$80K - $120K': 1, '$60K - $80K': 2}, inplace=True)
    df_1.Income_Category.replace({'$40K - $60K': 3, '$120K +': 4}, inplace=True)
    df_1.head()
    X = df_1.drop(columns=["Income_Category"])
    y = df_1["Income_Category"]
    from sklearn.model_selection import train_test_split
    X_tr, X_test, y_tr, y_test = train_test_split(X, y, test_size=0.33, random_state=44, shuffle=True)
    my_array = np.array([[48, 1, 3, 0]])
    X_new = pd.DataFrame(my_array)
    # decision tree
    RF = RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0).fit(X_tr, y_tr)
    a = RF.predict(X_new)
    forest_score = round(RF.score(X_test, y_test), 4)
    print('سطح درآمد = ', a)
    # neural network
    from sklearn.neural_network import MLPClassifier
    NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(150, 10), random_state=1).fit(X_tr, y_tr)
    a = NN.predict(X_new)
    NN_score = round(NN.score(X_test, y_test), 4)
    print('سطح درآمد = ', a)


if __name__ == '__main__':
    q_6()
    # احتمالا میزان درآمد این مشتری در بازه 120-80 دلار قرار دارد
