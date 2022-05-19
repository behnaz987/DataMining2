from main import *
eighteen_percentage_of_total_trans_amount = (df['Total_Trans_Amt'].count())*0.8
count = 0
sns.histplot(x='Total_Trans_Ct', y='Total_Trans_Amt', data=df)
plt.show()
if __name__ == '__main__':
    y = df.Total_Trans_Amt.sort_values()
    y = pd.DataFrame(y)
    y = y.reset_index()
    total = df.Total_Trans_Amt.sum()
    print(total)
    print(0.8 * 10127)
    Sum = y.iloc[8101:-1, 1].sum(axis=0)
    print(Sum / total)
    # قانون پارتو برقرار نیست


