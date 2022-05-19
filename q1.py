import statistics
from main import *


def q_1():
    df['Income'] = df['Income_Category']
    df.loc[df['Income'] == 'Less than $40K', 'Income'] = 40000
    df.loc[df['Income'] == '$40K - $60K', 'Income'] = 50000
    df.loc[df['Income'] == '$60K - $80K', 'Income'] = 70000
    df.loc[df['Income'] == '$80K - $120K', 'Income'] = 100000
    df.loc[df['Income'] == 'Unknown', 'Income'] = 40000
    df.loc[df['Income'] == '$120K +', 'Income'] = 120000
    post_graduate = list()
    decorate = list()
    for i in range(0, 10127):
        if df["Education_Level"][i] == "Post-Graduate":
            post_graduate.append(df["Income"][i])
        if df["Education_Level"][i] == "Doctorate":
            decorate.append(df["Income"][i])
    post_graduate_avg = statistics.mean(post_graduate)
    decorate_avg = statistics.mean(decorate)
    if post_graduate_avg > decorate_avg:
        print("Stop! Post_graduate is enough")
    if decorate_avg > post_graduate_avg:
        print("Go decorate")
    if post_graduate_avg == decorate_avg:
        print("Do what you want")


if __name__ == '__main__':
    q_1()
# بر اساس نتایج ورود به بازار کار گزینه بهتری است