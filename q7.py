from main import *
if __name__ == '__main__':
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Customer_Age', hue='Attrition_Flag', data=df)
    plt.show()
    #  با توجه به نمودار اهمیت بازه سنی 36 تا 55 مشهود است