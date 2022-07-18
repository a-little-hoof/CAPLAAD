from sklearn.cluster import KMeans
import numpy as np
f=open("E:\Mallet-202108-bin\Mallet-202108\\topic_file_topic.txt","r",encoding="utf-8")
data=f.readlines()
f.close()
total_lst=[]
for line in data:
    lst=[]
    line=list(line.split("\t"))
    for i in range(2,32,1):
        line[i]=float(line[i])
        lst.append(line[i])
    total_lst.append(lst)
X=np.array(total_lst)
kmeans=KMeans(n_clusters=32,max_iter=1000,random_state=0).fit(X)
print(kmeans.labels_)
outcome=kmeans.labels_.tolist()
f=open("t.txt","w",encoding="utf-8")
f.write(str(outcome))
f.close()
