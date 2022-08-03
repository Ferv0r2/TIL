import pandas as pd

## 데이터셋 불러오기

# csv
df1 = pd.read_csv('./Python/Bigdata/content/countries.csv')
print(df1)

# excel
df2 = pd.read_excel('./Python/Bigdata/content/dust.xlsx')
print(df2)

## 데이터 전처리

# 컬럼명 변경
df2.rename(columns={'날짜':'DAY', '아황산가스':'SO2', '일산화탄소':'CO', '오존':'O3', '이산화질소':'NO2'}, inplace=True)
print(df2)

# 결측값 유무 파악
nan = df2.isnull()
print(nan.any())

# 결측값 갯수 파악
print(nan.sum())

# 전처리 - 결측치 제거
df2.drop(['PM10'], axis=1, inplace=True)
print(df2)

# 전처리 - 결측값 변경 (평균)
# 데이터 전처리 : 결측값 변경
avg = df2['SO2'].mean()
df2['SO2']=df2['SO2'].fillna(avg)

# 데이터 전처리 : 결측값 변경
avg = df2['CO'].mean()
df2['CO']=df2['CO'].fillna(avg)

# 결측값 변경 확인
print(nan.sum())

# 전체 구조 확인하기
print(df1.info())

# 인덱스, 행렬, 둘다
print(df1.index)
print(df1.values)
print(df1.value_counts)

# 데이터 통계치 확인하기
print(df2.describe())

# 데이터 타입 확인하기
print(df2.dtypes)

# SO2 데이터 타입 변경하기
df2['SO2']=df2['SO2'].astype(int)
print(df2.dtypes)