import pandas as pd
import numpy as np

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

    condition01 = df.iloc[19350]['표준 성분명'] == '작약캘러스배양여과물'
    condition02 = len(df) == 20375
    condition03 = df.equals(df.sort_values('성분코드'))

    if condition01 and condition02 and condition03:
        result = True
    else:
        result = False
    
    return question_no, points, result

# 1-2
@result_deco
def check_01_02(df: pd.core.frame.DataFrame):
    question_no, points = 1, 15

    result = True
    for _idx, row in df.iterrows():
        for cell in row:
            if type(cell) is str and '\r' in cell:
                result = False
                break
        if result == False:
            break
    else:
        result = True

    return question_no, points, result

# 1-3
@result_deco
def check_01_03(df: pd.core.frame.DataFrame):
    question_no, points = 2, 15

    replace_dict = {
        'Acetobacter/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitumit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia': 'Acetobacter/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitumit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia Ferment',
        'Saccharomyces/Licorice Root/Rehmannia Glutinosa Root/Angelica Gigas Root/Ophiopogon Japonicus Root/Atractylodes Macrocephala Root/Paeonia Lactiflora Root/Anemarrhena Asphodeloides Root/Fraxinus Excelsior Bark/Asparagus Cochinchinensis/Phellodendron Amurense': 'Saccharomyces/Licorice Root/Rehmannia Glutinosa Root/Angelica Gigas Root/Ophiopogon Japonicus Root/Atractylodes Macrocephala Root/Paeonia Lactiflora Root/Anemarrhena Asphodeloides Root/Fraxinus Excelsior Bark/Asparagus Cochinchinensis/Phellodendron Amurense Bark Ferment Extract',
        'Bacillus/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia': 'Bacillus/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia Ferment',
        'Bifida/Angelica Gigas/Angelica Tenuissima Root/Antler Velvet/Rehmannia Glutinosa Root/Atractylodes Japonica Rhizome/Cnidium Officinale Root/Cordyceps Sinensis/Ledebouriella Seseloides Root/Licorice Root/Paeonia Lactiflora Root/Panax Ginseng': 'Bifida/Angelica Gigas/Angelica Tenuissima Root/Antler Velvet/Rehmannia Glutinosa Root/Atractylodes Japonica Rhizome/Cnidium Officinale Root/Cordyceps Sinensis/Ledebouriella Seseloides Root/Licorice Root/Paeonia Lactiflora Root/Panax Ginseng Root/Phellinus Linteus/Scutellaria Baicalensis Root Ferment',
        'Leuconostoc/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia': 'Leuconostoc/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia Ferment',
        'Saccharomyces/Anemarrhena Asphodeloides Root/Angelica Gigas Root/Asparagus Cochinchinensis/Atractylodes Macrocephala Root/Fraxinus Excelsior Bark/Licorice Root/Ophiopogon Japonicus Root/Paeonia Lactiflora Root/Phellodendron Amurense': 'Saccharomyces/Anemarrhena Asphodeloides Root/Angelica Gigas Root/Asparagus Cochinchinensis/Atractylodes Macrocephala Root/Fraxinus Excelsior Bark/Licorice Root/Ophiopogon Japonicus Root/Paeonia Lactiflora Root/Phellodendron Amurense Bark Ferment Extract',
        'Saccharomyces/Camellia Japonica Flower/Castanea Crenata Shell/Diospyros Kaki Leaf/Paeonia Suffruticosa Root/Rhus Javanica/Sanguisorba Officinalis Root Extract': 'Saccharomyces/Camellia Japonica Flower/Castanea Crenata Shell/Diospyros Kaki Leaf/Paeonia Suffruticosa Root/Rhus Javanica/Sanguisorba Officinalis Root Extract Ferment Filtrate',
        'Lactobacillus/Honeysuckle Flower/Licorice Root/Morus Alba Root/Pueraria Lobata Root/Schisandra Chinensis Fruit/Scutellaria Baicalensis Root/Sophora Japonica Flower': 'Lactobacillus/Honeysuckle Flower/Licorice Root/Morus Alba Root/Pueraria Lobata Root/Schizandra Chinensis Fruit/Scutellaria Baicalensis Root/Sophora Japonica Flower Extract Ferment Filtrate',
        'Lactobacillus/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/Cinnamomum Cassia': 'Lactobacillus/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/Cinnamomum Cassia Ramulus Bark Ferment Filtrate',
        'Saccharomyces/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia': 'Saccharomyces/Lycium Chinense Fruit/Rehmannia Glutinosa Root/Cuscuta Chinensis Fruit/Cistanche Deserticola/Zanthoxylum Piperitum Fruit/Chrysanthemum Morifolium Fruit/Poria Cocos/ Cinnamomum Cassia Ferment',
    }

    if df['표준 영문명'].isin(replace_dict.values()).sum() != 0:
        result = True
    else:
        result = False

    return question_no, points, result

