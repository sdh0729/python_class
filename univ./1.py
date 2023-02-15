import pandas as pd

df = pd.DataFrame({'Number':[1,2,3,4,5,6],
                   'Name':['ITZY','TREI','Cheery Bullet','The Pink Lady','BTS','TWICE'],
                   'Pay':[12450,13450,14450,11450,15590,12650]})

df['rank'] = df.Pay.rank(method='max',ascending = False)
first = (df['rank'] ==1)
print(df)
print(df[first])


