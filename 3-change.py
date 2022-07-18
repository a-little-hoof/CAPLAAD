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
f=open('data_with_language.csv', 'r',encoding='utf-8')
reader = csv.reader(f)
test_file=open('for_mallet.csv', 'w',encoding='utf-8')
writer= csv.writer(test_file)

for i in reader:
    str=""
    test_list=i
    if i[3] == 'en':
        words=i[2]
        words = words.replace("\\n", ' ')
        pun=string.punctuation
        pun+="1234567890–‘’”“【】•®"
        for punc in pun:
            words = words.replace(punc,' ')
        words=words.split(" ")  # Split over space
        for word in words:
            word=word.lower()
            if word not in sw and word!="":
                if(word.find("http")!=-1):
                    continue
                str=str+word+" "
        print(i[0])
        test_list.append(str)
        writer.writerow(test_list)
        id = test_list[0]
        location = "E:\github\python\data_for_mallet_2\\" + id + ".txt"
        fi = open(location, 'w', encoding='utf-8')
        fi.write(str)
        fi.close()
f.close()
test_file.close()
