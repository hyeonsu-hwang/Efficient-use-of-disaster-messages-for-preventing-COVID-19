import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("C:/Users/wel27/OneDrive/바탕 화면/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)
daegu = data['여행지'] == '대구광역시'
go_daegu = data[daegu]
go_daegu.set_index('거주지역', inplace=True)
home_seoul = go_daegu.loc['서울특별시']
home_seoul = home_seoul.drop(['sido_cd','여행지','home_sido_cd','age_cd','sex_cd'], axis=1)




home_seoul.reset_index()

dt = home_seoul['dt']
dt
dt.reset_index()
dt = dt.drop(['거주지역'])
dt

dt
home_seoul.set_index('dt', inplace=True)
plt.plot(home_seoul.index, home_seoul['추정 여행객수(명)'])

plt.plot(home_seoul['dt'], home_seoul['추정 여행객수(명)'])

home_seoul.head()


home_seoul

from matplotlib import font_manager, rc
font_path = "C:/Users/황현수/Desktop/2020 2학기 기말/ufs카드/본문소스코드/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 한글 폰트 오류 해결
import pandas as pd
import matplotlib.pyplot as plt
plt.plot(home_seoul)

plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(home_seoul['dt'], home_seoul['추정 여행객수(명)'])
plt.title('서울 -> 대구 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 대구'], loc='best')
plt.show()

plt.plot(home_seoul['추정 여행객수(명)'])







#############################################################다시#######################################
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("C:/Users/wel27/OneDrive/바탕 화면/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)
daegu = data['여행지'] == '대구광역시'
go_daegu = data[daegu]
go_daegu.set_index('거주지역', inplace=True)
home_seoul = go_daegu.loc['서울특별시']
home_seoul.reset_index()
home_seoul.set_index('dt', inplace=True)
home_seoul
plt.plot(home_seoul.index, home_seoul['추정 여행객수(명)'])
plt.plot(home_seoul['추정 여행객수(명)'])


real = home_seoul.reset_index()
plt.plot(real.index, real['추정 여행객수(명)'])
plt.plot(real['dt'])
ax.set(ylim=(0,200000))
type(real['추정 여행객수(명)'])
class(real['추정 여행객수(명)'])
str(real)
print(type(real['추정 여행객수(명)']))
real['추정 여행객수(명)']=int(real['추정 여행객수(명)'])
print(type(real['추정 여행객수(명)']))

x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 

############################################ 재수정 ##########################################3

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("C:/Users/wel27/OneDrive/바탕 화면/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)
daegu = data['여행지'] == '대구광역시'
go_daegu = data[daegu]
go_daegu.set_index('거주지역', inplace=True)
home_seoul = go_daegu.loc['서울특별시']
home_seoul=home_seoul.reset_index()
type(home_seoul['추정 여행객수(명)']) #type series형
plt.plot(home_seoul['추정 여행객수(명)'])

re=home_seoul
re['추정 여행객수(명)']=pd.to_numeric(re['추정 여행객수(명)']) #자료형을 숫자형(nemeric)으로 변경
type(re['추정 여행객수(명)']) #type series형, 데이터 type은 변경 전과 동일

plt.plot(re['추정 여행객수(명)'])
re['추정 여행객수(명)'].plot()


x = [1,2,3];y = [2,4,1] 
plt.plot(x, y) 

x=['1','2','3'];y=['2','4','1']
plt.plot(x, y) 






################################## 재수정2 #################################################

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)
daegu = data['여행지'] == '대구광역시'
go_daegu = data[daegu]
go_daegu.set_index('거주지역', inplace=True)
home_seoul = go_daegu.loc['서울특별시']
home_seoul.set_index('dt', inplace=True)
re=home_seoul
re['추정 여행객수(명)']=pd.to_numeric(re['추정 여행객수(명)'])
re = re.drop(['sido_cd','여행지','home_sido_cd','age_cd','sex_cd'], axis=1)
plt.plot(re.index, re['추정 여행객수(명)'])


# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#표꾸미기
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re.index, re['추정 여행객수(명)'])
plt.title('서울 -> 대구 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 대구'], loc='best')
plt.show()

