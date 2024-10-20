import csv
feilds = ['name','school','age']
dt = [{'name':'naresh','school':'nagaejuna','age':20},{'name':'suresh','school':'nagaejuna','age':21},{'name':'chandu','school':'nagaejuna','age':24}]

with open('school_data.csv','w') as fp:
    obj_w1 = csv.DictWriter(fp,feilds)
    obj_w1.writeheader()
    obj_w1.writerows(dt)
print('is file closed: ',fp.closed)