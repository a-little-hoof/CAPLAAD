import csv
import json
f=open("t.txt","r",encoding="utf-8")
data=f.read()
f.close()
data=data.replace("[","")
data=data.replace("]","")
lst=data.split(", ")
cal=0
write_file=open("label+category.csv",'w',encoding="utf-8")
writer= csv.writer(write_file)
with open('stemming+label_file.csv', 'r',encoding='utf-8') as f:
    reader=csv.reader(f)
    for i in reader:
        if i:
            print (i[0])
            if i[5]:
                str=i[5]
                if str.find("privacyTypes")==-1 or str[str.find('"privacyTypes"')+16]==']':
                    continue
                i.append(lst[cal])
                s=str.find('"privacyTypes"')
                e=str.find(',"relationships":')
                str=str[s+15:e]
                str=str[:-2]
                print(str)
                dic=json.loads(str)
                print(dic)
                i.append(dic)
                writer.writerow(i)
            cal+=1

write_file.close()

# for i in dic.keys():
#     print(i)   #输出键
#     print(dic[i])  #输出值

