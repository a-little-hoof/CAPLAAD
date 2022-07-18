import csv
data=open("stemming+label_file.csv",'r',encoding='utf-8')
csv_reader_lines=csv.reader(data)
cnt=0
total=0
for one_line in csv_reader_lines:
    if one_line:
        str=one_line[5]
        if str.find("privacyTypes")!=-1:
            if str[174]!=']':
                cnt+=1
        total+=1
print(total)
print(cnt)
data.close()