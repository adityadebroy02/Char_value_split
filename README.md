# Char_value_split
<b>How to split by number of characters in python?</b>

Function to split your column values if that value is like this - '123456' or 'abcdef'

df -
index    Column_1
1         '123456'
2         '88956123'
3         '6780'

if you want to split your column(3-3) values in different column
like - 
Column_1  column_2 and so on....
'123'     '456'

then use the function -
       <b>var_list = char_split(df, 'column_name', n) <b/> 
       (*note here n will be the split of character for each column for 2-2 values in each column use n =2 and for 3-3 use n = 3 and so on)


import pandas as pd
df_dum = pd.DataFrame(var_list)

