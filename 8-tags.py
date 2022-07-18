import csv
f=open("label+category_new.csv",'r',encoding="utf-8")
reader=csv.reader(f)
my_set=set()
for i in reader:
    if i:
        str=i[5]
        lst=str.split("', '")
        for j in lst:
            if j.find("identifier")!=-1:
                substr=j[j.find("identifier")+14:]
                print(substr)
                my_set.add(substr)
print(my_set)
f.close()