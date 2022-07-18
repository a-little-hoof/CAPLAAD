import csv
f=open("t.txt","r",encoding="utf-8")
data=f.read()
f.close()
print(data)
data=data.replace("[","")
data=data.replace("]","")
lst=data.split(", ")
print(len(lst))
print(type(lst))
f=open('for_mallet.csv', 'r',encoding='utf-8')
reader = csv.reader(f)
test_file=open('for_mallet_2.csv', 'w',encoding='utf-8')
writer= csv.writer(test_file)
cnt=0
for i in reader:
    if i:
        lt=i
        lt.append(lst[cnt])
        cnt+=1
        writer.writerow(lt)
        print(cnt)
f.close()
test_file.close()