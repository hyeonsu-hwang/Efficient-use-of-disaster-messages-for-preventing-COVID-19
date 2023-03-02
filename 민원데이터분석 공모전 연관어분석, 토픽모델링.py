## 민원데이터 형태소 분석(엑셀 파일로 저장)
from konlpy.tag import Okt
okt = Okt()
okt.pos('konlpy의 설치를 성공적으로 마쳤습니다.')

from konlpy.tag import Mecab
mecab = Mecab()
mecab.pos('Mecab도 설치 완료했습니다.')

import os
print(os.getcwd())
os.chdir('D:/파이썬텍스트분석')
import pandas as pd
df = pd.read_excel('국민권익위원회 경진 대회 데이터(목적이외 사용시 관련 법에 의해 처벌 받을수 있음).xlsx')

import pandas as pd
import numpy as np
import re
import glob
import sys
from math import log
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Mecab

#실행시간 측정을 위한 모듈
import time
import datetime
start=time.time()

#분리된 민원데이터 2개씩 병합 후 그 병합된것들 다시 병합하여 full_data로 내보냄
#읽어들일 파일 위치 지정 & mecab

#엑셀 읽기
df = pd.read_excel('국민권익위원회 경진 대회 데이터(목적이외 사용시 관련 법에 의해 처벌 받을수 있음).xlsx')

#필요한 컬럼만 뽑기
df_proc = df.loc[:,'제목']

def get_nouns(text):
    nouns = list() # 추가
    nouns_app = nouns.append # 추가
    if len(text) > 0:
        pos = mecab.pos(text)
        for keyword, type in pos:
            if (type in filter_pos
                and len(keyword) >= word_len
                and bool(reg.search(keyword)) == False
                and keyword.upper() not in stopword_upper):
                nouns_app(keyword)
                #print(text, "->", nouns) #
    df_nouns.loc[len(df_nouns)] = {'텍스트' : text, '명사목록' : [" ".join(nouns)]} # 추가
    print('확인')
    return nouns

filter_pos = ['NNG', 'NNP', 'SL'] # 일반명사, 고유명사, 영어 
word_len = 2 # 키워드 2글자 이상
reg = re.compile('[^a-zA-Z가-힣]')
stopword = list(map(str, pd.read_excel('~')['불용어'].tolist())) # 불용어 로딩
stopword_upper = list()
for i in stopword:
    stopword_upper.append(i.upper())
    

df_nouns = pd.DataFrame(columns = ['텍스트', '명사목록'])
del[[df_nouns]]
df_nouns = pd.DataFrame(columns = ['텍스트', '명사목록']) # 추가

cv = CountVectorizer(tokenizer=get_nouns)
tdm = cv.fit_transform(df['제목'].apply(lambda x: np.str_(x)))

df_nouns.to_excel('result.xlsx', index = False)

print(df_nouns.head())
    

## 공백 제거
#단어들 데이터프레임 ->  리스트
for i in range(len(minwon['질문내용'])):
    get_nouns(minwon['질문내용'][i])

list_nouns = sum(df_nouns['명사목록'].tolist(),[])

vocab = list(set(w for doc in list_nouns for w in doc.split()))
vocab.sort()
result_tab = pd.DataFrame(index=vocab)

#vocab 내 영어 제거
for i, document in enumerate(vocab):
    document = re.sub(r'[a-zA-Z]','' , document) #영어 제거, 정규 표현식    
    vocab[i] = document
    
#영어 제거 후 공백 제거
while '' in vocab:
    vocab.remove('')
#print(vocab)    



## 연관어분석 
!pip install apriori apyori

#2차원 list에 명사만 넣기
nouns = df_nouns['명사목록']
dataset = []
for i in range(len(nouns)):
    dataset.append(nouns[i])

#단어 간 공백제거
transactions = [transaction for transaction in dataset if transaction]
print(transactions)

#조건 정해서 연관어 분석, df['length']==2는 고정, df['support']값 변환가능
from apyori import apriori

