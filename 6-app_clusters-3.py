import csv
f=open('app_clusters.csv', 'r',encoding='utf-8')
reader = csv.reader(f)
dict={}
cnt={}
for i in reader:
    if i:
        i[2]=int(i[2].replace("\n",""))
        if dict.get(i[2])==None:
            dict[i[2]]={}
            cnt[i[2]]=0
        cnt[i[2]]+=1
        i[1] = i[1].replace("[", "")
        i[1] = i[1].replace("]", "")
        i[1] = i[1].split(",")
        for item in i[1]:
            if dict[i[2]].get(item)==None:
                dict[i[2]][item] = 1
            else:
                dict[i[2]][item] += 1
print(dict)
f.close()
for i in range(0,32,1):
    dict[i]=sorted(dict[i].items(),key=lambda x:x[1],reverse=True)
dict=sorted(dict.items(),key=lambda x:x[0])
cnt=sorted(cnt.items(),key=lambda x:x[0])
f=open("app_clusters_final.csv","w",encoding="utf-8")
writer= csv.writer(f)
for i in dict:
    end_lst=[]
    end_lst.append(i[0])
    end_lst.append(cnt[i[0]])
    end_lst.append(i[1])
    print(end_lst)
    writer.writerow(end_lst)
f.close()