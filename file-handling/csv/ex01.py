import csv
with open("csv01.csv","r") as f:
    r=csv.reader(f)
    # print(r)--csv reader object
    data=list(r)
    for d in data:
        #print(d)
        pass
    
with open("csv01.csv","a",newline='') as f:
    w=csv.writer(f)
    w.writerow(["DATE","ESTIMATE_TYPE","TENURE","PRIVATE_DWELLING"])
    s="30 Sep 2021,mean quarter ended,free,67500".split(",")
    w.writerow(s)