plt.plot(home_seoul['추정 여행객수(명)'])


####################################### 중간발표용 코드 #########################################

#데이터 추출 [서울(거주지) -> 대구(여행지)]
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("C:/Users/we`l27/OneDrive/바탕 화면/2)여행지수_20200921.csv")
data = raw_data
daegu = data['sido_nm'] == '대구광역시'
go_daegu = data[daegu]
go_daegu.set_index('home_sido_nm', inplace=True)
home_seoul = go_daegu.loc['서울특별시']
home_seoul = home_seoul.drop(['sido_cd','home_sido_cd','age_cd','sex_cd'], axis=1)



home_seoul.set_index('dt', inplace=True)

#자료형 문자형
home_seoul.set_index('dt', inplace=True)
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(home_seoul.index, home_seoul['cnt_aprx'])
plt.title('서울 -> 대구 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 대구'], loc='best')
plt.show()

#자료형 숫자형 
re=home_seoul
re['cnt_aprx)']=pd.to_numeric(re['cnt_aprx'])

plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re.index, re['cnt_aprx)'])
plt.title('서울 -> 대구 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 대구'], loc='best')
plt.show()





###################################################################################################3
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(home_seoul.index, home_seoul['cnt_aprx'])
plt.title('서울 -> 대구 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 대구'], loc='best')
plt.show()


plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re.index, re['추정 여행객수(명)'])
plt.title('서울 -> 대구 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 대구'], loc='best')
plt.show()


plt.plot(re.index, re['cnt_aprx'])
re['추정 여행객수(명)']=pd.to_numeric(re['추정 여행객수(명)'])


plt.plot(home_seoul['추정 여행객수(명)'])
re=home_seoul
re['추정 여행객수(명)']=pd.to_numeric(re['추정 여행객수(명)'])
re = re.drop(['sido_cd','여행지','home_sido_cd','age_cd','sex_cd'], axis=1)
plt.plot(re.index, re['cnt_aprx'])

#################################################################################################
#################################################################################################




############################################################기말발표용 코드(연습)#############################################

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)

###### 서울 -> 제주 #########
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('거주지역', inplace=True)
home_seoul = go_Jeiu.loc['서울특별시']
home_seoul.set_index('dt', inplace=True)
re_home_seoul=home_seoul
re_home_seoul['추정 여행객수(명)']=pd.to_numeric(re_home_seoul['추정 여행객수(명)'])
plt.plot(re_home_seoul.index, re_home_seoul['추정 여행객수(명)'])


# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/2020 2학년2학기/컴이자2/본문소스코드/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#표꾸미기
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re_home_seoul.index, re_home_seoul['추정 여행객수(명)'])
plt.title('서울 -> 제주 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['서울 -> 제주'], loc='best')
plt.show()



###### 부산 -> 제주 #########
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('거주지역', inplace=True)
home_Busan = go_Jeiu.loc['부산광역시']
home_Busan.set_index('dt', inplace=True)
re_home_Busan=home_Busan
re_home_Busan['추정 여행객수(명)']=pd.to_numeric(re_home_Busan['추정 여행객수(명)'])
plt.plot(re_home_Busan.index, re_home_Busan['추정 여행객수(명)'])


# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/2020 2학년2학기/컴이자2/본문소스코드/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#표꾸미기
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re_home_Busan.index, re_home_Busan['추정 여행객수(명)'])
plt.title('부산 -> 제주 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['부산 -> 제주'], loc='best')
plt.show()



###### 대구 -> 제주 #########
home_Daegu = go_Jeiu.loc['대구광역시']
home_Daegu.set_index('dt', inplace=True)
re_home_Daegu=home_Daegu
re_home_Daegu['추정 여행객수(명)']=pd.to_numeric(re_home_Daegu['추정 여행객수(명)'])


#표꾸미기
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re_home_Daegu.index, re_home_Daegu['추정 여행객수(명)'])
plt.title('대구 -> 제주 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['대구 -> 제주'], loc='best')
plt.show()


###### 인천 -> 제주 #########
home_Incheon = go_Jeiu.loc['인천광역시']
home_Incheon.set_index('dt', inplace=True)
re_home_Incheon=home_Incheon
re_home_Incheon['추정 여행객수(명)']=pd.to_numeric(re_home_Incheon['추정 여행객수(명)'])


#표꾸미기
plt.figure(figsize=(14, 5))
plt.xticks(rotation='vertical')
plt.plot(re_home_Incheon.index, re_home_Incheon['추정 여행객수(명)'])
plt.title('인천 -> 제주 여행')
plt.xlabel('날짜')
plt.ylabel('여행객수')
plt.legend(labels=['인천 -> 제주'], loc='best')
plt.show()

#######################################################################################################################################
#######################################################################################################################################


# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

############# 제주도로 여행가는 지역별 그래프 !!! ##################################################

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)

