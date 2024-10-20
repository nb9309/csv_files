import csv
with open("C:\\Users\\nares\\PycharmProjects\\csv_files\\job_data.csv","r") as fp:
    objread = csv.reader(fp)
    for i in objread:
        for j in i:
            print(j,end=' ')
        print()
print('is file closed: ',fp.closed)