from main import *

if __name__ == '__main__':
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Income_Category', y='Total_Trans_Ct', data=df)
    plt.show()
# با توجه به نمودار بالا تفاوت فاحشی بین تعداد تراکنش ها وجود ندارد

