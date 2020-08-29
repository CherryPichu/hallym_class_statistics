import pandas as pd

data = pd.read_csv('데이터 정리 수정.csv', encoding='cp949')
d = []
count =0
name = '의예과'
for i in data.대학 :
    if not name in i :
        d.append(count)
        data = data.drop(count)
    count += 1


print(len(data))
trf_video = 0
for i in data.iloc[:,7] :
    if '[전환(동영상)]' in i :
        trf_video += 1

print('전환(동영상) : ' ,trf_video)

offline = 0
for i in data.iloc[:,7] :
    if '[오프라인]' in i :
        offline += 1
print('[오프라인] : ',offline)




Mixed_operation = 0
for i in data.iloc[:,7] :
    if '[전환(혼합)]' in i :
        Mixed_operation  += 1
print('[전환(혼합)] : ',Mixed_operation)

trf_class = 0
for i in data.iloc[:,7] :
    if '[전환(화상)]' in i :
        trf_class += 1
print('전환(화상) : ', trf_class)

video_con  = 0
for i in data.iloc[:,7] :
    if '[동영상 콘텐츠]' in i :
        video_con += 1
print('동영상 콘텐츠 : ',video_con)


BFlearn = 0
for i in data.iloc[:,7] :
    if '[플립러닝]' in i :
        BFlearn += 1
    if '[블렌디드]' in i :
        BFlearn += 1
print('플립러닝&블렌디드 : ',BFlearn)

real_time_class = 0
for i in data.iloc[:,7] :
    if '[실시간 화상강의]' in i :
        real_time_class += 1
print('실시간 화상강의 : ', real_time_class)


etc_class = len(data) - (real_time_class + trf_class + trf_video + BFlearn + video_con + offline + Mixed_operation)
print("기타 : " , etc_class)
import math

trf_video = round(trf_video / len(data) * 100 , 1)
trf_class = round(trf_class / len(data) * 100 , 1)
BFlearn  = round(BFlearn / len(data) * 100 , 1)
real_time_class = round(real_time_class / len(data) * 100 , 1)
video_con = round(video_con / len(data) * 100 , 1)
Mixed_operation = round(Mixed_operation / len(data) * 100 , 1)
offline = round(offline / len(data) * 100 , 1)

etc_class = 100 - (real_time_class + trf_class + trf_video + BFlearn + video_con + offline + Mixed_operation)
print(real_time_class + trf_class + trf_video + BFlearn + video_con + offline + Mixed_operation + etc_class)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'yellow', 'blue', 'red' ] # ,  'purple'
labels = ['[전환(동영상)]', '[오프라인]', '[전환(혼합)]',  '[전환(화상)]', '[동영상 콘텐츠]', '플립러닝&블렌디드', '[실시간 화상강의]'] # , '기타'
ratio = [trf_video, offline, Mixed_operation, trf_class, video_con,BFlearn, real_time_class] # , etc_class
explode = (0.0, 0.03, 0.06, 0.09, 0.12, 0.2, 0.28) # , 0.49

plt.pie(ratio,  explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('                                                                    ' + name)
plt.show()







