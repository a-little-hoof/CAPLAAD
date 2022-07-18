import csv

data=open("stemming.csv",'r',encoding='utf-8')
csv_reader_lines=csv.reader(data)

new_data=open("stemming+label_file.csv",'w',encoding='utf-8')
writer=csv.writer(new_data)

for one_line in csv_reader_lines:
    if one_line:
        l=list(one_line)
        str="E:\BaiduNetdiskDownload\privacy_label\\auth\\"
        id=l[0]
        id+="_auth.txt"
        str+=id
        f=open(str,'r',encoding='utf-8')
        content=f.read()
        l.append(content)
        writer.writerow(l)
        f.close()
        print(id)

data.close()
new_data.close()