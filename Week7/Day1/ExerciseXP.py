import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse

# 1)
# def numpy_array(start,length,step):
#     # end=((end-1)*step)+
#     end=(step*length)+start
#     return np.arange(start,end,step)
# array=numpy_array(0, 100,4)
# print(array)
# print(array.shape)


# 2)
# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# a = a[~np.isnan(a)]
# print(a)



# 3)
# random_numpy= np.random.randint(100,size=100)
# random_numpy=  random_numpy.reshape(5,6 )
# print(np,max(random_numpy,axis=1))

# 4)
# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# print(series.value_counts())


# 5)
# series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# series =series.map(lambda x: parse(x))
# print("Day of month:")
# print(series.dt.day.tolist())
# print("Week number:")
# print(series.dt.isocalendar().week.tolist())
# print("Day of year:")
# print(series.dt.dayofyear.tolist())
# print("Day of week:")
# print(series.dt.dayofweek.tolist())


# 6)
df=pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df.rename(columns = {'Type':'TypeOfCar'}, inplace = True)
# print("the renaming was successful")
# print(df.info())
# print(df.head(10))
# print(df.isnull().sum().idxmax())


# 7)
# del df['EngineSize']
# del df['Length']


# 8)

# df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
#                     'weight': ['high', 'medium', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 9)})

# df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
#                     'kilo': ['high', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 6)})
# merged=pd.merge(df1,df2)
# df_merged = pd.merge(df1, df2, how='inner')
# print("the merge was succesful")


# 9.
# df = pd.DataFrame(["STD,City\tState",
# "33,Kolkata\tWest Bengal",
# "44,Chennai\tTamil Nadu",
# "40,Hyderabad\tTelengana",
# "80,Bangalore\tKarnataka"], columns=['row'])
# df= df.split(",",df)
# names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
# df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)
# df_mpg = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/')

# 10

# def scatter_plot():
#     df = pd.DataFrame([])
#     x = [1, 2, 3, 4]
#     y = [2, 20, 35, 6]
#     plt.scatter(x,y)
#     plt.xlabel('displacement')
#     plt.ylabel('acceleration')
#     plt.show()
# scatter_plot()

# 11
# def bar_plot():
#     df=pd.read_csv('')
#     df[df.cylinders =='1978']
#     df=df.index%2 ==0
#     df[df.cylinders =='toyota']
# bar_plot()

# 12
# def line_plot():
#     x=pd.read_csv('')
#     y=x.['weight']
# line_plot()
    
    