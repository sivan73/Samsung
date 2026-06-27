Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#day 9
import datetime
datetime.now().date()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    datetime.now().date()
AttributeError: module 'datetime' has no attribute 'now'
datetime.date()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    datetime.date()
TypeError: function missing required argument 'year' (pos 1)
datetime.now()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    datetime.now()
AttributeError: module 'datetime' has no attribute 'now'
datetime.datetime.now().date()
datetime.date(2026, 6, 24)
datetime.datetime.now().time()
datetime.time(9, 15, 40, 143247)
for i in range(0, 987567):
    print(datetime.datetime.now().time())

    

Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(datetime.datetime.now().time())
KeyboardInterrupt
Ls = [for i in range(0, 9875): datetime.datetime.now().time()]
SyntaxError: invalid syntax
Ls = [datetime.datetime.now().time() for i in range(0, 9875)]
Ls

Ls = tuple(Ls)
Ls

type(Ls)
<class 'tuple'>
import pandas as pd
import 
wti = pd.read_csv(r"C:\Users\Lenovo\Downloads\DCOILWTICO.csv")
wti.head()
  observation_date  DCOILWTICO
0       2021-06-15       72.06
1       2021-06-16       72.03
2       2021-06-17       71.06
3       2021-06-18       71.64
4       2021-06-21       73.64
wti.info()
<class 'pandas.DataFrame'>
RangeIndex: 1305 entries, 0 to 1304
Data columns (total 2 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   observation_date  1305 non-null   str    
 1   DCOILWTICO        1249 non-null   float64
dtypes: float64(1), str(1)
memory usage: 20.5 KB
wti['N_DATE'] = pd.to_datetime(wti['DATE'])
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'DATE'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    wti['N_DATE'] = pd.to_datetime(wti['DATE'])
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'DATE'
wti['N_DATE'] = pd.to_datetime(wti['observation_date'])
wti.head()
  observation_date  DCOILWTICO     N_DATE
0       2021-06-15       72.06 2021-06-15
1       2021-06-16       72.03 2021-06-16
2       2021-06-17       71.06 2021-06-17
3       2021-06-18       71.64 2021-06-18
4       2021-06-21       73.64 2021-06-21
df = wti.drop(['observation_date'], axis =1 )
df.head()
   DCOILWTICO     N_DATE
0       72.06 2021-06-15
1       72.03 2021-06-16
2       71.06 2021-06-17
3       71.64 2021-06-18
4       73.64 2021-06-21
#or we can project by
df = df['']
KeyboardInterrupt
#df = df['DCOILWTICO','N_DATE']
df.setindex('N_DATE', inplace = True)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    df.setindex('N_DATE', inplace = True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'setindex'. Did you mean: 'set_index'?
df.set_index('N_DATE', inplace = True)
df.head()
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
df.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 1305 entries, 2021-06-15 to 2026-06-15
Data columns (total 1 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   DCOILWTICO  1249 non-null   float64
dtypes: float64(1)
memory usage: 20.4 KB
df['2016-11-04': '2016-11-10']
Empty DataFrame
Columns: [DCOILWTICO]
Index: []
pd.date_range(start='2021-01-01', end=None, periods=5, freq='D', tz=None)
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05'],
              dtype='datetime64[us]', freq='D')
df.iloc[5:10, :]
            DCOILWTICO
N_DATE                
2021-06-22       73.15
2021-06-23       73.11
2021-06-24       73.31
2021-06-25       74.21
2021-06-28       72.98
df.iloc[:10.:]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    df.iloc[:10.:]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexing.py", line 1207, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexing.py", line 1750, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexing.py", line 1785, in _get_slice_axis
    labels._validate_positional_slice(slice_obj)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 4041, in _validate_positional_slice
    self._validate_indexer("positional", key.stop, "iloc")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 6864, in _validate_indexer
    self._raise_invalid_indexer(form, key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 4125, in _raise_invalid_indexer
    raise TypeError(msg)
TypeError: cannot do positional indexing on DatetimeIndex with these indexers [10.0] of type float
df.iloc[:10,:]
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
2021-06-22       73.15
2021-06-23       73.11
2021-06-24       73.31
2021-06-25       74.21
2021-06-28       72.98
p_data = pd.period_range(start = '2020-1-1',end= '2020-12-1',periods = None, freq = 'M')
p_data
PeriodIndex(['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06',
             '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12'],
            dtype='period[M]')
for i in p_data:
    print("{0}{1}".format(i.start_time,i.end_time))

    
2020-01-01 00:00:002020-01-31 23:59:59.999999
2020-02-01 00:00:002020-02-29 23:59:59.999999
2020-03-01 00:00:002020-03-31 23:59:59.999999
2020-04-01 00:00:002020-04-30 23:59:59.999999
2020-05-01 00:00:002020-05-31 23:59:59.999999
2020-06-01 00:00:002020-06-30 23:59:59.999999
2020-07-01 00:00:002020-07-31 23:59:59.999999
2020-08-01 00:00:002020-08-31 23:59:59.999999
2020-09-01 00:00:002020-09-30 23:59:59.999999
2020-10-01 00:00:002020-10-31 23:59:59.999999
2020-11-01 00:00:002020-11-30 23:59:59.999999
2020-12-01 00:00:002020-12-31 23:59:59.999999
df
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
...                ...
2026-06-09       91.90
2026-06-10       93.68
2026-06-11       91.58
2026-06-12       88.62
2026-06-15       84.65

[1305 rows x 1 columns]
for i in range(0,len(df),5):
    print(df.iloc[i:5,0].mean(),ends= ' ')

    
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    print(df.iloc[i:5,0].mean(),ends= ' ')
TypeError: print() got an unexpected keyword argument 'ends'. Did you mean 'end'?
for i in range(0,len(df),5):
    print(df.iloc[i:5,0].mean(),end= ' ')

    
72.086 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan 
for i in range(0,len(df),5):
    print(df.iloc[i:i+5,0].mean(),end= ' ')

    
72.086 73.352 74.34 73.518 71.636 70.824 72.58200000000001 68.55 68.51 64.69000000000001 68.316 69.1175 69.29400000000001 71.66199999999999 73.206 75.882 79.09599999999999 81.572 83.88 83.732 81.364 81.70800000000001 78.17 75.50666666666666 66.838 71.628 70.684 73.325 76.148 78.282 82.3675 85.638 87.876 90.014 91.46799999999999 92.23499999999999 92.966 111.424 110.18199999999999 102.214 112.774 103.04 97.398 104.965 102.29 103.96399999999998 106.268 107.196 111.428 114.145 116.78 120.93199999999999 115.34 108.59400000000001 110.8425 103.87 99.598 101.30999999999999 98.95599999999999 93.39399999999999 94.396 92.05 95.268 89.1375 85.868 86.832 81.666 81.452 89.732 87.854 85.38 87.95400000000001 90.188 87.22 82.798 78.07749999999999 79.238 72.28999999999999 75.542 77.83500000000001 79.2325 74.352 77.69749999999999 80.596 79.596 75.73400000000001 78.712 78.10249999999999 75.45 78.502 76.16799999999999 68.176 70.394 75.29400000000001 80.47 82.09400000000001 78.76 75.71599999999998 70.66 71.622 71.76599999999999 72.8175 70.31 70.54999999999998 70.00750000000001 70.14200000000001 69.488 72.625 75.422 76.536 80.278 81.426 83.154 80.57 79.96 82.96249999999999 87.19399999999999 89.978 89.92 91.26599999999999 84.6775 85.356 87.79400000000001 84.704 81.69200000000001 77.2525 76.824 76.10999999999999 75.148 70.35 70.356 73.495 73.515 72.206 72.27250000000001 73.738 76.762 74.97399999999999 75.872 78.3725 78.676 79.80600000000001 79.366 81.392 82.53599999999999 83.265 86.894 86.29599999999999 84.168 84.564 80.90599999999999 80.38399999999999 80.75 78.94 78.66599999999998 76.22999999999999 79.75800000000001 82.58749999999999 82.946 84.3375 83.36000000000001 82.586 78.46 76.544 77.73 78.362 75.194 75.8525 69.94200000000001 69.11200000000001 72.188 69.702 73.63399999999999 75.17 70.878 70.89200000000001 69.52199999999999 71.905 68.594 70.096 68.67249999999999 68.954 70.44800000000001 70.084 71.065 73.795 76.455 79.21000000000001 75.284 73.30999999999999 71.89000000000001 72.02499999999999 71.89 69.44800000000001 67.054 67.252 68.28399999999999 70.288 66.92600000000002 61.428 63.2925 63.588 60.03000000000001 61.35600000000001 64.074 63.084999999999994 62.108000000000004 64.604 69.934 74.1475 66.166 68.14750000000001 68.952 68.11399999999999 66.99199999999999 69.488 65.28999999999999 64.23599999999999 64.27799999999999 64.3525 63.78800000000001 63.274 63.84400000000001 65.088 62.236000000000004 62.0 58.705999999999996 60.96 61.426 60.7 60.0925 59.964 58.777499999999996 59.398 57.88199999999999 56.541999999999994 57.94 57.589999999999996 57.814 60.305 60.215999999999994 63.132000000000005 63.676 63.7825 65.514 66.822 83.072 91.598 95.256 97.364 108.0 101.88600000000001 91.908 97.196 107.54 100.64399999999999 107.24000000000001 103.58250000000001 93.94999999999999 96.676 90.08600000000001 
print(NaN)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(NaN)
NameError: name 'NaN' is not defined
NaN = ['NaN']
NaN
['NaN']
del NaN
df
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
...                ...
2026-06-09       91.90
2026-06-10       93.68
2026-06-11       91.58
2026-06-12       88.62
2026-06-15       84.65

[1305 rows x 1 columns]
df.rolling().mean()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    df.rolling().mean()
TypeError: NDFrame.rolling() missing 1 required positional argument: 'window'
df.rolling(5).mean()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21      72.086
...                ...
2026-06-09      95.562
2026-06-10      94.346
2026-06-11      93.296
2026-06-12      92.156
2026-06-15      90.086

[1305 rows x 1 columns]
df.rolling(100).mean()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21         NaN
...                ...
2026-06-09         NaN
2026-06-10         NaN
2026-06-11         NaN
2026-06-12         NaN
2026-06-15         NaN

[1305 rows x 1 columns]
df.rolling(5).mean()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21      72.086
...                ...
2026-06-09      95.562
2026-06-10      94.346
2026-06-11      93.296
2026-06-12      92.156
2026-06-15      90.086

[1305 rows x 1 columns]
df.rolling(5).std()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21    0.957904
...                ...
2026-06-09    2.936821
2026-06-10    1.804517
2026-06-11    1.499427
2026-06-12    2.414100
2026-06-15    3.540435

[1305 rows x 1 columns]
df.rolling(5).var()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21     0.91758
...                ...
2026-06-09     8.62492
2026-06-10     3.25628
2026-06-11     2.24828
2026-06-12     5.82788
2026-06-15    12.53468

[1305 rows x 1 columns]
df.rolling(5).sum()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21      360.43
...                ...
2026-06-09      477.81
2026-06-10      471.73
2026-06-11      466.48
2026-06-12      460.78
2026-06-15      450.43

[1305 rows x 1 columns]
df.rolling(5).min()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21       71.06
...                ...
2026-06-09       91.90
2026-06-10       91.90
2026-06-11       91.58
2026-06-12       88.62
2026-06-15       84.65

[1305 rows x 1 columns]
df.rolling(5).max()
            DCOILWTICO
N_DATE                
2021-06-15         NaN
2021-06-16         NaN
2021-06-17         NaN
2021-06-18         NaN
2021-06-21       73.64
...                ...
2026-06-09       99.76
2026-06-10       96.83
2026-06-11       95.00
2026-06-12       95.00
2026-06-15       93.68

[1305 rows x 1 columns]
from datetime import date,datetime,time
import matplotlib.pyplot as plt
impo
rt yfinance as yf
SyntaxError: invalid syntax
import yfinance as yf
start = datetime(2020,1,1)
end = datetime(2020,12,1)
sec = yf.download(tickers = ['005930.KS'], start= start, end = end)

[*********************100%***********************]  1 of 1 completed
sec
sec.head()
Price              Close          High           Low          Open    Volume
Ticker         005930.KS     005930.KS     005930.KS     005930.KS 005930.KS
Date                                                                        
2020-01-02  47372.847656  48059.410666  47201.206904  47630.308785  12993228
2020-01-03  47630.304688  48574.328744  47115.382475  48059.406532  15422255
2020-01-06  47630.304688  47716.125056  46857.921368  47115.382475  10278951
2020-01-07  47887.765625  48402.687836  47716.124888  47801.945256  10009778
2020-01-08  48745.976562  49260.898850  47973.593131  48231.054275  23501171
sec.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 227 entries, 2020-01-02 to 2020-11-30
Data columns (total 5 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   (Close, 005930.KS)   227 non-null    float64
 1   (High, 005930.KS)    227 non-null    float64
 2   (Low, 005930.KS)     227 non-null    float64
 3   (Open, 005930.KS)    227 non-null    float64
 4   (Volume, 005930.KS)  227 non-null    int64  
dtypes: float64(4), int64(1)
memory usage: 10.6 KB
sec = yf.download(tickers = ['005930.KS'], start= start, end = (2026,6,24))

[*********************100%***********************]  1 of 1 completed

1 Failed download:
['005930.KS']: ValueError("Unable to parse input dt (2026, 6, 24) of type <class 'tuple'>")
end = (2026,6,24)
sec = yf.download(tickers = ['005930.KS'], start= start, end = end)

[*********************100%***********************]  1 of 1 completed

1 Failed download:
['005930.KS']: ValueError("Unable to parse input dt (2026, 6, 24) of type <class 'tuple'>")
end = datetime(2026,6,24)
sec = yf.download(tickers = ['005930.KS'], start= start, end = end)

[*********************100%***********************]  1 of 1 completed
sec.head()
Price              Close          High           Low          Open    Volume
Ticker         005930.KS     005930.KS     005930.KS     005930.KS 005930.KS
Date                                                                        
2020-01-02  47372.851562  48059.414629  47201.210796  47630.312712  12993228
2020-01-03  47630.316406  48574.340695  47115.394067  48059.418356  15422255
2020-01-06  47630.316406  47716.136796  46857.932897  47115.394067  10278951
2020-01-07  47887.769531  48402.691784  47716.128780  47801.949156  10009778
2020-01-08  48745.980469  49260.902798  47973.596975  48231.058140  23501171
sec.tail()
Price          Close      High       Low      Open    Volume
Ticker     005930.KS 005930.KS 005930.KS 005930.KS 005930.KS
Date                                                        
2026-06-17  346500.0  348000.0  331500.0  332000.0  18134051
2026-06-18  362500.0  363000.0  344500.0  345000.0  32764450
2026-06-19  354000.0  374500.0  346250.0  372500.0  43284898
2026-06-22  353500.0  363000.0  342000.0  343000.0  24330451
2026-06-23  310000.0  353000.0  310000.0  347500.0  41266630
sec.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 1585 entries, 2020-01-02 to 2026-06-23
Data columns (total 5 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   (Close, 005930.KS)   1585 non-null   float64
 1   (High, 005930.KS)    1585 non-null   float64
 2   (Low, 005930.KS)     1585 non-null   float64
 3   (Open, 005930.KS)    1585 non-null   float64
 4   (Volume, 005930.KS)  1585 non-null   int64  
dtypes: float64(4), int64(1)
memory usage: 74.3 KB
ma5 = sec['Adj Close'].rolling(window=5).mean()
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Adj Close'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    ma5 = sec['Adj Close'].rolling(window=5).mean()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4377, in __getitem__
    return self._getitem_multilevel(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4435, in _getitem_multilevel
    loc = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 3523, in get_loc
    loc = self._get_level_indexer(key, level=0)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 3885, in _get_level_indexer
    idx = self._get_loc_single_level_index(level_index, key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 3458, in _get_loc_single_level_index
    return level_index.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Adj Close'
sec.columns()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    sec.columns()
TypeError: 'MultiIndex' object is not callable
sec.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 1585 entries, 2020-01-02 to 2026-06-23
Data columns (total 5 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   (Close, 005930.KS)   1585 non-null   float64
 1   (High, 005930.KS)    1585 non-null   float64
 2   (Low, 005930.KS)     1585 non-null   float64
 3   (Open, 005930.KS)    1585 non-null   float64
 4   (Volume, 005930.KS)  1585 non-null   int64  
dtypes: float64(4), int64(1)
memory usage: 74.3 KB
ma5 = sec['Close'].rolling(window=5).mean()
ma5.head()
Ticker         005930.KS
Date                    
2020-01-02           NaN
2020-01-03           NaN
2020-01-06           NaN
2020-01-07           NaN
2020-01-08  47853.446875
close = sec['Close']
ma5 = sec['Close'].rolling(window=5).mean()
ma10 = sec['Close'].rolling(window=10).mean()
ma60 = sec['Close'].rolling(window=60).mean()
ma120 = sec['Close'].rolling(window=120).mean()
plt.figure(figsize = (30,20))
<Figure size 3000x2000 with 0 Axes>
plt.plot(close,label= 'close', linewidth = 4)
[<matplotlib.lines.Line2D object at 0x00000193D0BE2BA0>]
plt.plot(ma5,label = '5 window')
[<matplotlib.lines.Line2D object at 0x00000193D0C08EC0>]
plt.plot(ma10,label = '10 window')
[<matplotlib.lines.Line2D object at 0x00000193D0C09010>]
plt.plot(ma60,label = '60 window')
[<matplotlib.lines.Line2D object at 0x00000193D0C09160>]
plt.plot(ma120,label = '120 window')
[<matplotlib.lines.Line2D object at 0x00000193D0C092B0>]
plt.legend()
<matplotlib.legend.Legend object at 0x00000193D0BE2CF0>
plt.title('Rolling window calculations')
Text(0.5, 1.0, 'Rolling window calculations')
plt.xlabel('Date')
Text(0.5, 0, 'Date')
plt.ylabel('close price')
Text(0, 0.5, 'close price')
plt.show()
plt.show()
plt.show()
plt.show()
plt.figure(figsize = (30,20))
<Figure size 3000x2000 with 0 Axes>
plt.show()
plt.figure(figsize = (30,20))
<Figure size 3000x2000 with 0 Axes>
def stockplot():
    plt.plot(close,label= 'close', linewidth = 4)
    plt.plot(ma5,label = '5 window')
    plt.plot(ma10,label = '10 window')
    plt.plot(ma60,label = '60 window')
    plt.plot(ma120,label = '120 window')
    plt.legend()
    plt.title('Rolling window calculations')
    plt.xlabel('Date')
    plt.ylabel('close price')
    plt.show()

    
stckplot()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    stckplot()
NameError: name 'stckplot' is not defined. Did you mean: 'stockplot'?
stockplot()
import matplotlib.dates as mdates
KeyboardInterrupt
def stock_dashboard(df, ticker='005930.KS'):
    if ('Close', ticker) in df.columns:
        close_series = df[('Close', ticker)]
        volume_series = df[('Volume', ticker)]
    elif 'close' in df.columns:
        close_series = df['close']
        volume_series = df['volume'] if 'volume' in df.columns else df['Volume']
    else:
        close_series = df['Close']
        volume_series = df['Volume']
    ma5 = close_series.rolling(window=5).mean()
    ma10 = close_series.rolling(window=10).mean()
    ma60 = close_series.rolling(window=60).mean()
    ma120 = close_series.rolling(window=120).mean()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, 
                                   gridspec_kw={'height_ratios': [3, 1]})
    ax1.plot(df.index, close_series, label='Close Price', linewidth=2.5, color='#1f77b4')
    ax1.plot(df.index, ma5, label='5-Day MA', linewidth=1.2, alpha=0.9)
    ax1.plot(df.index, ma10, label='10-Day MA', linewidth=1.2, alpha=0.9)
    ax1.plot(df.index, ma60, label='60-Day MA', linewidth=1.5, linestyle='--')
    ax1.plot(df.index, ma120, label='120-Day MA', linewidth=1.5, linestyle=':')
    latest_price = close_series.iloc[-1]
    latest_date = df.index[-1].strftime('%Y-%m-%d')
    ax1.set_title(f'Financial Dashboard: {ticker} (As of {latest_date})\n'
                  f'Latest Close: {latest_price:,.2f}', 
                  fontsize=14, fontweight='bold', pad=15)
    ax1.set_ylabel('Price', fontsize=12)
    ax1.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none')
    ax1.grid(True, linestyle='--', alpha=0.5)
    price_diff = close_series.diff().fillna(0)
    colors = ['#2ca02c' if x >= 0 else '#d62728' for x in price_diff]
    
    ax2.bar(df.index, volume_series, color=colors, alpha=0.7, width=1.0, label='Volume')
    ax2.set_ylabel('Volume', fontsize=12)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))
    )
    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    fig.autofmt_xdate() 
    
    plt.tight_layout()
    plt.show()

    
stock_dashboard(sec)
url = "https://ourworldindata.org/fish-and-overfishing"
df1 = pd.read_csv(url, storage_options= {'User-Agent': 'Our World In Data fetch/1.0')
                  
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
df1 = pd.read_csv(url, storage_options= {'User-Agent': 'Our World In Data fetch/1.0'})
                  
print(df.head())
                  
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
print(df1.head())
                  
  <!doctype html><html lang="en" class="js-disabled"><head><meta name="viewport" content="width=device-width  ... type:"archived-page-version"}}]}</script><script>
0                   function setJSEnabled(enabled) {                                                          ...                                               NaN
1        var elem = window.document.documentElement;                                                          ...                                               NaN
2                                     if (enabled) {                                                          ...                                               NaN
3              elem.classList.remove("js-disabled");                                                          ...                                               NaN
4                  elem.classList.add("js-enabled");                                                          ...                                               NaN

[5 rows x 5158 columns]
print(df1.tail)
                                                                                                              

url = "https://ourworldindata.org"
                                                                                                              
df1 = pd.read_csv(url, storage_options={'User-Agent': 'Our World In Data fetch/1.0'})
                                                                                                              
print(df1.head())
                                                                                                              
  <!doctype html><html lang="en" class="js-disabled"><head><meta name="viewport" content="width=device-width  ... grapher-url:"https://ourworldindata.org/explorers/population-and-demography?tab=map&indicator=Natural+population+growth+rate&Sex=Both+sexes&Age=Total&Projection+scenario=None&country=CHN~IND~USA~IDN~PAK~NGA~BRA~JPN"}}]}</script><script>
0                   function setJSEnabled(enabled) {                                                          ...                                                NaN                                                                                                                                                                                          
1        var elem = window.document.documentElement;                                                          ...                                                NaN                                                                                                                                                                                          
2                                     if (enabled) {                                                          ...                                                NaN                                                                                                                                                                                          
3              elem.classList.remove("js-disabled");                                                          ...                                                NaN                                                                                                                                                                                          
4                  elem.classList.add("js-enabled");                                                          ...                                                NaN                                                                                                                                                                                          

[5 rows x 3302 columns]
import requests
url = "https://ourworldindata.org/fish-and-overfishing"
r = requests.get(url)
SyntaxError: multiple statements found while compiling a single statement
url = "https://ourworldindata.org/fish-and-overfishing"
r = requests.get(url)
print(r.text[:500])
<!doctype html><html lang="en" class="js-disabled"><head><meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1"/><title>Fish and Overfishing | Our World in Data</title><meta name="description" content="How are fish stocks changing across the world? How much is overfished?"/><link rel="canonical" href="https://ourworldindata.org/fish-and-overfishing"/><link rel="alternate" type="application/atom+xml" href="/atom.xml?topics=Fish%20%26%20Overfishing" title="Atom feed f
csv_url = "https://ourworldindata.org/grapher/capture-and-aquaculture-production.csv?v=1&csvType=full&useColumnShortNames=true"
df1 = pd.read_csv(csv_url)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    df1 = pd.read_csv(csv_url)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 776, in get_handle
    ioargs = _get_filepath_or_buffer(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 405, in _get_filepath_or_buffer
    with urlopen(req_info) as req:
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 282, in urlopen
    return urllib.request.urlopen(*args, **kwargs)  # noqa: TID251
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 187, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 493, in open
    response = meth(req, response)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 602, in http_response
    response = self.parent.error(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 531, in error
    return self._call_chain(*args)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 464, in _call_chain
    result = func(*args)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 611, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden
df1 = pd.read_csv("https://ourworldindata.org/grapher/capture-and-aquaculture-production.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
df1
            entity code  year  er_fsh_aqua_mt  er_fsh_capt_mt
0      Afghanistan  AFG  1960            0.00          200.00
1      Afghanistan  AFG  1961            0.00          300.00
2      Afghanistan  AFG  1962            0.00          300.00
3      Afghanistan  AFG  1963            0.00          300.00
4      Afghanistan  AFG  1964            0.00          300.00
...            ...  ...   ...             ...             ...
14637     Zimbabwe  ZWE  2019        20356.01       111717.26
14638     Zimbabwe  ZWE  2020        21276.34       103150.56
14639     Zimbabwe  ZWE  2021         5057.82       110194.00
14640     Zimbabwe  ZWE  2022         8353.01       102365.50
14641     Zimbabwe  ZWE  2023         8714.55        92005.00

[14642 rows x 5 columns]
df1.info()
<class 'pandas.DataFrame'>
RangeIndex: 14642 entries, 0 to 14641
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   entity          14642 non-null  str    
 1   code            14642 non-null  str    
 2   year            14642 non-null  int64  
 3   er_fsh_aqua_mt  14493 non-null  float64
 4   er_fsh_capt_mt  14642 non-null  float64
dtypes: float64(2), int64(1), str(2)
memory usage: 572.1 KB
df1.drop(['code'], axis = 1, inplace = True)
df.head()
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
df1.head()
        entity  year  er_fsh_aqua_mt  er_fsh_capt_mt
0  Afghanistan  1960             0.0           200.0
1  Afghanistan  1961             0.0           300.0
2  Afghanistan  1962             0.0           300.0
3  Afghanistan  1963             0.0           300.0
4  Afghanistan  1964             0.0           300.0
df1.isnull().sum()
entity              0
year                0
er_fsh_aqua_mt    149
er_fsh_capt_mt      0
dtype: int64
df1.fillna(0, inplace= True)
            entity  year  er_fsh_aqua_mt  er_fsh_capt_mt
0      Afghanistan  1960            0.00          200.00
1      Afghanistan  1961            0.00          300.00
2      Afghanistan  1962            0.00          300.00
3      Afghanistan  1963            0.00          300.00
4      Afghanistan  1964            0.00          300.00
...            ...   ...             ...             ...
14637     Zimbabwe  2019        20356.01       111717.26
14638     Zimbabwe  2020        21276.34       103150.56
14639     Zimbabwe  2021         5057.82       110194.00
14640     Zimbabwe  2022         8353.01       102365.50
14641     Zimbabwe  2023         8714.55        92005.00

[14642 rows x 4 columns]
df1.isnull().sum()
entity            0
year              0
er_fsh_aqua_mt    0
er_fsh_capt_mt    0
dtype: int64
df1['new_year'] = pd.to_datetime(df1[year].astype(str),format = '%Y')
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    df1['new_year'] = pd.to_datetime(df1[year].astype(str),format = '%Y')
NameError: name 'year' is not defined
df1['Year']
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Year'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    df1['Year']
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Year'
df1['entity']
0        Afghanistan
1        Afghanistan
2        Afghanistan
3        Afghanistan
4        Afghanistan
            ...     
14637       Zimbabwe
14638       Zimbabwe
14639       Zimbabwe
14640       Zimbabwe
14641       Zimbabwe
Name: entity, Length: 14642, dtype: str
df1.info()
<class 'pandas.DataFrame'>
RangeIndex: 14642 entries, 0 to 14641
Data columns (total 4 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   entity          14642 non-null  str    
 1   year            14642 non-null  int64  
 2   er_fsh_aqua_mt  14642 non-null  float64
 3   er_fsh_capt_mt  14642 non-null  float64
dtypes: float64(2), int64(1), str(1)
memory usage: 457.7 KB
df1['new_year'] = pd.to_datetime(df1['year'].astype(str),format = '%Y')
df1.info()
<class 'pandas.DataFrame'>
RangeIndex: 14642 entries, 0 to 14641
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   entity          14642 non-null  str           
 1   year            14642 non-null  int64         
 2   er_fsh_aqua_mt  14642 non-null  float64       
 3   er_fsh_capt_mt  14642 non-null  float64       
 4   new_year        14642 non-null  datetime64[us]
dtypes: datetime64[us](1), float64(2), int64(1), str(1)
memory usage: 572.1 KB
df1.head()
        entity  year  er_fsh_aqua_mt  er_fsh_capt_mt   new_year
0  Afghanistan  1960             0.0           200.0 1960-01-01
1  Afghanistan  1961             0.0           300.0 1961-01-01
2  Afghanistan  1962             0.0           300.0 1962-01-01
3  Afghanistan  1963             0.0           300.0 1963-01-01
4  Afghanistan  1964             0.0           300.0 1964-01-01
df.setindex('new_year', inplace = True)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    df.setindex('new_year', inplace = True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'setindex'. Did you mean: 'set_index'?
df1.setindex('new_year', inplace = True)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    df1.setindex('new_year', inplace = True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'setindex'. Did you mean: 'set_index'?
df1.set_index('new_year', inplace = True)
df1.drop(['year'],axis =1, inplace = True)
df.head()
            DCOILWTICO
N_DATE                
2021-06-15       72.06
2021-06-16       72.03
2021-06-17       71.06
2021-06-18       71.64
2021-06-21       73.64
df1.head()
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
1960-01-01  Afghanistan             0.0           200.0
1961-01-01  Afghanistan             0.0           300.0
1962-01-01  Afghanistan             0.0           300.0
1963-01-01  Afghanistan             0.0           300.0
1964-01-01  Afghanistan             0.0           300.0
df.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 1305 entries, 2021-06-15 to 2026-06-15
Data columns (total 1 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   DCOILWTICO  1249 non-null   float64
dtypes: float64(1)
memory usage: 52.7 KB
new_df = df1.sort_index()
new_df.head()
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1960-01-01                 Afghanistan             0.0           200.0
1960-01-01                        Fiji             0.0          3000.0
1960-01-01                    Malaysia          7841.0        147800.0
1960-01-01                   Indonesia         80639.0        681087.0
1960-01-01  East Asia and Pacific (WB)       1566799.0      11501285.0
new_df['entity'] = new_df['Entity'].astype('category')
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Entity'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    new_df['entity'] = new_df['Entity'].astype('category')
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Entity'
new_df['entity'] = new_df['entity'].astype('category')
new_df.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 14642 entries, 1960-01-01 to 2023-01-01
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype   
---  ------          --------------  -----   
 0   entity          14642 non-null  category
 1   er_fsh_aqua_mt  14642 non-null  float64 
 2   er_fsh_capt_mt  14642 non-null  float64 
dtypes: category(1), float64(2)
memory usage: 373.6 KB
new_df['entity'].value_counts()
entity
Afghanistan                      64
Albania                          64
Algeria                          64
American Samoa                   64
Andorra                          64
                                 ..
North America (WB)               63
South Asia (WB)                  63
Sub-Saharan Africa (WB)          63
Upper-middle-income countries    63
World                            63
Name: count, Length: 229, dtype: int64
g= new_df.groupby(['new_year'])
g.head()
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1960-01-01                 Afghanistan           0.000          200.00
1960-01-01                        Fiji           0.000         3000.00
1960-01-01                    Malaysia        7841.000       147800.00
1960-01-01                   Indonesia       80639.000       681087.00
1960-01-01  East Asia and Pacific (WB)     1566799.000     11501285.00
...                                ...             ...             ...
2023-01-01                      Malawi        4780.000       212817.86
2023-01-01                    Honduras      102768.000        20300.00
2023-01-01                        Laos      140000.000        73150.00
2023-01-01                      Jordan        2719.400          655.00
2023-01-01                       Malta       20833.295         2013.59

[320 rows x 3 columns]
for key,group in g:
    print('+key:',key)
    print('+number:',len(group))
    print(group.head())
    print('\n')

    
+key: (Timestamp('1960-01-01 00:00:00'),)
+number: 229
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1960-01-01                 Afghanistan             0.0           200.0
1960-01-01                        Fiji             0.0          3000.0
1960-01-01                    Malaysia          7841.0        147800.0
1960-01-01                   Indonesia         80639.0        681087.0
1960-01-01  East Asia and Pacific (WB)       1566799.0      11501285.0


+key: (Timestamp('1961-01-01 00:00:00'),)
+number: 229
                   entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                 
1961-01-01        Vanuatu             0.0          1400.0
1961-01-01       Tanzania             0.0         73100.0
1961-01-01          Italy          4776.0        240430.0
1961-01-01  Guinea-Bissau             0.0           700.0
1961-01-01        Moldova             0.0             0.0


+key: (Timestamp('1962-01-01 00:00:00'),)
+number: 229
                       entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                     
1962-01-01         Seychelles             0.0          2000.0
1962-01-01        Philippines         62314.0        467367.0
1962-01-01  Equatorial Guinea             0.0           800.0
1962-01-01            Eritrea             0.0             0.0
1962-01-01             Canada          3100.0       1287603.0


+key: (Timestamp('1963-01-01 00:00:00'),)
+number: 229
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1963-01-01       Sao Tome and Principe             0.0           500.0
1963-01-01                    Cameroon             0.0         59400.0
1963-01-01                       Niger             0.0          9000.0
1963-01-01  East Asia and Pacific (WB)       1683131.0      13136281.0
1963-01-01                      Guyana             0.0          9200.0


+key: (Timestamp('1964-01-01 00:00:00'),)
+number: 229
                                   entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                 
1964-01-01                        Bolivia             0.0          1900.0
1964-01-01                    Philippines         63885.0        582491.0
1964-01-01  Upper-middle-income countries       1172241.0      15578319.0
1964-01-01                     San Marino             0.0             0.0
1964-01-01                        Albania             0.0          3000.0


+key: (Timestamp('1965-01-01 00:00:00'),)
+number: 229
                  entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                
1965-01-01        Monaco             0.0             0.0
1965-01-01  Saudi Arabia             0.0         18600.0
1965-01-01       Estonia             0.0             0.0
1965-01-01      Eswatini             0.0             0.0
1965-01-01      Bulgaria          5100.0         16083.0


+key: (Timestamp('1966-01-01 00:00:00'),)
+number: 229
                              entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                            
1966-01-01              Burkina Faso             0.0          4000.0
1966-01-01                   Estonia             0.0             0.0
1966-01-01  Central African Republic             0.0          4000.0
1966-01-01                   Comoros             0.0           875.0
1966-01-01                 Guatemala             0.0          3000.0


+key: (Timestamp('1967-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
1967-01-01   Cape Verde             0.0          5900.0
1967-01-01  Puerto Rico             0.0          2500.0
1967-01-01      Tunisia             0.0         28207.0
1967-01-01      Vanuatu             0.0          1800.0
1967-01-01  South Korea         96450.0        663787.0


+key: (Timestamp('1968-01-01 00:00:00'),)
+number: 229
                             entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                           
1968-01-01  Sub-Saharan Africa (WB)          3771.0       3711837.0
1968-01-01                 Eswatini             0.0            50.0
1968-01-01               Kyrgyzstan             0.0             0.0
1968-01-01                  Czechia             0.0             0.0
1968-01-01          Solomon Islands             0.0          7400.0


+key: (Timestamp('1969-01-01 00:00:00'),)
+number: 229
                    entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                  
1969-01-01     South Sudan             0.0             0.0
1969-01-01     Netherlands        105900.0        217300.0
1969-01-01         Vietnam         62440.0        703310.0
1969-01-01  Cayman Islands             0.0             0.0
1969-01-01      Kyrgyzstan             0.0             0.0


+key: (Timestamp('1970-01-01 00:00:00'),)
+number: 229
                  entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                
1970-01-01         Congo             0.0         14399.0
1970-01-01      Slovakia             0.0             0.0
1970-01-01  Sierra Leone             0.0         31050.0
1970-01-01       Czechia             0.0             0.0
1970-01-01       Comoros             0.0          1661.0


+key: (Timestamp('1971-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1971-01-01    Zimbabwe             0.0          2500.0
1971-01-01    Djibouti             0.0           300.0
1971-01-01       Samoa             0.0           900.0
1971-01-01  Uzbekistan             0.0             0.0
1971-01-01      Kuwait             0.0          5700.0


+key: (Timestamp('1972-01-01 00:00:00'),)
+number: 229
                       entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                     
1972-01-01              Samoa             0.0           900.0
1972-01-01              Egypt          8000.0         71209.0
1972-01-01  Equatorial Guinea             0.0          4000.0
1972-01-01           Pakistan          2900.0        193162.0
1972-01-01             Cyprus             0.0          1340.0


+key: (Timestamp('1973-01-01 00:00:00'),)
+number: 229
                          entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                        
1973-01-01  United Arab Emirates             0.0         43000.0
1973-01-01                  Iran           311.0         19949.0
1973-01-01                Malawi             0.0         69300.0
1973-01-01              Maldives             0.0         35706.0
1973-01-01               Ukraine             0.0             0.0


+key: (Timestamp('1974-01-01 00:00:00'),)
+number: 229
                           entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                         
1974-01-01                Czechia             0.0             0.0
1974-01-01             East Timor             0.0             0.0
1974-01-01                 Russia             0.0             0.0
1974-01-01                Romania         33544.0         95909.0
1974-01-01  Saint Kitts and Nevis             0.0          1000.0


+key: (Timestamp('1975-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1975-01-01  Kyrgyzstan             0.0             0.0
1975-01-01       Macao             0.0          6000.0
1975-01-01        Iraq          2300.0         19532.0
1975-01-01     Liberia             0.0         10046.0
1975-01-01       Libya             0.0          4949.0


+key: (Timestamp('1976-01-01 00:00:00'),)
+number: 229
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1976-01-01                    Paraguay             0.0          2900.0
1976-01-01  Saint Martin (French part)             0.0             0.0
1976-01-01                      Guinea             0.0          9920.0
1976-01-01                      Cyprus            31.0          1052.0
1976-01-01                     Nigeria          5087.0        255498.0


+key: (Timestamp('1977-01-01 00:00:00'),)
+number: 229
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1977-01-01                       Macao             0.0          7160.0
1977-01-01                     Austria          1600.0           870.0
1977-01-01  East Asia and Pacific (WB)       5232586.5      23686264.0
1977-01-01                        Iraq          3000.0         23101.0
1977-01-01                     Algeria             0.0         43475.0


+key: (Timestamp('1978-01-01 00:00:00'),)
+number: 229
                                  entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                
1978-01-01      Central African Republic            47.0         13000.0
1978-01-01                          Chad             0.0         75000.0
1978-01-01                        France        163893.0        695965.3
1978-01-01  Europe and Central Asia (WB)        732189.0      12592808.0
1978-01-01                      Ethiopia             0.0          2515.0


+key: (Timestamp('1979-01-01 00:00:00'),)
+number: 229
                                      entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                    
1979-01-01                           Lebanon            25.0          1650.0
1979-01-01                           Morocco            91.0        290355.7
1979-01-01                            Poland          9932.0        589349.0
1979-01-01                       North Korea        297961.0        914000.0
1979-01-01  Saint Vincent and the Grenadines             0.0           547.0


+key: (Timestamp('1980-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
1980-01-01  Puerto Rico             0.0          2557.0
1980-01-01       Poland          9636.0        630783.0
1980-01-01       Latvia             0.0             0.0
1980-01-01        Nauru             0.0           140.0
1980-01-01       Sweden           822.0        232694.0


+key: (Timestamp('1981-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
1981-01-01     Maldives             0.0       40916.000
1981-01-01      Bahamas             0.0        7631.789
1981-01-01      Germany         35543.0      549483.000
1981-01-01       Belize             0.0        2252.000
1981-01-01  Afghanistan           170.0         700.000


+key: (Timestamp('1982-01-01 00:00:00'),)
+number: 229
                     entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                   
1982-01-01  North Macedonia             0.0             0.0
1982-01-01       Mauritania             0.0         56288.0
1982-01-01             Mali             0.0         73451.0
1982-01-01           Norway         15329.0       2706242.0
1982-01-01          Belgium           203.0         47841.0


+key: (Timestamp('1983-01-01 00:00:00'),)
+number: 229
                       entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                     
1983-01-01               Cuba          4145.0        194349.0
1983-01-01  Equatorial Guinea             0.0          2341.0
1983-01-01            Burundi             0.0         11366.0
1983-01-01      New Caledonia            16.0          2958.0
1983-01-01            Georgia             0.0             0.0


+key: (Timestamp('1984-01-01 00:00:00'),)
+number: 229
                           entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                         
1984-01-01                  Tonga             0.0          2385.0
1984-01-01  High-income countries       3417958.5      39111340.0
1984-01-01          Faroe Islands           513.0        348760.0
1984-01-01                   Oman             0.0        105200.0
1984-01-01                Myanmar          3951.0        609740.0


+key: (Timestamp('1985-01-01 00:00:00'),)
+number: 229
                                      entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                    
1985-01-01  Saint Vincent and the Grenadines             0.0           483.0
1985-01-01                           Eritrea             0.0             0.0
1985-01-01                              Iraq          4441.0         17000.0
1985-01-01                         Palestine             0.0             0.0
1985-01-01              Low-income countries        749009.0       1574855.1


+key: (Timestamp('1986-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1986-01-01      Guinea             2.0         33000.0
1986-01-01  Montenegro             0.0             0.0
1986-01-01     Croatia             0.0             0.0
1986-01-01       Chile          9941.0       5685596.0
1986-01-01     Andorra             0.0             0.0


+key: (Timestamp('1987-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1987-01-01       Syria          1982.0         3399.66
1987-01-01     Algeria           274.0        94093.80
1987-01-01       China       6325967.0      5407952.00
1987-01-01  Cape Verde             0.0         7312.00
1987-01-01    Slovakia             0.0            0.00


+key: (Timestamp('1988-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
1988-01-01         Peru          4958.0       6637579.0
1988-01-01      Ecuador         75631.0        800393.0
1988-01-01  Saint Lucia            35.0           791.0
1988-01-01        Niger            20.0          2479.0
1988-01-01    Mauritius            73.0         17117.0


+key: (Timestamp('1989-01-01 00:00:00'),)
+number: 229
                    entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                  
1989-01-01          Latvia             0.0             0.0
1989-01-01  Cayman Islands             0.0           615.0
1989-01-01        Zimbabwe           160.0         35447.0
1989-01-01      Kyrgyzstan             0.0             0.0
1989-01-01          Rwanda            44.0          1472.0


+key: (Timestamp('1990-01-01 00:00:00'),)
+number: 229
                           entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                         
1990-01-01  Sao Tome and Principe             0.0        3867.000
1990-01-01        Solomon Islands             5.0       41404.355
1990-01-01                 Uganda            52.0      245223.000
1990-01-01             Madagascar           280.0      105600.000
1990-01-01                Somalia             0.0       23195.000


+key: (Timestamp('1991-01-01 00:00:00'),)
+number: 229
                                  entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                
1991-01-01  United States Virgin Islands             0.0           904.0
1991-01-01                      Dominica             0.0           552.0
1991-01-01                         Macao             0.0          2322.0
1991-01-01                      Bulgaria          7798.0         50056.0
1991-01-01                         Qatar             0.0          8136.0


+key: (Timestamp('1992-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1992-01-01  Costa Rica          2244.0       16010.000
1992-01-01      Cyprus           155.0        9336.000
1992-01-01    Slovakia             0.0           0.000
1992-01-01     Bahamas            10.0       12205.532
1992-01-01      Bhutan            35.0          90.000


+key: (Timestamp('1993-01-01 00:00:00'),)
+number: 229
                                   entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                 
1993-01-01                     East Timor             0.0             0.0
1993-01-01         British Virgin Islands             0.0           343.0
1993-01-01  Lower-middle-income countries       2860322.0      12161501.0
1993-01-01                        Estonia           330.0        147185.0
1993-01-01                        Ecuador         87763.0        290394.0


+key: (Timestamp('1994-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1994-01-01  Mauritania             0.0         53746.0
1994-01-01       Qatar             0.0          5086.0
1994-01-01   Guatemala          4393.0          7211.0
1994-01-01     Denmark         42892.0       1877765.0
1994-01-01    Botswana             0.0           987.0


+key: (Timestamp('1995-01-01 00:00:00'),)
+number: 229
                                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                              
1995-01-01  Saint Martin (French part)             0.0             0.0
1995-01-01                       Yemen             0.0        107970.0
1995-01-01                 North Korea        738317.0        327083.0
1995-01-01                    Slovenia           789.0          2167.0
1995-01-01                      Guinea             4.0         67960.0


+key: (Timestamp('1996-01-01 00:00:00'),)
+number: 229
                      entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                    
1996-01-01  Papua New Guinea            38.0       62840.445
1996-01-01             Syria          6355.0        5773.000
1996-01-01            Guinea             4.0       63360.000
1996-01-01           Eritrea             0.0        3252.000
1996-01-01          Botswana             0.0         428.000


+key: (Timestamp('1997-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
1997-01-01       Russia         59766.0       4738463.0
1997-01-01  South Korea       1040210.0       2227947.0
1997-01-01       Malawi           231.0         56740.0
1997-01-01     Slovakia          1254.0          1364.0
1997-01-01     Cambodia         11800.0        119800.0


+key: (Timestamp('1998-01-01 00:00:00'),)
+number: 229
                                   entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                 
1998-01-01                          Macao             0.0          1500.0
1998-01-01                        Bolivia           385.0          7812.0
1998-01-01                    Isle of Man             0.0          2214.0
1998-01-01                         Brazil        103915.0        609021.0
1998-01-01  Lower-middle-income countries       4230820.0      13657528.0


+key: (Timestamp('1999-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
1999-01-01     Ukraine         33816.0        408881.0
1999-01-01     Estonia           200.0        113112.0
1999-01-01  Kyrgyzstan            71.0            48.0
1999-01-01      Canada        112916.0       1277027.0
1999-01-01   Palestine             0.0          3650.0


+key: (Timestamp('2000-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
2000-01-01       Yemen             0.0        114750.0
2000-01-01    Maldives             0.0        119373.0
2000-01-01  Costa Rica          9708.0         35163.0
2000-01-01   Mauritius            87.0          9615.0
2000-01-01   Sri Lanka          4420.0        296749.6


+key: (Timestamp('2001-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
2001-01-01  North Korea        508095.0        206500.0
2001-01-01       Panama          3127.0        288469.0
2001-01-01      Iceland          4371.0       2003941.0
2001-01-01      Bermuda             0.0           309.0
2001-01-01        Nepal         16570.0         16700.0


+key: (Timestamp('2002-01-01 00:00:00'),)
+number: 229
                     entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                   
2002-01-01         Botswana             0.0          139.00
2002-01-01       Tajikistan           143.0          181.00
2002-01-01            Kenya           798.0       149131.33
2002-01-01  South Asia (WB)       2995830.0      5342020.00
2002-01-01           Angola            51.0       255443.00


+key: (Timestamp('2003-01-01 00:00:00'),)
+number: 229
              entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                            
2003-01-01    Panama          6228.0        244808.0
2003-01-01   Finland         12558.0        122107.0
2003-01-01   Czechia         19670.0          5127.0
2003-01-01  Malaysia        192160.0       1291428.0
2003-01-01      Oman           352.0        138482.0


+key: (Timestamp('2004-01-01 00:00:00'),)
+number: 229
                                  entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                
2004-01-01         Saint Kitts and Nevis             1.0          1111.0
2004-01-01                   Puerto Rico           457.0          3342.0
2004-01-01                      Slovenia          1571.0          1023.0
2004-01-01                        Russia        110018.0       2968363.0
2004-01-01  Democratic Republic of Congo          2965.0        235752.0


+key: (Timestamp('2005-01-01 00:00:00'),)
+number: 229
                                   entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                 
2005-01-01                        Bolivia           430.0         57690.0
2005-01-01                   Sierra Leone            30.0        142993.0
2005-01-01                       Zimbabwe          2502.0         79794.0
2005-01-01                       Mongolia             0.0           366.0
2005-01-01  Upper-middle-income countries      43568640.0      39467430.0


+key: (Timestamp('2006-01-01 00:00:00'),)
+number: 229
                                   entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                 
2006-01-01                        Bahamas            52.0         16242.0
2006-01-01                         Bhutan            40.0            20.0
2006-01-01            European Union (27)       1142515.2       5183653.0
2006-01-01                  Liechtenstein             0.0             0.0
2006-01-01  Lower-middle-income countries       9525742.0      17710218.0


+key: (Timestamp('2007-01-01 00:00:00'),)
+number: 229
                                  entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                                
2007-01-01                     Indonesia       3137376.0       5060086.0
2007-01-01                     Argentina          2957.0        992618.0
2007-01-01  Democratic Republic of Congo          3020.5        234252.0
2007-01-01                        Malawi          1500.0         67787.0
2007-01-01                 Cote d'Ivoire          1290.0         47300.0


+key: (Timestamp('2008-01-01 00:00:00'),)
+number: 229
                        entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                      
2008-01-01            Paraguay          2450.0         19400.0
2008-01-01           Venezuela         18762.6        311055.0
2008-01-01  North America (WB)        656875.0       5342329.0
2008-01-01             Morocco           579.0       1006167.7
2008-01-01            Mongolia             0.0            88.0


+key: (Timestamp('2009-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
2009-01-01     Comoros             0.0         44745.0
2009-01-01       Tonga           300.2          1955.0
2009-01-01   Singapore          3567.0          3207.0
2009-01-01  Cape Verde             0.0         19213.0
2009-01-01     Bolivia           847.0         35453.0


+key: (Timestamp('2010-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
2010-01-01  Afghanistan          2250.0          1000.0
2010-01-01     Dominica            11.0           700.0
2010-01-01     Honduras         27509.0         12078.0
2010-01-01      Lebanon          1180.0          3400.0
2010-01-01        Qatar            36.0         13760.0


+key: (Timestamp('2011-01-01 00:00:00'),)
+number: 229
                               entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                             
2011-01-01  Sint Maarten (Dutch part)             0.0          253.00
2011-01-01                 Bangladesh       1523759.0      1600918.00
2011-01-01                      Libya            10.0        30004.00
2011-01-01                South Sudan             0.0            0.00
2011-01-01           Marshall Islands             0.0        93318.45


+key: (Timestamp('2012-01-01 00:00:00'),)
+number: 229
                         entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                       
2012-01-01  Antigua and Barbuda           18.00         5951.00
2012-01-01              Andorra            0.00            0.00
2012-01-01                Ghana        27450.00       356346.60
2012-01-01              Namibia          679.35       528079.94
2012-01-01            Lithuania         3581.96        66970.00


+key: (Timestamp('2013-01-01 00:00:00'),)
+number: 229
                 entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                               
2013-01-01    Nicaragua         26406.9         40979.0
2013-01-01   Costa Rica         30352.0         18558.0
2013-01-01  South Korea       1533446.0       1607232.2
2013-01-01      Senegal           706.8        469595.6
2013-01-01   East Timor          1229.0          3580.0


+key: (Timestamp('2014-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
2014-01-01       Chile      1227359.00       2592748.5
2014-01-01      Mexico       194229.77       1531398.6
2014-01-01      Brunei          711.07          3186.0
2014-01-01     Tunisia        11663.00        114520.0
2014-01-01  Uzbekistan        29275.40         17116.0


+key: (Timestamp('2015-01-01 00:00:00'),)
+number: 229
                         entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                       
2015-01-01               Belize          4206.0        97524.24
2015-01-01        Faroe Islands         80622.0       586067.00
2015-01-01  Antigua and Barbuda            20.0         3165.00
2015-01-01              Senegal          1212.5       425449.12
2015-01-01        United States        426111.0      5419913.00


+key: (Timestamp('2016-01-01 00:00:00'),)
+number: 229
             entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                           
2016-01-01  Morocco         1150.10      1472314.40
2016-01-01   Turkey       253395.00       335324.60
2016-01-01    Syria         2500.00         4179.00
2016-01-01   Malawi         7646.39       164949.00
2016-01-01     Iran       398129.00       688903.56


+key: (Timestamp('2017-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
2017-01-01    Cameroon        5000.000        261741.0
2017-01-01  Bangladesh     2333402.000       1801084.0
2017-01-01    Djibouti           0.000          2022.0
2017-01-01        Oman          77.248        347539.0
2017-01-01      Uganda      112343.600        389629.0


+key: (Timestamp('2018-01-01 00:00:00'),)
+number: 229
                entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                              
2018-01-01     Iceland        19185.00      1279652.00
2018-01-01  Bangladesh      2405516.00      1871225.00
2018-01-01    Malaysia       391977.47      1468401.40
2018-01-01     Tunisia        21826.20       105959.27
2018-01-01     Curacao            0.50        37863.48


+key: (Timestamp('2019-01-01 00:00:00'),)
+number: 229
                          entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                        
2019-01-01            Uzbekistan        81717.00        40000.00
2019-01-01                Kuwait          467.84         3016.00
2019-01-01                Angola         1934.00       401013.00
2019-01-01  Low-income countries       846054.75      2687960.80
2019-01-01              Zimbabwe        20356.01       111717.26


+key: (Timestamp('2020-01-01 00:00:00'),)
+number: 229
                             entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                           
2020-01-01                 Djibouti            0.00        2322.500
2020-01-01                  Nigeria       261710.72      783101.700
2020-01-01  Sub-Saharan Africa (WB)       727143.75     7335958.000
2020-01-01                    Libya           10.00       31803.545
2020-01-01                    Niger          649.00       46000.000


+key: (Timestamp('2021-01-01 00:00:00'),)
+number: 229
                               entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                                             
2021-01-01                   Dominica           1.500          287.97
2021-01-01                  Singapore        5243.564         2142.32
2021-01-01  Sint Maarten (Dutch part)           0.000          253.00
2021-01-01                    Ecuador      904136.300       863105.75
2021-01-01                   Paraguay       14150.000        17560.00


+key: (Timestamp('2022-01-01 00:00:00'),)
+number: 229
               entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                             
2022-01-01    Vanuatu             4.0        84915.34
2022-01-01      Yemen            10.0       150470.00
2022-01-01    Albania          8908.0         8891.50
2022-01-01  Venezuela         67531.0       211939.58
2022-01-01    Algeria          5208.0        80790.00


+key: (Timestamp('2023-01-01 00:00:00'),)
+number: 215
              entity  er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                            
2023-01-01    Malawi        4780.000       212817.86
2023-01-01  Honduras      102768.000        20300.00
2023-01-01      Laos      140000.000        73150.00
2023-01-01    Jordan        2719.400          655.00
2023-01-01     Malta       20833.295         2013.59


world_total = g.sum(numeric_only = True)
world_total.head()
            er_fsh_aqua_mt  er_fsh_capt_mt
new_year                                  
1960-01-01       8402457.0     131212776.0
1961-01-01       8044319.0     145950928.0
1962-01-01       8400755.0     158218161.0
1963-01-01       9396196.0     160917892.1
1964-01-01      10160024.0     177513084.1
plt.style.use('ggplot')
world_total.plot(kind = 'area', alpha = 0.2, stacked= False, figsize = (20,10))
<Axes: xlabel='new_year'>
plt.legend()
<matplotlib.legend.Legend object at 0x00000193D0BE0980>
plt.show()
country = new_df['entity'].value_counts()
print(country)
entity
Afghanistan                      64
Albania                          64
Algeria                          64
American Samoa                   64
Andorra                          64
                                 ..
North America (WB)               63
South Asia (WB)                  63
Sub-Saharan Africa (WB)          63
Upper-middle-income countries    63
World                            63
Name: count, Length: 229, dtype: int64
country
entity
Afghanistan                      64
Albania                          64
Algeria                          64
American Samoa                   64
Andorra                          64
                                 ..
North America (WB)               63
South Asia (WB)                  63
Sub-Saharan Africa (WB)          63
Upper-middle-income countries    63
World                            63
Name: count, Length: 229, dtype: int64
print("DataTypes =>",type(country))
DataTypes => <class 'pandas.Series'>
'South Korea' in country
True
s= new_df.loc[new_df['Entity'] == 'South Korea']
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Entity'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    s= new_df.loc[new_df['Entity'] == 'South Korea']
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Entity'
s= new_df.loc[new_df['entity'] == 'South Korea']
c= new_df.loc[new_df['entity'] == 'China']
a= new_df.loc[new_df['entity'] == 'Afghanistan']
new_df.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 14642 entries, 1960-01-01 to 2023-01-01
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype   
---  ------          --------------  -----   
 0   entity          14642 non-null  category
 1   er_fsh_aqua_mt  14642 non-null  float64 
 2   er_fsh_capt_mt  14642 non-null  float64 
dtypes: category(1), float64(2)
memory usage: 381.7 KB
sy = s[['er_fsh_aqua_mt','er_fsh_capt_mt']]
sx = s.index
cy = c[['er_fsh_aqua_mt','er_fsh_capt_mt']]
cx =c.index
ay = a[['er_fsh_aqua_mt','er_fsh_capt_mt']]
ax = a.index
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1,3, figsize = (15,5))
axs[0].plot(sx,sy)
[<matplotlib.lines.Line2D object at 0x00000193D0F5DFD0>, <matplotlib.lines.Line2D object at 0x00000193D0F5E120>]
axs[1].plot(cx,cy)
[<matplotlib.lines.Line2D object at 0x00000193D0F5E270>, <matplotlib.lines.Line2D object at 0x00000193D0F5E3C0>]
axs[2].plot(ax,ay)
[<matplotlib.lines.Line2D object at 0x00000193D0F5E510>, <matplotlib.lines.Line2D object at 0x00000193D0F5E660>]
fig.suptitle('Fish Production')
Text(0.5, 0.98, 'Fish Production')
fig.show()
path
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    path
NameError: name 'path' is not defined
path = r"C:\Users\Lenovo\Documents\Day9"
df.write_csv(path)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    df.write_csv(path)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'write_csv'
pd.write_csv(df,path)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    pd.write_csv(df,path)
AttributeError: module 'pandas' has no attribute 'write_csv'
path = r"C:\Users\Lenovo\Documents\Day9\df.csv"
df.to_csv(path)
path = r"C:\Users\Lenovo\Documents\Day9\df2.csv"
df1.to_csv(path, index= False)
path = r"C:\Users\Lenovo\Documents\Day9\new_df.csv"
dir()
['Ls', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'ax', 'axs', 'ay', 'c', 'close', 'country', 'csv_url', 'cx', 'cy', 'date', 'datetime', 'df', 'df1', 'end', 'fig', 'g', 'group', 'i', 'key', 'ma10', 'ma120', 'ma5', 'ma60', 'mdates', 'new_df', 'p_data', 'path', 'pd', 'plt', 'r', 'requests', 's', 'sec', 'start', 'stock_dashboard', 'stockplot', 'sx', 'sy', 'time', 'url', 'world_total', 'wti', 'yf']
dir(DataFrames)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    dir(DataFrames)
NameError: name 'DataFrames' is not defined
dir(functions)
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    dir(functions)
NameError: name 'functions' is not defined
a

ax

axs

ay

type(a,ax)
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    type(a,ax)
TypeError: type() takes 1 or 3 arguments
for i in range(len(dir())):
    name = input("Enter a variable name to check (or type 'exit'): ").strip()
    if name.upper() == 'exit':
        break
    if name in globals():
        actual_variable = globals()[name]
        print(f"-> The data type of '{name}' is: {type(actual_variable)}\n")
    else:
        print(f"'{name}' is not defined in your workspace.\n")

        
Enter a variable name to check (or type 'exit'): a
-> The data type of 'a' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): ax
-> The data type of 'ax' is: <class 'pandas.DatetimeIndex'>

Enter a variable name to check (or type 'exit'): axs
-> The data type of 'axs' is: <class 'numpy.ndarray'>

Enter a variable name to check (or type 'exit'): ay
-> The data type of 'ay' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): c
-> The data type of 'c' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): close
-> The data type of 'close' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): country
-> The data type of 'country' is: <class 'pandas.Series'>

Enter a variable name to check (or type 'exit'): csv_url
-> The data type of 'csv_url' is: <class 'str'>

Enter a variable name to check (or type 'exit'): cx
-> The data type of 'cx' is: <class 'pandas.DatetimeIndex'>

Enter a variable name to check (or type 'exit'): cy
-> The data type of 'cy' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): date
-> The data type of 'date' is: <class 'type'>

Enter a variable name to check (or type 'exit'): datetime
-> The data type of 'datetime' is: <class 'type'>

Enter a variable name to check (or type 'exit'): df
-> The data type of 'df' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): df1
-> The data type of 'df1' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): end
-> The data type of 'end' is: <class 'datetime.datetime'>

Enter a variable name to check (or type 'exit'): fig
-> The data type of 'fig' is: <class 'matplotlib.figure.Figure'>

Enter a variable name to check (or type 'exit'): g
-> The data type of 'g' is: <class 'pandas.api.typing.DataFrameGroupBy'>

Enter a variable name to check (or type 'exit'): group
-> The data type of 'group' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): i
-> The data type of 'i' is: <class 'int'>

Enter a variable name to check (or type 'exit'): key
-> The data type of 'key' is: <class 'tuple'>

Enter a variable name to check (or type 'exit'): ma10
-> The data type of 'ma10' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): ma120
-> The data type of 'ma120' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): ma5
-> The data type of 'ma5' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): ma60
-> The data type of 'ma60' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): mdates
-> The data type of 'mdates' is: <class 'module'>

Enter a variable name to check (or type 'exit'): new_df
-> The data type of 'new_df' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): p_data
-> The data type of 'p_data' is: <class 'pandas.PeriodIndex'>

Enter a variable name to check (or type 'exit'): path
-> The data type of 'path' is: <class 'str'>

Enter a variable name to check (or type 'exit'): pd
-> The data type of 'pd' is: <class 'module'>

Enter a variable name to check (or type 'exit'): plt
-> The data type of 'plt' is: <class 'module'>

Enter a variable name to check (or type 'exit'): r
-> The data type of 'r' is: <class 'requests.models.Response'>

Enter a variable name to check (or type 'exit'): requests
-> The data type of 'requests' is: <class 'module'>

Enter a variable name to check (or type 'exit'): s
-> The data type of 's' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): sec
-> The data type of 'sec' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): start
-> The data type of 'start' is: <class 'datetime.datetime'>

Enter a variable name to check (or type 'exit'): stock_dashboard
-> The data type of 'stock_dashboard' is: <class 'function'>

Enter a variable name to check (or type 'exit'): stockplot
-> The data type of 'stockplot' is: <class 'function'>

Enter a variable name to check (or type 'exit'): sx
-> The data type of 'sx' is: <class 'pandas.DatetimeIndex'>

Enter a variable name to check (or type 'exit'): sy
-> The data type of 'sy' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): time
-> The data type of 'time' is: <class 'type'>

Enter a variable name to check (or type 'exit'): url
-> The data type of 'url' is: <class 'str'>

Enter a variable name to check (or type 'exit'): world_total
-> The data type of 'world_total' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): wti
-> The data type of 'wti' is: <class 'pandas.DataFrame'>

Enter a variable name to check (or type 'exit'): yf
-> The data type of 'yf' is: <class 'module'>

Enter a variable name to check (or type 'exit'): exit
'exit' is not defined in your workspace.

Enter a variable name to check (or type 'exit'): EXIT
'EXIT' is not defined in your workspace.

Enter a variable name to check (or type 'exit'): 
>>> Traceback (most recent call last):
>>>   File "<pyshell#232>", line 2, in <module>
>>>     name = input("Enter a variable name to check (or type 'exit'): ").strip()
>>> KeyboardInterrupt
... import os
... output_folder = r"C:\Users\Lenovo\Documents\Day9"
... os.makedirs(output_folder, exist_ok=True)
... for name, obj in list(globals().items()):
...     if not name.startswith('_') and isinstance(obj, pd.DataFrame):
...         file_path = os.path.join(output_folder, f"{name}.csv")
        obj.to_csv(file_path, index=True)
        print(f"Saved: {file_path} ({obj.shape[0]} rows, {obj.shape[1]} columns)")

        
Saved: C:\Users\Lenovo\Documents\Day9\wti.csv (1305 rows, 3 columns)
Saved: C:\Users\Lenovo\Documents\Day9\df.csv (1305 rows, 1 columns)
Saved: C:\Users\Lenovo\Documents\Day9\sec.csv (1585 rows, 5 columns)
Saved: C:\Users\Lenovo\Documents\Day9\ma5.csv (1585 rows, 1 columns)
Saved: C:\Users\Lenovo\Documents\Day9\close.csv (1585 rows, 1 columns)
Saved: C:\Users\Lenovo\Documents\Day9\ma10.csv (1585 rows, 1 columns)
Saved: C:\Users\Lenovo\Documents\Day9\ma60.csv (1585 rows, 1 columns)
Saved: C:\Users\Lenovo\Documents\Day9\ma120.csv (1585 rows, 1 columns)
Saved: C:\Users\Lenovo\Documents\Day9\df1.csv (14642 rows, 3 columns)
Saved: C:\Users\Lenovo\Documents\Day9\new_df.csv (14642 rows, 3 columns)
Saved: C:\Users\Lenovo\Documents\Day9\group.csv (215 rows, 3 columns)
Saved: C:\Users\Lenovo\Documents\Day9\world_total.csv (64 rows, 2 columns)
Saved: C:\Users\Lenovo\Documents\Day9\s.csv (64 rows, 3 columns)
Saved: C:\Users\Lenovo\Documents\Day9\c.csv (64 rows, 3 columns)
>>> Saved: C:\Users\Lenovo\Documents\Day9\a.csv (64 rows, 3 columns)
>>> Saved: C:\Users\Lenovo\Documents\Day9\sy.csv (64 rows, 2 columns)
... Saved: C:\Users\Lenovo\Documents\Day9\cy.csv (64 rows, 2 columns)
... Saved: C:\Users\Lenovo\Documents\Day9\ay.csv (64 rows, 2 columns)
... config_path = r"C:\Users\Lenovo\Documents\Day9\session_variables.txt"
... with open(config_path, "w", encoding="utf-8") as f:
...     for name, obj in list(globals().items()):
        if not name.startswith('_') and type(obj).__name__ in ['str', 'datetime', 'int', 'float', 'tuple']:
>>>             f.write(f"{name} = {obj}\n")
>>> 
... print(f"Text variables archived to: {config_path}")
... SyntaxError: invalid syntax
... 
... with open(config_path, "w", encoding="utf-8") as f:
...     for name, obj in list(globals().items()):
        if not name.startswith('_') and type(obj).__name__ in ['str', 'datetime', 'int', 'float', 'tuple']:
            f.write(f"{name} = {obj}\n")

            
7
335756
28
26
54
126
42
49
21
