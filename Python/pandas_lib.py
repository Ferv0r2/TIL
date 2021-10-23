import pandas as pd

datas = {'이름': ['행복이', 'BTS', '블핑'],
         '중간': [95, 88, 72],
         '기말': [87, 90, 83],
         '과제': [95, 90, 80],
         '출석': [100, 70, 72]}

# 데이터프레임 생성
df1 = pd.DataFrame(datas)

# 특정 형, 열
df1.loc[0]  # 행
df1['이름']  # 열

# 새로운 열 생성
df1['가산점'] = [5, 0, 2]

# 열 삭제
df2 = df1.drop('가산점', axis=1)  # 행 : axis=0, 열 : axis=1

# 필터링 방법
print(df2[df2['중간'] >= 85].head(1))
print(df2[df2['중간'] >= 85].tail(1))

# 데이터 정렬
# 오름차순 : ascending=True 내림차순 : ascending=False
sorted = df2.sort_values('이름', ascending=False)
print(sorted)

print('=========')

# 그룹화
filename = '/content/movies_train.csv'
data = pd.read_csv(filename)

grouped1 = data.groupby(by='genre')
print(grouped1.sum()['box_off_num'])

grouped2 = data['box_off_num'].groupby(
    data['genre']).sum()  # 뒷 data[] 기준으로 앞 data[] 집계
print(grouped2)

grouped3 = data.groupby(['genre', 'distributor'])[
    'box_off_num'].sum()  # 뒷 data[] 기준으로 앞 data[] 집계
print(grouped3)

# 그룹화 메소드 종류
print('합계 :', grouped1.sum()['box_off_num'])  # 합계
print('평균 :', grouped1.mean())  # 평균
print('크기 :', grouped1.size())  # 크기


# 기타 조회
df2.index
df2.columns
df2.values
