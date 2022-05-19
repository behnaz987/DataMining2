from main import *
import matplotlib.pyplot as plt


def q_2():
    plt.figure(figsize=(12, 9))
    sns.countplot(x='Education_Level', hue='Attrition_Flag', data=df)
    plt.show()


if __name__ == '__main__':
    q_2()

# با توجه به نمودار گروه Graduated بهتر است