## 여행지 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('거주지역', inplace=True)

## 서울 -> 제주 
home_seoul = go_Jeiu.loc['서울특별시']
home_seoul.set_index('dt', inplace=True)
re_home_seoul=home_seoul
re_home_seoul['추정 여행객수(명)']=pd.to_numeric(re_home_seoul['추정 여행객수(명)'])

## 경기 -> 제주
home_gyeonggi = go_Jeiu.loc['경기도']
home_gyeonggi.set_index('dt', inplace=True)
re_home_gyeonggi=home_gyeonggi
re_home_gyeonggi['추정 여행객수(명)']=pd.to_numeric(re_home_gyeonggi['추정 여행객수(명)'])

## 부산 -> 제주 
home_Busan = go_Jeiu.loc['부산광역시']
home_Busan.set_index('dt', inplace=True)
re_home_Busan=home_Busan
re_home_Busan['추정 여행객수(명)']=pd.to_numeric(re_home_Busan['추정 여행객수(명)'])

## 대구 -> 제주 
home_Daegu = go_Jeiu.loc['대구광역시']
home_Daegu.set_index('dt', inplace=True)
re_home_Daegu=home_Daegu
re_home_Daegu['추정 여행객수(명)']=pd.to_numeric(re_home_Daegu['추정 여행객수(명)'])


## 인천 -> 제주 
home_Incheon = go_Jeiu.loc['인천광역시']
home_Incheon.set_index('dt', inplace=True)
re_home_Incheon=home_Incheon
re_home_Incheon['추정 여행객수(명)']=pd.to_numeric(re_home_Incheon['추정 여행객수(명)'])

# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_home_gyeonggi.index, re_home_gyeonggi['추정 여행객수(명)'], marker='o', markerfacecolor='black', 
        markersize=10, color='black', linewidth=2, label='경기')
ax.plot(re_home_seoul.index, re_home_seoul['추정 여행객수(명)'], marker='o', markerfacecolor='green', 
        markersize=10, color='olive', linewidth=2, label='서울')
ax.plot(re_home_Busan.index, re_home_Busan['추정 여행객수(명)'], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='부산')
ax.plot(re_home_Daegu.index, re_home_Daegu['추정 여행객수(명)'], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='대구')
ax.plot(re_home_Incheon.index, re_home_Incheon['추정 여행객수(명)'], marker='o', markerfacecolor='orange', 
        markersize=10, color= 'yellow', linewidth=2, label='인천')



# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(지역별)경기,서울,부산,대구,인천 -> 제주', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(re_home_seoul.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력



###############################################################
############# 제주도로 여행가는 성별 그래프 !!! ##################################################

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)', }, inplace=True)

