from sklearn.svm import OneClassSVM
import csv
import numpy as np
my_list=['CONTACTS', 'IDENTIFIERS', 'SEARCH_HISTORY', 'OTHER_PURPOSES', 'HEALTH_AND_FITNESS', 'BROWSING_HISTORY', 'FINANCIAL_INFO', 'THIRD_PARTY_ADVERTISING', 'CONTACT_INFO', 'DEVELOPERS_ADVERTISING', 'PURCHASES', 'OTHER', 'PRODUCT_PERSONALIZATION', 'DATA_LINKED_TO_YOU', 'USER_CONTENT', 'APP_FUNCTIONALITY', 'DATA_USED_TO_TRACK_YOU', 'DIAGNOSTICS', 'ANALYTICS', 'LOCATION', 'USAGE_DATA', 'DATA_NOT_LINKED_TO_YOU', 'SENSITIVE_INFO']
print(type(my_list))
print(len(my_list))
f=open("label+category_new.csv","r",encoding="utf-8")
data=csv.reader(f)
total_lst=[]
for line in data:
    if not line:
        continue
    if int(line[4])!=0:
        continue
    ori_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if line[5]=='None':
        total_lst.append(ori_lst)
    else:
        str = line[5]
        lst = str.split("', '")
        for j in lst:
            if j.find("identifier") != -1:
                substr = j[j.find("identifier") + 14:]
                print(substr)
                point=my_list.index(substr)
                ori_lst[point]=1
        total_lst.append(ori_lst)
f.close()
print(total_lst)
X=np.array(total_lst)
clf=OneClassSVM(gamma='auto').fit(X)
outcome=clf.predict(X).tolist()
print(outcome)