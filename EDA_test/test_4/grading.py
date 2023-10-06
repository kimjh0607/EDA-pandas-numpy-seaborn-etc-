import pandas as pd

points_list = [0] * 11

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
    question_no, points = 0, 5

    condition_dict = {
        'condition01': len(df) == 182,
        'condition02': 0 not in df.index and 209 not in df.index,
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 5

    condition_dict = {
        'condition01': len(df) == 182,
        'condition02': 0 not in df.index and 209 not in df.index,
        'condition03': df.loc[49, 'country'] == 'Czech Republic',
        'condition04': df.loc[183, 'country'] == 'Eswatini',
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 10

    condition_dict = {
        'condition01': len(df) == 182,
        'condition02': 0 not in df.index and 209 not in df.index,
        'condition03': df.loc[49, 'country'] == 'Czech Republic',
        'condition04': df.loc[183, 'country'] == 'Eswatini',
        'condition05': df.loc[3, 'code'] == 'AD',
        'condition06': df.loc[210, 'code'] == 'YE',
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-1
# @result_deco
# def check_02_01(df: pd.core.frame.DataFrame):
#     question_no, points = 3, 10

#     condition_dict = {
#         'condition01': 'Country / Dependency' in df.columns,
#         'condition02': 'Population' in df.columns,
#         'condition03': 'China' in df[df.Rank.isin(['1', '2', 1, 2])]['Country / Dependency'].to_list(),
#         }

#     if sum(condition_dict.values()) == len(condition_dict):
#         result = True
#     else:
#         result = False
    
#     return question_no, points, result

@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 3, 10

    condition_dict = {
        'condition01': 'Country / Dependency' in df.columns,
        'condition02': 'Population' in df.columns,
        'condition03': 'China' in df[df.index.isin([0, 1, 2, 3])]['Country / Dependency'].to_list(),
    }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result


# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 4, 5

    condition_dict = {
        'condition01': 'Country / Dependency' not in df.columns,
        'condition02': 'Population' not in df.columns,
        'condition03': 'World' not in df['country'],
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 2-3
@result_deco
def check_02_03(df: pd.core.frame.DataFrame):
    question_no, points = 5, 5

    condition_dict = {
        'condition01': 'Country / Dependency' not in df.columns,
        'condition02': 'Population' not in df.columns,
        'condition03': 'World' not in df['country'],
        'condition04': 'Laos' not in df['country'],
        'condition05': 'Korea, Republic of' not in df['country'],
        'condition06': df.index.is_monotonic_increasing
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result
    
# 2-4
@result_deco
def check_02_04(df: pd.core.frame.DataFrame):
    question_no, points = 6, 10

    columns = ['country', 'incomeperperson', 'internetuserate', 'urbanrate', 'code', 'population']

    condition_dict = {
        'condition01': df.index.is_monotonic_increasing,
        'condition02': df.code.is_monotonic_increasing,
        'condition03': sum([bool(col not in columns) for col in df.columns]) == 0,
        'condition04': sum(df[df.country == 'Samoa']['incomeperperson'] == 1784.071284) == 1,
        'condition05': df[df.population == df.population.max()]['code'].values in ['CN', 'IN'],
        'condition06': len(df) == 182,
        'condition07': df.iloc[0].code == 'AD',

        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result
    
# 3-1
@result_deco
def check_03_01(df: pd.core.frame.DataFrame):
    question_no, points = 7, 10

    columns = ['name', 'code', 'region', 'sub_region', 'intermediate_region']

    condition_dict = {
        'condition01': df.code.isna().sum() == 0,
        'condition02': type(df[df['name'] == 'Namibia']['code'].values[0]) == str,
        'condition03': sum([bool(col not in columns) for col in df.columns]) == 0,
        'condition04': df.iloc[0].code == 'AF',
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result
    
# 3-2
@result_deco
def check_03_02(df: pd.core.frame.DataFrame):
    question_no, points = 8, 10
    
    change_nan = lambda value: '-' if type(value) == float else value
    df['intermediate_region'] = df['intermediate_region'].apply(change_nan)

    columns = ['code', 'country', 'population', 'income_per_person', 'internet_use_rate', 'urbanrate', 'region', 'sub_region', 'intermediate_region']

    condition_dict = {
        'condition01': df.code.is_monotonic_increasing,
        'condition02': df.isna().sum().sum() == 0,
        'condition03': sum(df.columns == columns) == len(columns),
        'condition04': df.iloc[0].code == 'AD',
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result
    
# 4-1
@result_deco
def check_04_01(df: pd.core.frame.DataFrame):
    question_no, points = 9, 15
    
    index_0 = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    index_1 = ['Latin America and the Caribbean', 'Northern America', 'Central Asia', 'Micronesia', 'Polynesia']
    columns = ['weighted_ave_internet', 'weighted_ave_income']
    
    condition_dict = {
        'condition01': sum(bool(idx in df.index.get_level_values(0).unique()) for idx in index_0) == len(index_0),
        'condition02': sum(bool(idx in df.index.get_level_values(1).unique()) for idx in index_1) == len(index_1),
        'condition03': sum(df.columns == columns) == len(columns),
        'condition04': sum(df[df['weighted_ave_internet'] == df['weighted_ave_internet'].max()].index == ('Europe', 'Northern Europe')) == 1,
        'condition05': sum(df[df['weighted_ave_internet'] == df['weighted_ave_internet'].min()].index.get_level_values(1) == 'Melanesia') == 1,
        'condition06': sum(df[df['weighted_ave_income'] == df['weighted_ave_income'].max()].index == ('Americas', 'Northern America')) == 1,
        'condition07': sum(df[df['weighted_ave_income'] == df['weighted_ave_income'].min()].index == ('Africa', 'Sub-Saharan Africa')) == 1,
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result

# 4-2
@result_deco
def check_04_02(df: pd.core.frame.DataFrame):
    question_no, points = 10, 15
    
    index_0 = ['Asia']
    index_1 = ['Eastern Asia', 'Southern Asia']
    columns = ['weighted_ave_internet', 'weighted_ave_income']
    
    condition_dict = {
        'condition01': sum(bool(idx in df.index.get_level_values(0).unique()) for idx in index_0) == len(index_0),
        'condition02': sum(bool(idx in df.index.get_level_values(1).unique()) for idx in index_1) == len(index_1),
        'condition03': sum(df.columns == columns) == len(columns),
        'condition04': sum(df[df['weighted_ave_internet'] == df['weighted_ave_internet'].max()].index.get_level_values(1) == 'Eastern Asia') == 1,
        'condition05': sum(df[df['weighted_ave_income'] == df['weighted_ave_income'].min()].index.get_level_values(1) == 'Southern Asia') == 1,
        'condition06': sum(df[df['weighted_ave_income'] == df['weighted_ave_income'].max()]['weighted_ave_income'] >= 32000) == 1,
        'condition07': sum(df[df['weighted_ave_internet'] == df['weighted_ave_internet'].min()]['weighted_ave_internet'] <= 20) == 1,
        }

    if sum(condition_dict.values()) == len(condition_dict):
        result = True
    else:
        result = False
    
    return question_no, points, result