## 남성 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('sex_cd', inplace=True)
male = go_Jeiu.loc['1']
male.set_index('dt', inplace=True)
re_male=male
re_male['추정 여행객수(명)']=pd.to_numeric(re_male['추정 여행객수(명)'])

## 여성 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('sex_cd', inplace=True)
female = go_Jeiu.loc['2']
female.set_index('dt', inplace=True)
re_female=female
re_female['추정 여행객수(명)']=pd.to_numeric(re_female['추정 여행객수(명)'])


# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_male.index, re_male['추정 여행객수(명)'], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='남성')
ax.plot(re_female.index, re_female['추정 여행객수(명)'], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='여성')

# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(성별)남성,여성 -> 제주', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(re_male.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력




###############################################################
############# 제주도로 여행가는 성별 그래프 !!! ##################################################

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)', }, inplace=True)

## 남성 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('sex_cd', inplace=True)
male = go_Jeiu.loc['1']
male.set_index('dt', inplace=True)
re_male=male
re_male['추정 여행객수(명)']=pd.to_numeric(re_male['추정 여행객수(명)'])

## 여성 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('sex_cd', inplace=True)
female = go_Jeiu.loc['2']
female.set_index('dt', inplace=True)
re_female=female
re_female['추정 여행객수(명)']=pd.to_numeric(re_female['추정 여행객수(명)'])


# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_male.index, re_male['추정 여행객수(명)'], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='남성')
ax.plot(re_female.index, re_female['추정 여행객수(명)'], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='여성')

# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(성별)남성,여성 -> 제주', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(re_male.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력




###############################################################
############# 제주도로 여행가는 연령별 그래프 !!! ##################################################

import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)', }, inplace=True)

## 0대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_0 = go_Jeiu.loc['0']
age_0.set_index('dt', inplace=True)
re_age_0=age_0
re_age_0['추정 여행객수(명)']=pd.to_numeric(re_age_0['추정 여행객수(명)'])

## 10대 -> 제주
age_10 = go_Jeiu.loc['10']
age_10.set_index('dt', inplace=True)
re_age_10=age_10
re_age_10['추정 여행객수(명)']=pd.to_numeric(re_age_10['추정 여행객수(명)'])

## 20대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_20 = go_Jeiu.loc['20']
age_20.set_index('dt', inplace=True)
re_age_20=age_20
re_age_20['추정 여행객수(명)']=pd.to_numeric(re_age_20['추정 여행객수(명)'])

## 30대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_30 = go_Jeiu.loc['30']
age_30.set_index('dt', inplace=True)
re_age_30=age_30
re_age_30['추정 여행객수(명)']=pd.to_numeric(re_age_30['추정 여행객수(명)'])

## 40대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_40 = go_Jeiu.loc['40']
age_40.set_index('dt', inplace=True)
re_age_40=age_40
re_age_40['추정 여행객수(명)']=pd.to_numeric(re_age_40['추정 여행객수(명)'])

## 50대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_50 = go_Jeiu.loc['50']
age_50.set_index('dt', inplace=True)
re_age_50=age_50
re_age_50['추정 여행객수(명)']=pd.to_numeric(re_age_50['추정 여행객수(명)'])

## 60대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_60 = go_Jeiu.loc['60']
age_60.set_index('dt', inplace=True)
re_age_60=age_60
re_age_60['추정 여행객수(명)']=pd.to_numeric(re_age_60['추정 여행객수(명)'])

## 70대 -> 제주
Jeju = data['여행지'] == '제주특별자치도'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('age_cd', inplace=True)
age_70 = go_Jeiu.loc['70']
age_70.set_index('dt', inplace=True)
re_age_70=age_70
re_age_70['추정 여행객수(명)']=pd.to_numeric(re_age_70['추정 여행객수(명)'])


# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)


# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_age_0.index, re_age_0['추정 여행객수(명)'], marker='o', markerfacecolor='pink', 
        markersize=10, color='pink', linewidth=2, label='0대')
