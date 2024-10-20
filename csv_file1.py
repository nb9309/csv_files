import csv
cols = ['name','job','sal']
rows = [['naresh','python dev',40000],['suresh','java dev','39000'],['chandu','tester','41000']]
a = cols+rows

with open('job_data.csv','w') as fp:
    obj = csv.writer(fp)
    obj.writerow(cols)
    obj.writerows(rows)
    print(type(obj))
print('is file closed: ',fp.closed)

