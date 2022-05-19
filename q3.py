from main import *
from sklearn.tree import DecisionTreeClassifier


def q_3():
    df.drop([
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'],
        axis=1)
    df.loc[df['Attrition_Flag'] == 'Existing Customer', 'Attrition_Flag'] = 0
    df.loc[df['Attrition_Flag'] == 'Attrited Customer', 'Attrition_Flag'] = 1
    df.Attrition_Flag = df.Attrition_Flag.astype(int)
    # df_enc = pd.get_dummies(df)
    # df_enc = df_enc.drop(['CLIENTNUM'], axis=1)
    # df_x = df_enc.loc[:, df_enc.columns != 'Attrition_Flag']
    # df_y = df_enc['Attrition_Flag']
    # clf = DecisionTreeClassifier()
    # clf.fit(df_x, df_y)
    # pd.Series(clf.feature_importances_, index=df_x.columns[:]).plot.bar(color='steelblue', figsize=(16, 20))
    # plt.show()
    plt.figure(figsize=(12, 18))
    correlations = df.loc[:, df.columns != 'Attrition_Flag'].corrwith(df.Attrition_Flag)
    correlations = correlations[correlations != 1]
    correlations.plot.bar()
    plt.title('Correlation with Attrition_Flag')
    plt.show()


if __name__ == '__main__':
    q_3()
#     با توجه به نمودار همبستگی، کاهش مواردی که دارای مقدار منفی هستند باعث افزایش ریزش مشتری می شوند برای مثال هرچه میزان سرمایه در گردش بالاتر باشد احتمال ریزش کمتر است. Total_Trans_Count و Total_Revolving_Bol  بیشترین تاثیر را دارند