ax.plot(re_age_10.index, re_age_10['추정 여행객수(명)'], marker='o', markerfacecolor='bisque', 
        markersize=10, color='bisque', linewidth=2, label='10대')
ax.plot(re_age_20.index, re_age_20['추정 여행객수(명)'], marker='o', markerfacecolor='orangered', 
        markersize=10, color='orangered', linewidth=2, label='20대')
ax.plot(re_age_30.index, re_age_30['추정 여행객수(명)'], marker='o', markerfacecolor='black', 
        markersize=10, color= 'black', linewidth=2, label='30대')
ax.plot(re_age_40.index, re_age_40['추정 여행객수(명)'], marker='o', markerfacecolor='mediumvioletred', 
        markersize=10, color= 'mediumvioletred', linewidth=2, label='40대')
ax.plot(re_age_50.index, re_age_50['추정 여행객수(명)'], marker='o', markerfacecolor='steelblue', 
        markersize=10, color= 'steelblue', linewidth=2, label='50대')
ax.plot(re_age_60.index, re_age_60['추정 여행객수(명)'], marker='o', markerfacecolor='gold', 
        markersize=10, color= 'gold', linewidth=2, label='60대')
ax.plot(re_age_70.index, re_age_70['추정 여행객수(명)'], marker='o', markerfacecolor='forestgreen', 
        markersize=10, color= 'forestgreen', linewidth=2, label='70대')


# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(연령별) 0대,10대,20대 ~ 70대이상 -> 제주', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(re_male.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력








################################ 제주도 정규화 ################################
# 2019년 시도별 인구
# 서울 : 9662000(명)
# 부산 : 3373000(명)
# 대구 : 2432000(명)
# 인천 : 2944000(명)
# 울산 : 1147000(명)
# 제주 : 660000(명)


raw_travel_rate = {'전체인구(명)' : [13238000,9662000,3373000,2944000,2432000], 
               '추정여행객수(명)':[114258,125548,27175,21271,22516]}
travel_rate = pd.DataFrame(raw_travel_rate, index=('경기','서울','부산','인천','대구'))

# 정규화 함수 정의
def nomal(a,b):
    return b/a

travel_rate['rate'] = travel_rate.apply(lambda x : nomal(x['전체인구(명)'], x['추정여행객수(명)']), axis=1) 

##### 2축 그래프 그리기 ##############
ax1 = travel_rate['추정여행객수(명)'].plot(kind='bar', figsize=(8,4), width=0.5, stacked=True)
ax2 = ax1.twinx()
ax2.plot(travel_rate.index, travel_rate.rate, ls='--', marker='o',markersize=7,
         color='blue', label= 'rate')

ax1.set_ylim(0,150000)
ax2.set_ylim(0,0.05)

ax1.set_xlabel('지역', size=15)
ax1.set_ylabel('추정여행객수(명)')
ax2.set_ylabel('전체인구 대비 여행객수(비율)')