result = (list(apriori(transactions, min_support=0.01)))
df = pd.DataFrame(result)
df['length'] = df['items'].apply(lambda x:len(x))
df = df[(df['length'] == 2) &
       (df['support'] >= 0.02)].sort_values(by='support', ascending=False)

df.head(10)

import numpy as np
import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt
#network 그래프 정의
G = nx.Graph()
ar = (df['items']); G.add_edges_from(ar)

#페이지 랭크
pr = nx.pagerank(G)
nsize = np.array([v for v in pr.values()])
nsize = 2000*(nsize-min(nsize)) / (max(nsize) - min(nsize))

#레이아웃 종류들 - 레이아웃에 따라 시각화 결과들 달라짐, 오류뜨는 것도 잇드라
pos = nx.circular_layout(G)
# pos = nx.rescale_layout(G)
# pos = nx.fruchterman_reingold_layout(G)
# pos = nx.spectral_layout(G)
# pos = nx.random_layout(G)
# pos = nx.shell_layout(G)
# pos = nx.bipartite_layout(G)
# pos = nx.spring_layout(G)
# pos = nx.kamada_kawai_layout(G)

#네트워크 그래프그리기
from matplotlib import font_manager, rc
font_path = 'C:\\Users\\minseo\\Desktop\\malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.figure(figsize=(16,12)); plt.axis('off')
nx.draw_networkx(G, font_family=font_name, font_size=16,
                pos=pos, node_color=list(pr.values()), node_size=nsize,
                alpha=0.7, edge_color='.5', cmap=plt.cm.YlGn)    
    
    
    
## 토픽모델링
from konlpy.tag import Okt
okt = Okt()
from konlpy.tag import Mecab
mecab = Mecab()

import os
print(os.getcwd())
os.chdir('D:/파이썬텍스트분석')

import pandas as pd
df = pd.read_excel('국민권익위원회 경진 대회 데이터(목적이외 사용시 관련 법에 의해 처벌 받을수 있음).xlsx')

# 토픽모델링
import pandas as pd
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

# TFIDF 
def tokenizer(text):
    text = Mecab().nouns(text)
    return [word for word in text if len(word)>1]

vectorizer = TfidfVectorizer(tokenizer=tokenizer, max_df=0.90, min_df=2, max_features=5000)
tfidf = vectorizer.fit_transform(df['질문내용'])

# 토픽개수 
nmf = NMF(n_components=8, random_state=3)  
H = nmf.fit_transform(tfidf) 
W = nmf.components_ 

# 토픽별로 점수가 높은 단어 및 문서의 제목
def print_topics(W, H, words, titles, n_top_titles=5, n_top_words=10):
    for topic_idx, (doc_vec, word_vec) in enumerate(zip(H.T, W)):
        message = "\nTopic %d: " % topic_idx
        
        message += "#"+" #".join([words[i]
                     for i in word_vec.argsort()[:-n_top_words - 1:-1]])
        
        message += '\n\n'
        message += "    \n".join([titles[i]
                     for i in doc_vec.argsort()[:-n_top_titles - 1:-1]])
        print(message)
    
print_topics(W, H, vectorizer.get_feature_names(), df['제목'])

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'NanumGothic'

from matplotlib import font_manager, rc
font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


wordcloud = WordCloud(
    font_path="HANDotum.ttf",
    width = 300,
    height = 300,
    max_words=50,
    random_state=1,    
    background_color='white'
)
    
# 민원마다 토픽부여
df['topic'] = H.argmax(1)

# 토픽별 워드클라우드 8개
plt.figure(figsize=(16, 8))

for idx in range(8):    
    topic_idx = df.index[df['topic'] == idx]
    word_score = tfidf.toarray()[topic_idx].sum(0)
    d = dict(zip(vectorizer.get_feature_names(), word_score))
    
    wordcloud.generate_from_frequencies(d)
    
    plt.subplot(2,4,idx+1)
    title = df.loc[H[:, idx].argmax(), '제목']
    title = title.split()
    i = len(title) // 2
    title = ' '.join(title[:i]+["\n"]+title[i:])
    plt.title(title, fontsize=13)
    plt.imshow(wordcloud)
    plt.axis("off")

plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.show()

















