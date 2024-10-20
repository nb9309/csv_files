import csv
with open('job_data.csv','r') as fp:
    obj_read_dict = csv.DictReader(fp)
    for i in obj_read_dict:
        for col,row in i.items():
            print('{} ------> {}'.format(col,row))
        print()