plt.title('지역별 8/10 ~8/16 기간 제주도로 추정여행객수(명)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()


################### 전체인구 대비 여행객수 그래프 8/10 ~ 8/16 ######################
raw_travel_rate = {'전체인구(명)' : [13238000,9662000,3373000,2944000,2432000], 
               '추정여행객수(명)':[114258,125548,27175,21271,22516]}
travel_rate = pd.DataFrame(raw_travel_rate, index=('경기','서울','부산','인천','대구'))

# 정규화 함수 정의
def nomal(a,b):
    return b/a

travel_rate['rate'] = travel_rate.apply(lambda x : nomal(x['전체인구(명)'], x['추정여행객수(명)']), axis=1) 

##### 2축 그래프 그리기 ##############
ax1 = travel_rate['추정여행객수(명)'].plot(kind='bar', figsize=(8,4), width=0.5, stacked=True)
ax2 = ax1.twinx()
ax2.plot(travel_rate.index, travel_rate.rate, ls='--', marker='o',markersize=7,
         color='blue', label= 'rate')

ax1.set_ylim(0,150000)
ax2.set_ylim(0,0.05)

ax1.set_xlabel('지역', size=15)
ax1.set_ylabel('추정여행객수(명)')
ax2.set_ylabel('전체인구 대비 여행객수(비율)')

plt.title('지역별 8/10 ~8/16 기간 제주도로 추정여행객수(명)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()





import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['20대', '50대']

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()


############## 컴이자 울산! ###################### (서울,대구,부산,인천 + 경기도)
# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)'}, inplace=True)

## 여행지 울산 
ulsan = data['여행지'] == '울산광역시'
go_ulsan = data[ulsan]
go_ulsan.set_index('거주지역', inplace=True)

## 서울 -> 울산 
home_seoul = go_ulsan.loc['서울특별시']
home_seoul.set_index('dt', inplace=True)
re_home_seoul=home_seoul
re_home_seoul['추정 여행객수(명)']=pd.to_numeric(re_home_seoul['추정 여행객수(명)'])

## 부산 -> 울산
home_Busan = go_ulsan.loc['부산광역시']
home_Busan.set_index('dt', inplace=True)
re_home_Busan=home_Busan
re_home_Busan['추정 여행객수(명)']=pd.to_numeric(re_home_Busan['추정 여행객수(명)'])

## 대구 -> 울산 
home_Daegu = go_ulsan.loc['대구광역시']
home_Daegu.set_index('dt', inplace=True)
re_home_Daegu=home_Daegu
re_home_Daegu['추정 여행객수(명)']=pd.to_numeric(re_home_Daegu['추정 여행객수(명)'])

## 인천 -> 울산 
home_Incheon = go_ulsan.loc['인천광역시']
home_Incheon.set_index('dt', inplace=True)
re_home_Incheon=home_Incheon
re_home_Incheon['추정 여행객수(명)']=pd.to_numeric(re_home_Incheon['추정 여행객수(명)'])

## 경기도 -> 울산 
home_gyeonggi = go_ulsan.loc['경기도']
home_gyeonggi.set_index('dt', inplace=True)
re_home_gyeonggi=home_gyeonggi
re_home_gyeonggi['추정 여행객수(명)']=pd.to_numeric(re_home_gyeonggi['추정 여행객수(명)'])


# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_home_gyeonggi.index, re_home_gyeonggi['추정 여행객수(명)'], marker='o', markerfacecolor='black', 
        markersize=10, color= 'black', linewidth=2, label='경기')
ax.plot(re_home_Daegu.index, re_home_Daegu['추정 여행객수(명)'], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='대구')
ax.plot(re_home_seoul.index, re_home_seoul['추정 여행객수(명)'], marker='o', markerfacecolor='green', 
        markersize=10, color='olive', linewidth=2, label='서울')
ax.plot(re_home_Busan.index, re_home_Busan['추정 여행객수(명)'], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='부산')
ax.plot(re_home_Incheon.index, re_home_Incheon['추정 여행객수(명)'], marker='o', markerfacecolor='orange', 
        markersize=10, color= 'yellow', linewidth=2, label='인천')

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(지역별)서울,경기,부산,대구,인천 -> 울산', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(re_home_seoul.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력



######################################## 정규화 ##########################################

# 여행,단기출장 이동수치만 보면 경기,서울,대구 비슷하다 하지만 비율은 다를것 정규화를 통해 쉽게 수치화해서 알아볼수 있다.
# 정규화 : 데이터의 상대적인 크기 차이를 제거하는것, 각 열(변수)에 속하는 데이터값을 동일한 크기 기준으로 나눈 비율로 나타내는것
# 해당 열의 최대값(의 절대값)으로 나누는 방법, 
# 여기서 최대값은 각 시도별 전체인구가 최대값이 되고 ,
# 각 시도별 이동인구에서 그지역 최대값(전체인구)을 나누면 모든 데이터를 0~1 값으로 상대적인 크기차이를 제거하고 비교가능하다


# 2019년 시도별 인구
# 서울 : 9662000(명)
# 부산 : 3373000(명)
# 대구 : 2432000(명)
# 인천 : 2944000(명)
# 울산 : 1147000(명)
# 제주 : 660000(명)


################################
# 2019년 시도별 인구
# 경기 : 13238000(명)
# 서울 : 9662000(명)
# 부산 : 3373000(명)
# 인천 : 2944000(명)
# 대구 : 2432000(명)
###############################



################### 전체인구 대비 여행객수 그래프 8/10 ~ 8/16 ######################

raw_travel_rate = {'전체인구(명)' : [13238000,9662000,3373000,2944000,2432000], 
               '추정여행객수(명)':[36801,30114,6734,5628,32436]}
travel_rate = pd.DataFrame(raw_travel_rate, index=('경기','서울','부산','인천','대구'))

# 정규화 함수 정의
def nomal(a,b):
    return b/a

travel_rate['rate'] = travel_rate.apply(lambda x : nomal(x['전체인구(명)'], x['추정여행객수(명)']), axis=1) 

##### 2축 그래프 그리기 ##############
ax1 = travel_rate['추정여행객수(명)'].plot(kind='bar', figsize=(8,4), width=0.5, stacked=True)
ax2 = ax1.twinx()
ax2.plot(travel_rate.index, travel_rate.rate, ls='--', marker='o',markersize=7,
         color='blue', label= 'rate')

ax1.set_ylim(0,50000)
ax2.set_ylim(0,0.05)

ax1.set_xlabel('지역', size=15)
ax1.set_ylabel('추정여행객수(명)')
ax2.set_ylabel('전체인구 대비 여행객수(비율)')

plt.title('지역별 8/10 ~8/16 기간 울산으로 추정여행객수(명)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# 스타일 테마 설정
sns.set_style('whitegrid')


################### 울산 여행 연령별 그래프 ###########################################
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)', }, inplace=True)

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "D:/1/part4/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


## 0대 -> 울산
ulsan = data['여행지'] == '울산광역시'
go_ulsan = data[ulsan]
go_ulsan.set_index('age_cd', inplace=True)
age_0 = go_ulsan.loc['0']
age_0.set_index('dt', inplace=True)
re_age_0=age_0
re_age_0['추정 여행객수(명)']=pd.to_numeric(re_age_0['추정 여행객수(명)'])


## 10대 -> 울산
age_10 = go_ulsan.loc['10']
age_10.set_index('dt', inplace=True)
re_age_10=age_10
re_age_10['추정 여행객수(명)']=pd.to_numeric(re_age_10['추정 여행객수(명)'])

## 20대 -> 울산
age_20 = go_ulsan.loc['20']
age_20.set_index('dt', inplace=True)
re_age_20=age_20
re_age_20['추정 여행객수(명)']=pd.to_numeric(re_age_20['추정 여행객수(명)'])

## 30대 -> 울산
age_30 = go_ulsan.loc['30']
age_30.set_index('dt', inplace=True)
re_age_30=age_30
re_age_30['추정 여행객수(명)']=pd.to_numeric(re_age_30['추정 여행객수(명)'])

## 40대 -> 울산
age_40 = go_ulsan.loc['40']
age_40.set_index('dt', inplace=True)
re_age_40=age_40
re_age_40['추정 여행객수(명)']=pd.to_numeric(re_age_40['추정 여행객수(명)'])

## 50대 -> 울산
age_50 = go_ulsan.loc['50']
age_50.set_index('dt', inplace=True)
re_age_50=age_50
re_age_50['추정 여행객수(명)']=pd.to_numeric(re_age_50['추정 여행객수(명)'])

## 60대 -> 울산
age_60 = go_ulsan.loc['60']
age_60.set_index('dt', inplace=True)
re_age_60=age_60
re_age_60['추정 여행객수(명)']=pd.to_numeric(re_age_60['추정 여행객수(명)'])

## 70대 -> 울산
age_70 = go_ulsan.loc['70']
age_70.set_index('dt', inplace=True)
re_age_70=age_70
re_age_70['추정 여행객수(명)']=pd.to_numeric(re_age_70['추정 여행객수(명)'])


# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)


# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_age_0.index, re_age_0['추정 여행객수(명)'], marker='o', markerfacecolor='pink', 
        markersize=10, color='pink', linewidth=2, label='0대')
