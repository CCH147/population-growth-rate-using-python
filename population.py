import pandas as pd
from pandas import Series, DataFrame
import numpy as np

rate = 0.011 #1.1%成長率
pop = 683059 #683,059(0000)
a = 0
n = np.empty(20) #numpy大小20 的空陣列

df1= {'Year':[0],'Expect Population':[pop],'Increase Population':[0]} #生成key分別為(年、預期人數、增加人數)的字典
df2 = pd.DataFrame(df1) #將字典轉換成DataFrame格式
df3 = df2.copy() #複製一份
df3['Year'] = "This Year"
df3['Expect Population'] = (format(int(df2['Expect Population']), ',d')) #內建函式 每隔千位隔逗號
df3['Increase Population'] = (format(int(df2['Increase Population']), ',d')) #內建函式 每隔千位隔逗號
print(df3.to_string(index=False) #顯示初始的年、預期人數、增加人數
)

for i in range(1,76): #總共做75次
    df2["Year"] = df3["Year"] = i #將1~75(i)丟到Year列
    df2['Increase Population'] = 0 #每次迴圈都將增加人數初始化
    oldpop = float(df2['Expect Population']) #保存這一年的人數
    df2['Expect Population'] = oldpop * (1 + rate) #計算下一年預期人數
    newpop = float(df2['Expect Population']) #將下一年預期人數保存
    Inpop = newpop - oldpop #增加人數即為 (下一年預期人數 - 這一年預期人數)
    df2['Increase Population'] = Inpop 
    
    df3['Expect Population'] = (format(int(df2['Expect Population']), ',d')) #內建函式 每隔千位加上逗號
    df3['Increase Population'] = (format(int(df2['Increase Population']), ',d')) #內建函式 每隔千位加上逗號
    if i < 35 :
        print('{0:^17}'.format(df3.iat[0,0]),'{0:^11}'.format(df3.iat[0,1]),'{0:^29}'.format(df3.iat[0,2])) #(.iat為 通過行與列取值 迴圈內做75次)
    else:
        print('{0:^17}'.format(df3.iat[0,0]),'{:<0}'.format(df3.iat[0,1]),'{0:>19}'.format(df3.iat[0,2])) #(.iat為 通過行與列取值 迴圈內做75次)  
     
    if df2.iat[0,1] >= pop * 2 : #搜尋人口為兩倍的年份
        n[a] = i #將年份(即為i)丟入numpy空陣列中  從n[0]開始丟入空陣列
        a = a + 1 #a初始值為0 

print('{0:^18}'.format('自從第') , '{0:<1}'.format(int(n[0])) ,'{0:^17}'.format('年開始為原人口兩倍')) #印出n[0](即為人口開始變為兩倍的第一年)
        
    
    




