import os

from pprint import pprint
from gensim.models.wrappers import LdaMallet
os.environ.update({'MALLET_HOME':r'E:/Mallet-202108-bin/Mallet-202108/'})
mallet_path=r'E:/Mallet-202108-bin/Mallet-202108/bin/mallet'

ldamallet = gensim.models.wrappers.LdaMallet(
   mallet_path, corpus=corpus, num_topics=30, id2word=id2word
)
pprint(ldamallet.show_topics(formatted=False))