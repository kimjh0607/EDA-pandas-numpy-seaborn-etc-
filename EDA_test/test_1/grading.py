import pandas as pd
import numpy as np

points_list = [0] * 9

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

        print('현재 누적 점수:', sum(points_list), '/ 60')
        
    return wrapper

# 1-1
@result_deco
def check_01_01(df: pd.core.frame.DataFrame):
    question_no, points = 0, 10

    if df.index.to_list() == list(range(0, 25)) and df.loc[0]['자치구'] == '종로구':
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 10

    columns = ['기간', '자치구', '세대', '합계', '남자', '여자', '한국인 계', '한국인 남자', '한국인 여자', 
               '등록외국인 계', '등록외국인 남자', '등록외국인 여자', '세대당인구', '65세이상고령자']
    
    for col in df.columns:
        if col not in columns:
            result = False
            break
    else:
       result = True
    
    return question_no, points, result

# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 10

    answer = [np.dtype('O'), np.dtype('O'), np.dtype('int64'), np.dtype('int64'), np.dtype('int64'), 
              np.dtype('int64'), np.dtype('int64'), np.dtype('int64'), np.dtype('int64'), np.dtype('int64'), 
              np.dtype('int64'), np.dtype('int64'), np.dtype('float64'), np.dtype('int64')]
    
    if df.dtypes.to_list() == answer:
        result = True
    else:
        result = False 

    return question_no, points, result
    
################################################################################################################
region_dict = {'도심권': ['종로구', '중구', '용산구'],
               '동북권': ['성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구'],
               '서북권': ['은평구', '서대문구', '마포구'],
               '서남권': ['양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구'],
               '동남권': ['서초구', '강남구', '송파구', '강동구']
               }

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 3, 5

    for region, gu_list in region_dict.items():
        if df[df['권역'] == region]['자치구'].to_list() != gu_list:
            result = False
            break
    else:
        result = True
    
    return question_no, points, result

# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 4, 5

    condition_01 = sorted(df.columns.to_list()) == sorted(['합계', '세대', '여자', '한국인 계', '등록외국인 계', '65세이상고령자'])
    condition_02 = df.index.to_list() == ['동북권', '서남권', '동남권', '서북권', '도심권']
    condition_03 = df.loc['동북권', '합계'] == 3076926
    
    if condition_01 and condition_02 and condition_03:
        result = True
    else:
       result = False 

    return question_no, points, result

# 2-3
@result_deco
def check_02_03(df: pd.core.frame.DataFrame):
    question_no, points = 5, 5

    condition_01 = df.index.to_list() == ['동남권', '동북권', '서북권', '서남권', '도심권']
    condition_02 = round(df.loc['동남권', '외국인비율'], 2) == round(0.9663039709340892, 2)

    for col in ['고령자비율', '외국인비율', '여성비율', '세대당인구']:
        if col not in df.columns:
            points_list[5] = 0
            print('오답입니다. 다시 한번 확인해주세요.')
            break
    else:
        if condition_01 and condition_02:
            result = True
        else:
            result = False

    return question_no, points, result
    
# 2-4
@result_deco
def check_02_04(df: pd.core.frame.DataFrame):
    question_no, points = 6, 5

    condition_01 = df['자치구'].to_list()[:5] == ['양천구', '서초구', '노원구', '송파구', '도봉구']
    condition_02 = bool(round(df[df['자치구'] == '양천구']['외국인비율'], 2).values == round(0.910469, 2))

    for col in ['고령자비율', '외국인비율', '여성비율', '세대당인구']:
        if col not in df.columns:
            result = False
            break
    else:
        if condition_01 and condition_02:
            result = True
        else:
           result = False

    return question_no, points, result

# 2-5
@result_deco
def check_02_05(df: pd.core.frame.DataFrame):
    question_no, points = 7, 10

    condition_01 = round(df.loc['세대당인구', '외국인비율'], 2) == round(-0.943776, 2)
    condition_02 = round(df.loc['여성비율', '고령자비율'], 2) == round(0.079476, 2)
    for col in ['고령자비율', '외국인비율', '여성비율', '세대당인구']:
        if col not in df.columns or col not in df.index:
            result = False
            break
    else:
        if condition_01 and condition_02:
            result = True
        else:
            result = False
            
    return question_no, points, result