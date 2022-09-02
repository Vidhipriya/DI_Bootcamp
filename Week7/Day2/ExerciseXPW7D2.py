from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# import seaborn as sns

# 2)
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print(df.describe())
# df.groupby(['Survived']).sum().plot(kind='pie', y='Pclass',x='Sex')
# pie_chart=df[['Survived','Pclass','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']]
# # plt.pie(pie_chart)
# plt.show()

# 3a)dropna()
# 3b)_get_numeric_data()
# 3c)ax[0].set_title('survival rates')
# transformer = FunctionTransformer(np.log1p, validate=True)
# pd.DataFrame(transformer.transform(df[['Survived']].dropna())).plot(kind = 'kde', ax=ax[1]);
# ax[1].set_title('Did not survive ')
# plt.show()
# 3d)drop top and bottom 5% of the data
# 3e) del said columns

# 4)
X=df['Survived']
y=df['Fare']
X_train=df['Age']
X_test=df['Pclass']
y_train=df['Embarked']
y_test=df['Cabin']
X_train,X_test,y_train,y_test=train_test_split(X, y)

# PassengerId,
# Survived,
# Pclass,
# Sex,SibSp,
# Parch,Embarked 
# Ticket,Fare,cabin-ordinal


# nominal-Name