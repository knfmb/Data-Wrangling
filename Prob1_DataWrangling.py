import pandas as pd
a = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
a1 = pd.DataFrame (a,columns=['Student','Math'])

b = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
b1 = pd.DataFrame (b,columns=['Student','Electronics'])

c = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
c1 = pd.DataFrame (c,columns=['Student','GEAS'])

d = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
d1 = pd.DataFrame (d,columns=['Student','ESAT'])

result1=pd.merge(a1,b1, on = 'Student')
result2 =pd.merge(result1,c1, on = 'Student')
final=pd.merge(result2,d1, on = 'Student')

long = pd.melt(final,id_vars = 'Student',value_vars = ['Math','Electronics','GEAS','ESAT'])
x = long.rename(columns = {'variable':'Subject','value':'Grades'})
y = x.sort_values('Student')
z = y.reset_index()
k = z.drop(columns='index')