ax.plot(re_age_10.index, re_age_10['추정 여행객수(명)'], marker='o', markerfacecolor='bisque', 
        markersize=10, color='bisque', linewidth=2, label='10대')
ax.plot(re_age_20.index, re_age_20['추정 여행객수(명)'], marker='o', markerfacecolor='orangered', 
        markersize=10, color='orangered', linewidth=2, label='20대')
ax.plot(re_age_30.index, re_age_30['추정 여행객수(명)'], marker='o', markerfacecolor='black', 
        markersize=10, color= 'black', linewidth=2, label='30대')
ax.plot(re_age_40.index, re_age_40['추정 여행객수(명)'], marker='o', markerfacecolor='mediumvioletred', 
        markersize=10, color= 'mediumvioletred', linewidth=2, label='40대')
ax.plot(re_age_50.index, re_age_50['추정 여행객수(명)'], marker='o', markerfacecolor='steelblue', 
        markersize=10, color= 'steelblue', linewidth=2, label='50대')
ax.plot(re_age_60.index, re_age_60['추정 여행객수(명)'], marker='o', markerfacecolor='gold', 
        markersize=10, color= 'gold', linewidth=2, label='60대')
ax.plot(re_age_70.index, re_age_70['추정 여행객수(명)'], marker='o', markerfacecolor='forestgreen', 
        markersize=10, color= 'forestgreen', linewidth=2, label='70대')


# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(연령별) 0대,10대,20대 ~ 70대이상 -> 울산', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(age_0.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력




############################### 울산 성별 그래프 ##########################################
import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("D:/1/2)여행지수_20200921.csv")
data = raw_data
data.rename(columns={'sido_nm':'여행지', 'home_sido_nm':'거주지역', 'cnt_aprx':'추정 여행객수(명)', }, inplace=True)

## 남성 -> 울산
Jeju = data['여행지'] == '울산광역시'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('sex_cd', inplace=True)
male = go_Jeiu.loc['1']
male.set_index('dt', inplace=True)
re_male=male
re_male['추정 여행객수(명)']=pd.to_numeric(re_male['추정 여행객수(명)'])

## 여성 -> 울산
Jeju = data['여행지'] == '울산광역시'
go_Jeiu = data[Jeju]
go_Jeiu.set_index('sex_cd', inplace=True)
female = go_Jeiu.loc['2']
female.set_index('dt', inplace=True)
re_female=female
re_female['추정 여행객수(명)']=pd.to_numeric(re_female['추정 여행객수(명)'])


# 스타일 서식 지정
plt.style.use('ggplot') 

# 그래프 객체 생성 (figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20, 5))   
ax = fig.add_subplot(1, 1, 1)

# axe 객체에 plot 함수로 그래프 출력
ax.plot(re_male.index, re_male['추정 여행객수(명)'], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='남성')
ax.plot(re_female.index, re_female['추정 여행객수(명)'], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='여성')

# 범례 표시
ax.legend(loc='best')

# 차트 제목 추가
ax.set_title('(성별)남성,여성 -> 울산', size=20)

# 축이름 추가
ax.set_xlabel('날짜', size=12)
ax.set_ylabel('여행객수', size = 12)

# 축 눈금 라벨 지정 및 60도 회전
ax.set_xticklabels(re_male.index, rotation=60)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)

plt.show()  # 변경사항 저장하고 그래프 출력























































