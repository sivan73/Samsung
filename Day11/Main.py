Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
im
port seaborn as sns
SyntaxError: invalid syntax
import seaborn as sns
import folium

path = r"C:\Users\Lenovo\Documents\Day11\NFHS5_StateIndicators.csv"

#Phase 1
#Phase 1: Data Setup and Aggregation
#Goal: Load, clean, and structure the NFHS-5 state-level dataset to compare health indicators across different demographics.

#Step 1: Download the official state-wise indicator dataset from the National Family Health Survey (NFHS-5).
#Step 2:
df = pd.read_csv(path)
df.columns
Index(['States/UTs', 'Area', 'Number of Households surveyed',
       'Number of Women age 15-49 years interviewed',
       'Number of Men age 15-54 years interviewed',
       'Female population age 6 years and above who ever attended school (%)',
       'Population below age 15 years (%)',
       ' Sex ratio of the total population (females per 1,000 males)',
       'Sex ratio at birth for children born in the last five years (females per 1,000 males)',
       'Children under age 5 years whose birth was registered with the civil authority (%)',
       ...
       'Women (age 15-49 years) having a mobile phone that they themselves use (%)',
       'Women age 15-24 years who use hygienic methods of protection during their menstrual period26 (%)',
       'Ever-married women age 18-49 years who have ever experienced spousal violence27 (%)',
       'Ever-married women age 18-49 years who have experienced physical violence during any pregnancy (%)',
       'Young women age 18-29 years who experienced sexual violence by age 18 (%)',
       'Women age 15 years and above who use any kind of tobacco (%)',
       'Men age 15 years and above who use any kind of tobacco (%)',
       'Women age 15 years and above who consume alcohol (%)',
       'Men age 15 years and above who consume alcohol (%)', 'Unnamed: 136'],
      dtype='str', length=137)
dfcols = list(df.columns)
dfcols

health_df = df[['States/UTs','Women (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)',
    'Men (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2) (%)',
    'Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)',
    'All women age 15-49 years who are anaemic22 (%)',
    'Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)',
    'Men age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level  or taking medicine to control blood sugar level23 (%)',
    'Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)',
    'Men age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)']].copy()
health_df.rename(columns={
    'States/UTs': 'State',
    'Women (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2)21 (%)': 'Obesity_Women',
    'Men (age 15-49 years) who are overweight or obese (BMI ≥25.0 kg/m2) (%)': 'Obesity_Men',
    'Children age 6-59 months who are anaemic (<11.0 g/dl)22 (%)': 'Anaemia_Children',
    'All women age 15-49 years who are anaemic22 (%)': 'Anaemia_Women',
    'Women age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level or taking medicine to control blood sugar level23 (%)': 'BloodSugar_Women',
    'Men age 15 years and above wih high or very high (>140 mg/dl) Blood sugar level  or taking medicine to control blood sugar level23 (%)': 'BloodSugar_Men',
    'Women age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)': 'Hypertension_Women',
    'Men age 15 years and above wih Elevated blood pressure (Systolic ≥140 mm of Hg and/or Diastolic ≥90 mm of Hg) or taking medicine to control blood pressure (%)': 'Hypertension_Men'
}, inplace=True)
numeric_cols = [
    "Obesity_Men",
    "Obesity_Women",
    "Anaemia_Children",
    "Anaemia_Women",
    "HighBloodSugar_Men",
    "HighBloodSugar_Women",
    "Hypertension_Men",
    "Hypertension_Women"
]
for col in numeric_cols:
    health_df[col] = pd.to_numeric(health_df[col],errors="coerce")

    
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'HighBloodSugar_Men'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    health_df[col] = pd.to_numeric(health_df[col],errors="coerce")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'HighBloodSugar_Men'
numeric_cols = [
    "Obesity_Men",
    "Obesity_Women",
    "Anaemia_Children",
    "Anaemia_Women",
    "BloodSugar_Men",
    "BloodSugar_Women",
    "Hypertension_Men",
    "Hypertension_Women"]

for col in numeric_cols:
    health_df[col] = pd.to_numeric(health_df[col], errors="coerce")

    
print(health_df.isnull().sum())
State                 0
Obesity_Women         1
Obesity_Men           3
Anaemia_Children      1
Anaemia_Women         1
BloodSugar_Women      1
BloodSugar_Men        1
Hypertension_Women    1
Hypertension_Men      1
dtype: int64
health_df["Gender_Obesity_Gap"] = (health_df["Obesity_Women"]- health_df["Obesity_Men"])
health_df.head()
                       State  ...  Gender_Obesity_Gap
0                      India  ...                 3.4
1                      India  ...                 0.4
2                      India  ...                 1.1
3  Andaman & Nicobar Islands  ...                 4.7
4  Andaman & Nicobar Islands  ...               -14.9

[5 rows x 10 columns]
>>> health_df.info()
<class 'pandas.DataFrame'>
RangeIndex: 110 entries, 0 to 109
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   State               110 non-null    str    
 1   Obesity_Women       109 non-null    float64
 2   Obesity_Men         107 non-null    float64
 3   Anaemia_Children    109 non-null    float64
 4   Anaemia_Women       109 non-null    float64
 5   BloodSugar_Women    109 non-null    float64
 6   BloodSugar_Men      109 non-null    float64
 7   Hypertension_Women  109 non-null    float64
 8   Hypertension_Men    109 non-null    float64
 9   Gender_Obesity_Gap  107 non-null    float64
dtypes: float64(9), str(1)
memory usage: 8.7 KB
>>> #Step 2 completed
>>> #step 3 completed
>>> print(health_df.isnull().sum())
State                 0
Obesity_Women         1
Obesity_Men           3
Anaemia_Children      1
Anaemia_Women         1
BloodSugar_Women      1
BloodSugar_Men        1
Hypertension_Women    1
Hypertension_Men      1
Gender_Obesity_Gap    3
dtype: int64
>>> corr = health_df[[
...     "Anaemia_Children",
...     "Obesity_Men",
...     "Obesity_Women",
...     "Anaemia_Women"]].corr(method="pearson")
>>> corr
                  Anaemia_Children  Obesity_Men  Obesity_Women  Anaemia_Women
Anaemia_Children          1.000000    -0.323490      -0.167683       0.758598
Obesity_Men              -0.323490     1.000000       0.852852      -0.219146
Obesity_Women            -0.167683     0.852852       1.000000      -0.151936
Anaemia_Women             0.758598    -0.219146      -0.151936       1.000000
>>> #step 4 completed - health_df["Gender_Obesity_Gap"
>>> #Phase 2: Exploratory Data Analysis (EDA) and Plotting
>>> #step 1
>>> corr
                  Anaemia_Children  Obesity_Men  Obesity_Women  Anaemia_Women
Anaemia_Children          1.000000    -0.323490      -0.167683       0.758598
Obesity_Men              -0.323490     1.000000       0.852852      -0.219146
Obesity_Women            -0.167683     0.852852       1.000000      -0.151936
Anaemia_Women             0.758598    -0.219146      -0.151936       1.000000
