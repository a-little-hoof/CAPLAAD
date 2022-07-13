import gcld3
import csv

data=open("data.csv",'r',encoding='utf-8')
#old file
new_data=open("data_with_language.csv",'w',encoding='utf-8')
writer=csv.writer(new_data)
#new file
detector=gcld3.NNetLanguageIdentifier(min_num_bytes=0,max_num_bytes=1000)
csv_reader_lines=csv.reader(data)
for one_line in csv_reader_lines:
    l=list(one_line)
    if l:
        sentence=l[2]
        result=detector.FindLanguage(text=sentence)
        l.append(result.language)
        print(l[3])
        writer.writerow(l)


data.close()
new_data.close()