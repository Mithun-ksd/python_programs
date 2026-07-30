import pandas as pd
data1={
    'roll no':[101,102,103],
    'name':['Alice','Bob','Charlie'],
    'total_marks':[85,90,88]
    }
df1=pd.DataFrame(data1)
data2={
    'roll no':[104,105,106],
    'name':['David','Emma','France'],
    'total_marks':[98,87,84]
    }
df2=pd.DataFrame(data2)
merged_df=pd.concat([df1,df2],ignore_index=True)
print(merged_df)