# 2-1
@result_deco
def check_02_01(df: pd.core.frame.DataFrame):
    question_no, points = 3, 20

    replace_str_dict = {
        'Algae (Seaweed) Extract': 'Algae Extract',
        'Citrus Aurantifolia (Lime) Extract': 'Citrus Aurantifolia (Lime) Fruit Extract',
        'Eucalyptus Globulus (Eucalyptus) Leaf Oil': 'Eucalyptus Globulus Leaf Oil',
        'Galactomyces Ferment Filtrate (Pitera)': 'Galactomyces Ferment Filtrate',
        'Bacillus/Soybean/ Folic Acid Ferment Extract': 'Bacillus/Folic Acid/Soybean Ferment Extract',
        'Butyrospermum Parkii (Shea Butter)': 'Butyrospermum Parkii (Shea) Butter',
        'Sea Salt/Maris Sal/Sel Marin': 'Sea Salt',
        'Parfum/Fragrance': 'Fragrance|Perfume|Parfum',
        ', Fragrance': ', Fragrance|Perfume|Parfum',
        }
    
    condition01 = len(df[df['Ingredients'].str.endswith('.')])
    condition02 = df['Ingredients'].str.contains('. May Contain').sum()

    if condition01 or condition02:
        result = False
    else:
        for value in [value for value in replace_str_dict.values() if '(' not in value]:
            if not df['Ingredients'].str.contains(value).sum():
                result = False
                break
        else:
            result = True
    
    return question_no, points, result

# 2-2
@result_deco
def check_02_02(df: pd.core.frame.DataFrame):
    question_no, points = 4, 10

    def check_strip(ingredients_list: list) -> bool:
        
        for ingredients in ingredients_list:
            if ingredients.startswith(' ') or ingredients.endswith(' '):
                return False
        else:
            return True

    if 'Ingredients List' in df.columns:
        condition01 = sum(df['Ingredients List'].apply(type) == list) == len(df)
        condition02 = sum(df['Ingredients List'].apply(check_strip)) == len(df)
        if condition01 and condition02:
            result = True
        else:
            result = False
    else:
        result = False

    return question_no, points, result

# 3-1
@result_deco
def check_03_01(df: pd.core.frame.DataFrame):
    question_no, points = 5, 15
    
    condition01 = 'C13-14 Isoparaffin' in df[df['Name']=='The Moisturizing Soft Cream']['Ingredients'].values[0]
    condition02 = 'Code List' in df.columns
    if condition01 and condition02:
        if 2522 in df[df['Name']=='The Moisturizing Soft Cream']['Code List'].values[0]:
            result = True
        else:
            result = False
    else:
        result = False

    return question_no, points, result

# 3-2
@result_deco
def check_03_02(df: pd.core.frame.DataFrame):
    question_no, points = 6, 15

    condition01 = sum(df.index) == 868
    condition02 = df['성분코드'].sum() == 873
    condition03 = sum(df['표준 성분명'].apply(len)) == 32
    condition04 = df.iloc[df['표준 성분명'].apply(len).argmax()]['표준 영문명'][3:5] == 'ne'
    condition05 = df['구영문명'].fillna(False).apply(bool).sum() == 1

    if sum([condition01, condition02, condition03, condition04, condition05]) == 5:
        result = True
    else:
        result = False

    return question_no, points, result