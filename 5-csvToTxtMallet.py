import csv

data=open("stemming+label_file.csv",'r',encoding='utf-8')
csv_reader_lines=csv.reader(data)
for one_line in csv_reader_lines:
    if one_line:
        id=one_line[0]
        str="E:\github\python\data_for_mallet_3\\"+id+".txt"
        f=open(str,'w',encoding='utf-8')
        sentence=one_line[4]
        sentence=sentence.replace("['","")
        sentence=sentence.replace("']","")
        sentence=sentence.replace("', '"," ")
        print(sentence)
        f.write(sentence)
        f.close()
data.close()