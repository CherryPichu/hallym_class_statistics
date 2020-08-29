import re
import requests as req
import time
import pandas as pd
data_path = 'data_20202.js.다운로드'
p = re.compile('[,]+')
s = re.compile('","bd"$')
list_data = list()
with open(data_path, encoding='UTF-8') as data :
    read_data = data.read()
    for i in read_data.split(',') :
        if 'cd' in i :
            list_data.append(i)
data_modfiy = []
for i in list_data :
    data_modfiy.append(i.split('"')[3])


headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
'Connection': 'keep-alive',
'Cookie': 'JSESSIONID=GWUeZwQj2aRwHrFoMZQduj2wMLI0SexZGpBk6X8U3E5dm67BVKzmPEf2VhxyKt0y.amV1c19kb21haW4vc3U0Nl9zZXJ2ZXIy; _ga=GA1.3.724150523.1587700735; WMONID=5e8lFNSatmA; _gid=GA1.3.1464955452.1598363611; NetFunnel_ID=5002%3A200%3Akey%3D21080407997E8FA0CB4173243E0DDF10227CFB9D010572C8758F9E29D1701E407B46A4C4CE74DCE497B55E4880CA4F7D5F538B7DB89D15401FEF53E992BF8E477DEDFDFE1E7CA640BE305BB5E02C9C04D180A71272AC8E230E70A71278EF9E39BC3ADDC94361E8F40C0330DDF640C1D4312C302C30%26nwait%3D0%26nnext%3D0%26tps%3D0%26ttl%3D0%26ip%3Dwait.hallym.ac.kr%26port%3D443',
'Host': 'haksa.hallym.ac.kr',
'Referer': 'https://haksa.hallym.ac.kr/hluv/core?attribute=mainSearch&token=C32DB7CD8B2A92EAFC3C824DE5200730&fake=Wed%20Aug%2026%202020%2012:45:12%20GMT+0900%20(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%ED%91%9C%EC%A4%80%EC%8B%9C)',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
book_name = []
gyosu_name = []
daesang_hakgwa = []
bigo = []
plan_time = []
isu_gbn_name = []
kang_onoff_gbn_nm = []
for i in range(len(data_modfiy)) : # len(data_modfiy)
    time.sleep(0.4)
    url = 'https://haksa.hallym.ac.kr/hluv/core?attribute=lectDetailList&params=' + data_modfiy[i] +'&menu=1&fake=Wed%20Aug%2026%202020%2000:39:03%20GMT+0900%20(대한민국%20표준시)&_search=false&nd=1598369943380&rows=1000&page=1&sidx=&sord=asc'
    a = req.get(url , headers = headers)


    for i in str(a.text).split(',') :
        if 'bigo' in i :
            book_name.append(i.split('"')[3])
        elif 'daesang_hakgwa' in i :
            gyosu_name.append(i.split('"')[3])
        elif 'gyosu_name' in i :
            daesang_hakgwa.append(i.split('"')[3])
        elif 'book_name' in i :
            bigo.append(i.split('"')[3])
        elif 'plan_time' in i:
            plan_time.append(i.split('"')[3])
        elif 'isu_gbn_name' in i:
            isu_gbn_name.append(i.split('"')[3])
        elif "kang_onoff_gbn_nm" in i :
            kang_onoff_gbn_nm.append(i.split('"')[3])

data_frame = pd.DataFrame({'비고' : book_name,'수업시간표' : plan_time, '교수 이름' : gyosu_name ,  '대학' : daesang_hakgwa, '시간표':
                          bigo,  '이수구분' : isu_gbn_name, '온/오프' : kang_onoff_gbn_nm})

data_frame.to_csv('데이터 정리.csv', encoding='cp949' ,mode='w')









