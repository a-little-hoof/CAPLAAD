import csv
import os

data=open("data.csv",'w',encoding='utf-8')
writer=csv.writer(data)

def get_description(file_name,id):
    text=open(file_name,'r',encoding='utf-8')
    content=text.read()
    text.close()
    list=id.split('.')
    p1=content.find('"description":{"standard":"')
    subcontent=content[p1+27:]
    p2=subcontent.find('"},"')
    list.append(subcontent[:p2])
    p1=content.find("apps.apple")
    subcontent=content[p1:]
    p2=subcontent.find('","')
    list[1]=subcontent[:p2]
    print(list[0])
    writer.writerow(list)



for path,folder,file in os.walk('E:\BaiduNetdiskDownload\\app_info_part1\info'):
    for name in file:
        if(name.startswith('._')):
            continue
        file_name=os.path.join(path,name)
        get_description(file_name,name)

for path,folder,file in os.walk('E:\BaiduNetdiskDownload\\app_info_part2\info_part2'):
    for name in file:
        if(name.startswith('._')):
            continue
        file_name=os.path.join(path,name)
        get_description(file_name,name)

data.close()