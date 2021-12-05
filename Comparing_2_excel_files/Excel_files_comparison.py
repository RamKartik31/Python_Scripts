import pandas as pd

df1=pd.read_excel('File1.xlsx')
df2=pd.read_excel('File2.xlsx')

l1 = df1['Path'].tolist()
l2 = df2['Path'].tolist()

# print(l1)
# print(l2)

for ele in l1:
    f = open('Missing_values.txt','a')
    if ele not in l2:
        # print(ele)
        # print(type(ele))
        f.write(ele+'\n')
f.close()