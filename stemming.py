import nltk
import csv
from nltk.corpus import stopwords  #下载停用词
from nltk.stem import WordNetLemmatizer
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb
import string #remove punctuation

wnl = WordNetLemmatizer()
sw=set(stopwords.words('english'))

lc_stemmer = lc.LancasterStemmer()
f=open('new_data.csv', 'r',encoding='utf-8')
reader = csv.reader(f)
test_file=open('stemming.csv', 'w',encoding='utf-8')
writer= csv.writer(test_file)

for i in reader:
    list=[]
    test_list=i
    if i[3] == 'en':
        words=i[2]
        words = words.replace("\\n", ' ')
        pun=string.punctuation
        pun+="1234567890–‘’”“【】·"
        for punc in pun:
            words = words.replace(punc,' ')
        words=words.split(" ")  # Split over space
        for word in words:
            word=word.lower()
            if word not in sw and word!="":
                if(word.find("http")!=-1):
                    continue
                lc_stem = lc_stemmer.stem(word)
                list.append(lc_stem)
        print(i[0])
        test_list.append(list)
        writer.writerow(test_list)
f.close()
test_file.close()
