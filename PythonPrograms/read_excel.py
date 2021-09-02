import pandas

td_excelread = pandas.read_excel('example.xlsx');

for row in td_excelread.itertuples():
    #print(row)
    sal=row.Salary
    if sal>20000 and sal<30000:
        print('Grade C')
    elif sal>=30000 and sal<50000:
        print('Grade B')
    elif sal>=50000:
        print('Grade A')
    else:
        print('Grade F')
   
       

