import csv
f=open("label+category.csv",'r',encoding="utf-8")
reader=csv.reader(f)
write_file=open("label+category_new.csv",'w',encoding="utf-8")
writer= csv.writer(write_file)

cnt=0
for i in reader:
    if i:
        cnt+=1
        i.pop(4)
        i.pop(4)
        if i[5].find("DATA_NOT_COLLECTED")!=-1:
            i[5]="None"
        writer.writerow(i)
        print(cnt)
print(cnt)
f.close()
write_file.close()