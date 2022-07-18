import csv
f=open("app_clusters.txt","r",encoding="utf-8")
data=f.readlines()
f.close()
test_file=open('app_clusters.csv', 'w',encoding='utf-8')
writer= csv.writer(test_file)
for line in data:
    line=list(line.split("  "))
    writer.writerow(line)
test_file.close()