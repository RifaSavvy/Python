import pandas as pd
s=pd.Series([1,3,5,7,9])
print(s)

s=pd.Series([1,3,5,7,9],index=['a','b','c','d','e'])
print(s)

data={'Name':['Alice','Bob','Charles'],
	'Age':[25,30,35],
	'City':['New York','Los Angeles','Chicago']}
	
df=pd.DataFrame(data)
print(df)

ages=df['Age']
print(ages)












