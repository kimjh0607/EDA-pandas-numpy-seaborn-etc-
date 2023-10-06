import pandas as pd

points_list = [0] * 7

def result_deco(func):
    def wrapper(*args, **kwargs):
        global points_list
        question_no, points, result = func(*args, **kwargs)
        if result:
            points_list[question_no] = points
            print(f'정답입니다! {points}점 누적 되었습니다!')
        else:
            points_list[question_no] = 0
            print('오답입니다. 다시 한번 확인해주세요.')        

        print('현재 누적 점수:', sum(points_list), '/ 100')
        
    return wrapper

# 1-1
@result_deco
def check_01_01(df: pd.core.frame.DataFrame):
    question_no, points = 0, 10

    condition01 = df.describe()['Year'].loc['count'] == 15316.0
    condition02 = df.describe()['Year'].loc['max'] == 2008.0
    condition03 = type(df.loc[774,'City'])==float
    condition04 = len(df) == 15433

    if condition01 and condition02 and condition03 and condition04:
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 10

    condition01 = (df != df.dropna(axis=0)).sum().sum() == 0
    condition02 = len(df) == 15316


    if condition01 and condition02:
        result = True
    else:
        result = False
    
    return question_no, points, result
    
# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 10

    for col in df.columns:
        if col != 'Year':
            if df[col].apply(lambda x: type(x)!=str).sum() != 0:
                result = False
                break
        else:
            if df[col].apply(lambda x: type(x)!=int).sum() != 0:
                result = False
                break
    else:
        result = True

    return question_no, points, result

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 3, 15

    if len(df) != 6:
        result = False
        return question_no, points, result

    athletes = ['YUN, Ok-Hee', 'JOO, Hyun-Jung', 'LEE, Chang-Hwan', 'IM, Dong-Hyun', 'PARK, Kyung-Mo', 'PARK, Sung-Hyun']
    for athlete in df.Athlete:
        if not athlete in athletes:
            result = False
            break
    else:
        result = True
    
    return question_no, points, result
    
# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 4, 15

    condition01 = df.index.names == ['Year', 'Medal']
    condition02 = list(map(lambda x: x[1],df.index.values)) == ['Gold', 'Silver', 'Bronze'] * 8
    condition03 = df.loc[(2008,'Gold')][0] == 13
    condition04 = df.loc[(1976,'Bronze')][0] == 4
    condition05 = len(df) == 24

    if condition01 and condition02 and condition03 and condition04 and condition05:
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-3
@result_deco
def check_02_03(df: pd.core.frame.DataFrame):
    question_no, points = 5, 20
    
    condition01 = df.iloc[3][0] == 'China'
    condition02 = df.iloc[3][1] == 50
    condition03 = df.Medal.sum() == 467
    condition04 = df.iloc[-1][0] == 'Ukraine'

    if condition01 and condition02 and condition03 and condition04:
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-4
@result_deco
def check_02_04(df: pd.core.frame.DataFrame):
    question_no, points = 6, 20

    condition01 = df.iloc[5][0] == 'Italy'
    condition02 = df.iloc[3][1:].to_list() == [16, 22, 12]
    condition03 = df.iloc[-1].to_list() == ['Korea, South', 7, 15, 5]
    condition04 = df['Gold'].sum() == 168
    condition05 = df.iloc[:,1:].sum().sum() == 467

    if condition01 and condition02 and condition03 and condition04 and condition05:
        result = True
    else:
        result = False
    
    return question_no, points, result