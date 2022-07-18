f=open("t.txt","r",encoding="utf-8")
data=f.read()
f.close()
print(data)
data=data.replace("[","")
data=data.replace("]","")
lst=data.split(", ")

f=open("id_topic.txt","r",encoding="utf-8")
data=f.readlines()
f.close()

f=open("app_clusters.txt","w",encoding="utf-8")
cnt=0
for line in data:
    line=line.replace(" ","")
    line=line.replace(":","  ")
    line=line.replace("\n","  ")
    line+=str(lst[cnt])+"\n"
    cnt+=1
    f.write(line)
f.close()

