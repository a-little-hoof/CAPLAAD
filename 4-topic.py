f=open("E:\Mallet-202108-bin\Mallet-202108\\topic_file_topic.txt","r",encoding="utf-8")
write_file=open('id_topic.txt', 'w',encoding='utf-8')
data=f.readlines()
for line in data:
    line=list(line.split("\t"))
    dict={}
    for i in range(2,32,1):
        line[i]=float(line[i])
        dict[i-2]=line[i]
    dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    lst=[]
    for i in range(4):
        if dict[i][1]>=0.05:
            lst.append(dict[i][0])
    line[1]=line[1].replace("file:/E:/github/python/data_for_mallet_2/","")
    line[1] = line[1].replace(".txt","")
    write_str=line[1]+":"+str(lst)+'\n'
    print(write_str)
    write_file.write(write_str)

f.close()
write_file.close()
