Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone, time, date
def get_stockdata(ticker,start,end):
    data = yf.download(tickers=[ticker],start = start, end = end)
    data.insert(0,ticker)
    df = yf.download(')
                     
SyntaxError: unterminated string literal (detected at line 4)
 df = yf.download('SPY', datetime(2025,5,25), datetime.today())
                     
SyntaxError: unexpected indent
df = yf.download('SPY', datetime(2025,5,25), datetime.today())
                     

[*********************100%***********************]  1 of 1 completed
def get_stockdata(ticker,start,end):
    data = yf.download(tickers=[ticker],start = start, end = end)
    data.insert(0,"Ticker",ticker)
    return data

df
Price            Close        High         Low        Open    Volume
Ticker             SPY         SPY         SPY         SPY       SPY
Date                                                                
2025-05-27  582.948364  583.106118  570.404811  577.938828  72588500
2025-05-28  579.575745  584.545858  578.846021  583.352624  68445500
2025-05-29  581.863525  584.969846  577.938764  584.831774  69973300
2025-05-30  581.212830  582.928679  575.148130  580.759190  90601200
2025-06-02  584.486694  584.565541  576.942807  579.605359  61630500
...                ...         ...         ...         ...       ...
2026-06-17  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24  733.239990  739.950012  730.840027  735.169983  56924000

[271 rows x 5 columns]
df2 = yf.download('INFY', datetime(2025,5,25), datetime.today())

[*********************100%***********************]  1 of 1 completed
df
Price            Close        High         Low        Open    Volume
Ticker             SPY         SPY         SPY         SPY       SPY
Date                                                                
2025-05-27  582.948364  583.106118  570.404811  577.938828  72588500
2025-05-28  579.575745  584.545858  578.846021  583.352624  68445500
2025-05-29  581.863525  584.969846  577.938764  584.831774  69973300
2025-05-30  581.212830  582.928679  575.148130  580.759190  90601200
2025-06-02  584.486694  584.565541  576.942807  579.605359  61630500
...                ...         ...         ...         ...       ...
2026-06-17  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24  733.239990  739.950012  730.840027  735.169983  56924000

[271 rows x 5 columns]
df2 = yf.download('INFY.NS', datetime(2025,5,25), datetime.today())

[*********************100%***********************]  1 of 1 completed
df2
Price             Close         High          Low         Open    Volume
Ticker          INFY.NS      INFY.NS      INFY.NS      INFY.NS   INFY.NS
Date                                                                    
2025-05-26  1502.556152  1505.693456  1485.633930  1489.341621   3170102
2025-05-27  1492.669067  1504.837870  1479.644742  1501.985818   7775714
2025-05-28  1494.285278  1509.401062  1492.574001  1503.031525   3623370
2025-05-29  1507.404541  1529.555525  1498.848385  1510.636890   8609500
2025-05-30  1506.536987  1515.502795  1499.210153  1514.538735  13148092
...                 ...          ...          ...          ...       ...
2026-06-19  1051.400024  1066.000000  1030.000000  1062.300049  45665442
2026-06-22  1065.400024  1080.300049  1055.000000  1055.000000  10178505
2026-06-23  1029.300049  1055.300049  1026.000000  1053.800049  19323064
2026-06-24  1056.599976  1065.500000  1037.699951  1040.900024  12346266
2026-06-25  1046.800049  1068.000000  1044.099976  1065.000000   2372812

[272 rows x 5 columns]
df
Price            Close        High         Low        Open    Volume
Ticker             SPY         SPY         SPY         SPY       SPY
Date                                                                
2025-05-27  582.948364  583.106118  570.404811  577.938828  72588500
2025-05-28  579.575745  584.545858  578.846021  583.352624  68445500
2025-05-29  581.863525  584.969846  577.938764  584.831774  69973300
2025-05-30  581.212830  582.928679  575.148130  580.759190  90601200
2025-06-02  584.486694  584.565541  576.942807  579.605359  61630500
...                ...         ...         ...         ...       ...
2026-06-17  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24  733.239990  739.950012  730.840027  735.169983  56924000

[271 rows x 5 columns]
df2
Price             Close         High          Low         Open    Volume
Ticker          INFY.NS      INFY.NS      INFY.NS      INFY.NS   INFY.NS
Date                                                                    
2025-05-26  1502.556152  1505.693456  1485.633930  1489.341621   3170102
2025-05-27  1492.669067  1504.837870  1479.644742  1501.985818   7775714
2025-05-28  1494.285278  1509.401062  1492.574001  1503.031525   3623370
2025-05-29  1507.404541  1529.555525  1498.848385  1510.636890   8609500
2025-05-30  1506.536987  1515.502795  1499.210153  1514.538735  13148092
...                 ...          ...          ...          ...       ...
2026-06-19  1051.400024  1066.000000  1030.000000  1062.300049  45665442
2026-06-22  1065.400024  1080.300049  1055.000000  1055.000000  10178505
2026-06-23  1029.300049  1055.300049  1026.000000  1053.800049  19323064
2026-06-24  1056.599976  1065.500000  1037.699951  1040.900024  12346266
2026-06-25  1046.800049  1068.000000  1044.099976  1065.000000   2372812

[272 rows x 5 columns]
df3 = yf.download('^NSEI', datetime(2025,5,25), datetime.today())

[*********************100%***********************]  1 of 1 completed
df3
Price              Close          High           Low          Open  Volume
Ticker             ^NSEI         ^NSEI         ^NSEI         ^NSEI   ^NSEI
Date                                                                      
2025-05-26  25001.150391  25079.199219  24900.500000  24919.349609  302800
2025-05-27  24826.199219  25062.900391  24704.099609  24956.650391  525700
2025-05-28  24752.449219  24864.250000  24737.050781  24832.500000  684400
2025-05-29  24833.599609  24892.599609  24677.300781  24825.099609  345400
2025-05-30  24750.699219  24863.949219  24717.400391  24812.599609  853900
...                  ...           ...           ...           ...     ...
2026-06-19  24013.099609  24047.199219  23901.900391  23991.199219  447900
2026-06-22  24102.900391  24168.050781  24073.150391  24106.599609  252800
2026-06-23  23824.099609  24135.500000  23784.949219  24071.300781  340100
2026-06-24  24021.650391  24090.050781  23789.250000  23795.800781  395600
2026-06-25  24142.699219  24169.699219  24107.800781  24125.849609       0

[269 rows x 5 columns]
df.high
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    df.high
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'high'. Did you mean: 'High'?
df.High
Ticker             SPY
Date                  
2025-05-27  583.106118
2025-05-28  584.545858
2025-05-29  584.969846
2025-05-30  582.928679
2025-06-02  584.565541
...                ...
2026-06-17  750.217279
2026-06-18  748.229980
2026-06-22  750.179993
2026-06-23  739.630005
2026-06-24  739.950012

[271 rows x 1 columns]
df.Low
Ticker             SPY
Date                  
2025-05-27  570.404811
2025-05-28  578.846021
2025-05-29  577.938764
2025-05-30  575.148130
2025-06-02  576.942807
...                ...
2026-06-17  737.320450
2026-06-18  743.859985
2026-06-22  743.130005
2026-06-23  732.299988
2026-06-24  730.840027

[271 rows x 1 columns]
df
Price            Close        High         Low        Open    Volume
Ticker             SPY         SPY         SPY         SPY       SPY
Date                                                                
2025-05-27  582.948364  583.106118  570.404811  577.938828  72588500
2025-05-28  579.575745  584.545858  578.846021  583.352624  68445500
2025-05-29  581.863525  584.969846  577.938764  584.831774  69973300
2025-05-30  581.212830  582.928679  575.148130  580.759190  90601200
2025-06-02  584.486694  584.565541  576.942807  579.605359  61630500
...                ...         ...         ...         ...       ...
2026-06-17  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24  733.239990  739.950012  730.840027  735.169983  56924000

[271 rows x 5 columns]
d = df.reset_index().pivot("Date",columns = "Ticker", values = "Close")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d = df.reset_index().pivot("Date",columns = "Ticker", values = "Close")
TypeError: DataFrame.pivot() takes 1 positional argument but 2 positional arguments (and 2 keyword-only arguments) were given
d = df.reset_index().pivot(index="Date",columns = "Ticker", values = "Close")
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Ticker'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d = df.reset_index().pivot(index="Date",columns = "Ticker", values = "Close")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10986, in pivot
    return pivot(self, index=index, columns=columns, values=values)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\pivot.py", line 893, in pivot
    data_columns = [data[col] for col in columns_listlike]
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
KeyError: 'Ticker'
df.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 271 entries, 2025-05-27 to 2026-06-24
Data columns (total 5 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   (Close, SPY)   271 non-null    float64
 1   (High, SPY)    271 non-null    float64
 2   (Low, SPY)     271 non-null    float64
 3   (Open, SPY)    271 non-null    float64
 4   (Volume, SPY)  271 non-null    int64  
dtypes: float64(4), int64(1)
memory usage: 12.7 KB
d = df.reset_index().pivot(index="Date", values = "Close")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d = df.reset_index().pivot(index="Date", values = "Close")
TypeError: DataFrame.pivot() missing 1 required keyword-only argument: 'columns'
d = df.reset_index().pivot(index="Date")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d = df.reset_index().pivot(index="Date")
TypeError: DataFrame.pivot() missing 1 required keyword-only argument: 'columns'
d = df.reset_index().pivot(index="Date",columns = "Close")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d = df.reset_index().pivot(index="Date",columns = "Close")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10986, in pivot
    return pivot(self, index=index, columns=columns, values=values)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\pivot.py", line 910, in pivot
    result = cast("DataFrame", indexed.unstack(columns_listlike))  # type: ignore[arg-type]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 11579, in unstack
    result = unstack(self, level, fill_value, sort)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\reshape.py", line 583, in unstack
    return _unstack_frame(obj, level, fill_value=fill_value, sort=sort)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\reshape.py", line 606, in _unstack_frame
    unstacker = _Unstacker(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\reshape.py", line 176, in __init__
    self._make_selectors()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\reshape.py", line 217, in _make_selectors
    remaining_labels = self.sorted_labels[:-1]
  File "pandas/_libs/properties.pyx", line 36, in pandas._libs.properties.CachedProperty.__get__
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\reshape.py", line 205, in sorted_labels
    return [line.take(indexer) for line in to_sort]
IndexError: index 1 is out of bounds for axis 0 with size 1
plt.style.use('ggplot')
df.plot(figsize = (20,10))
<Axes: xlabel='Date'>
plt.show()
df.close.plot(figsize = (20,10))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    df.close.plot(figsize = (20,10))
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'close'. Did you mean: 'Close'?
df.Close.plot(figsize = (20,10))
<Axes: xlabel='Date'>
plt.show()
SPY = SPY.reset_index().pivot(index="Data", columns= "Ticker", values = "Close")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    SPY = SPY.reset_index().pivot(index="Data", columns= "Ticker", values = "Close")
NameError: name 'SPY' is not defined
start = datetime(2020,1,1)
end = datetime.today()
start
datetime.datetime(2020, 1, 1, 0, 0)
end
datetime.datetime(2026, 6, 25, 9, 55, 18, 268533)
SPY = get_stock_data("SPY", start,end)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    SPY = get_stock_data("SPY", start,end)
NameError: name 'get_stock_data' is not defined. Did you mean: 'get_stockdata'?
SPY = get_stockdata("SPY", start,end)
Exception ignored while calling deallocator <function Image.__del__ at 0x000002048185BED0>:
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 4283, in __del__
    self.tk.call('image', 'delete', self.name)
RuntimeError: main thread is not in main loop
Exception ignored while calling deallocator <function Variable.__del__ at 0x00000204813BF530>:
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 416, in __del__
    if self._tk.getboolean(self._tk.call("info", "exists", self._name)):
RuntimeError: main thread is not in main loop
Exception ignored while calling deallocator <function Variable.__del__ at 0x00000204813BF530>:
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 416, in __del__
    if self._tk.getboolean(self._tk.call("info", "exists", self._name)):
RuntimeError: main thread is not in main loop
Exception ignored while calling deallocator <function Variable.__del__ at 0x00000204813BF530>:
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 416, in __del__
    if self._tk.getboolean(self._tk.call("info", "exists", self._name)):
RuntimeError: main thread is not in main loop
Exception ignored while calling deallocator <function Variable.__del__ at 0x00000204813BF530>:
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 416, in __del__
    if self._tk.getboolean(self._tk.call("info", "exists", self._name)):
RuntimeError: main thread is not in main loop

[*********************100%***********************]  1 of 1 completed
SPY
Price      Ticker       Close        High         Low        Open    Volume
Ticker                    SPY         SPY         SPY         SPY       SPY
Date                                                                       
2020-01-02    SPY  296.125244  296.143492  293.992293  294.912936  59151200
2020-01-03    SPY  293.882965  295.004144  292.688877  292.743566  77709700
2020-01-06    SPY  295.004181  295.086214  292.014370  292.132872  55653900
2020-01-07    SPY  294.174622  294.912950  293.727958  294.438942  40496400
2020-01-08    SPY  295.742401  296.954709  294.119898  294.365998  68296000
...           ...         ...         ...         ...         ...       ...
2026-06-17    SPY  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18    SPY  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22    SPY  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23    SPY  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24    SPY  733.239990  739.950012  730.840027  735.169983  56924000

[1627 rows x 6 columns]
IYW = get_stockdata("IYW", start,end)
  

[*********************100%***********************]  1 of 1 completed
VT = get_stockdata("VT", start,end)
  

[*********************100%***********************]  1 of 1 completed
DBA = get_stockdata("DBA", start,end)
  

[*********************100%***********************]  1 of 1 completed
KeyboardInterrupt
TLT = get_stockdata("TLT", start,end)
  

[*********************100%***********************]  1 of 1 completed
PDBC = get_stockdata("PDBC", start,end)
  

[*********************100%***********************]  1 of 1 completed
IAU = get_stockdata("IAU", start,end)
  

[*********************100%***********************]  1 of 1 completed
IYW
  
Price      Ticker       Close        High         Low        Open  Volume
Ticker                    IYW         IYW         IYW         IYW     IYW
Date                                                                     
2020-01-02    IYW   57.811768   57.811768   57.098314   57.159189  826400
2020-01-03    IYW   57.234680   57.595059   57.027704   57.027704  377200
2020-01-06    IYW   57.587749   57.609664   56.528523   56.669753  330800
2020-01-07    IYW   57.609661   57.833681   57.465997   57.672973  289600
2020-01-08    IYW   58.184322   58.422951   57.609662   57.655928  476400
...           ...         ...         ...         ...         ...     ...
2026-06-17    IYW  246.389999  251.440002  245.839996  250.729996  814500
2026-06-18    IYW  253.570007  254.369995  250.250000  251.970001  571300
2026-06-22    IYW  253.279999  256.380005  251.919998  255.059998  629100
2026-06-23    IYW  243.369995  247.289993  242.940002  243.970001  484200
2026-06-24    IYW  242.190002  245.580002  239.210007  243.889999  600800

[1627 rows x 6 columns]
VT
  
Price      Ticker       Close        High         Low        Open   Volume
Ticker                     VT          VT          VT          VT       VT
Date                                                                      
2020-01-02     VT   71.985420   71.985420   71.554266   71.651057   946100
2020-01-03     VT   71.334312   71.624684   71.096740   71.184729  2310500
2020-01-06     VT   71.598289   71.598289   70.973554   70.982348  2641500
2020-01-07     VT   71.378304   71.527887   71.263911   71.527887  1339100
2020-01-08     VT   71.668663   71.915043   71.343101   71.351895  3532800
...           ...         ...         ...         ...         ...      ...
2026-06-17     VT  155.847000  158.288178  155.568009  157.889624  3620600
2026-06-18     VT  157.660004  157.949997  157.119995  157.789993  1976600
2026-06-22     VT  157.559998  158.429993  157.270004  157.889999  2718900
2026-06-23     VT  154.330002  155.600006  154.210007  154.419998  3432200
2026-06-24     VT  154.259995  155.339996  153.669998  154.580002  3433300

[1627 rows x 6 columns]
SPY = SPY.reset_index().pivot(index="Date", columns= "Ticker", values = "Close")
  
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    SPY = SPY.reset_index().pivot(index="Date", columns= "Ticker", values = "Close")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10986, in pivot
    return pivot(self, index=index, columns=columns, values=values)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\reshape\pivot.py", line 905, in pivot
    indexed = data._constructor_sliced(data[values]._values, index=multiindex)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\series.py", line 514, in __init__
    data = sanitize_array(data, index, dtype, copy)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\construction.py", line 681, in sanitize_array
    subarr = _sanitize_ndim(subarr, data, dtype, index, allow_2d=allow_2d)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\construction.py", line 740, in _sanitize_ndim
    raise ValueError(
ValueError: Data must be 1-dimensional, got ndarray of shape (1627, 1) instead
print(type(SPY["Close"]))
<class 'pandas.DataFrame'>
print(SPY.columns)
MultiIndex([('Ticker',    ''),
            ( 'Close', 'SPY'),
            (  'High', 'SPY'),
            (   'Low', 'SPY'),
            (  'Open', 'SPY'),
            ('Volume', 'SPY')],
           names=['Price', 'Ticker'])
print(SPY.reset_index().columns)
MultiIndex([(  'Date',    ''),
            ('Ticker',    ''),
            ( 'Close', 'SPY'),
            (  'High', 'SPY'),
            (   'Low', 'SPY'),
            (  'Open', 'SPY'),
            ('Volume', 'SPY')],
           names=['Price', 'Ticker'])
stock = pd.concat(
    [SPY, IYW, VT, DBA, TLT, PDBC, IAU],axis=1, join="outer")
stock.head()
Price      Ticker       Close        High  ...        Low       Open    Volume
Ticker                    SPY         SPY  ...        IAU        IAU       IAU
Date                                       ...                                
2020-01-02    SPY  296.125244  296.143492  ...  29.120001  29.200001  18539150
2020-01-03    SPY  293.882965  295.004144  ...  29.520000  29.600000   9172600
2020-01-06    SPY  295.004181  295.086214  ...  29.820000  30.139999  15387150
2020-01-07    SPY  294.174622  294.912950  ...  29.940001  29.959999  10537000
2020-01-08    SPY  295.742401  296.954709  ...  29.660000  30.160000  17847550

[5 rows x 42 columns]
stock.info()
<class 'pandas.DataFrame'>
DatetimeIndex: 1627 entries, 2020-01-02 to 2026-06-24
Data columns (total 42 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   (Ticker, )      1627 non-null   str    
 1   (Close, SPY)    1627 non-null   float64
 2   (High, SPY)     1627 non-null   float64
 3   (Low, SPY)      1627 non-null   float64
 4   (Open, SPY)     1627 non-null   float64
 5   (Volume, SPY)   1627 non-null   int64  
 6   (Ticker, )      1627 non-null   str    
 7   (Close, IYW)    1627 non-null   float64
 8   (High, IYW)     1627 non-null   float64
 9   (Low, IYW)      1627 non-null   float64
 10  (Open, IYW)     1627 non-null   float64
 11  (Volume, IYW)   1627 non-null   int64  
 12  (Ticker, )      1627 non-null   str    
 13  (Close, VT)     1627 non-null   float64
 14  (High, VT)      1627 non-null   float64
 15  (Low, VT)       1627 non-null   float64
 16  (Open, VT)      1627 non-null   float64
 17  (Volume, VT)    1627 non-null   int64  
 18  (Ticker, )      1627 non-null   str    
 19  (Close, DBA)    1627 non-null   float64
 20  (High, DBA)     1627 non-null   float64
 21  (Low, DBA)      1627 non-null   float64
 22  (Open, DBA)     1627 non-null   float64
 23  (Volume, DBA)   1627 non-null   int64  
 24  (Ticker, )      1627 non-null   str    
 25  (Close, TLT)    1627 non-null   float64
 26  (High, TLT)     1627 non-null   float64
 27  (Low, TLT)      1627 non-null   float64
 28  (Open, TLT)     1627 non-null   float64
 29  (Volume, TLT)   1627 non-null   int64  
 30  (Ticker, )      1627 non-null   str    
 31  (Close, PDBC)   1627 non-null   float64
 32  (High, PDBC)    1627 non-null   float64
 33  (Low, PDBC)     1627 non-null   float64
 34  (Open, PDBC)    1627 non-null   float64
 35  (Volume, PDBC)  1627 non-null   int64  
 36  (Ticker, )      1627 non-null   str    
 37  (Close, IAU)    1627 non-null   float64
 38  (High, IAU)     1627 non-null   float64
 39  (Low, IAU)      1627 non-null   float64
 40  (Open, IAU)     1627 non-null   float64
 41  (Volume, IAU)   1627 non-null   int64  
dtypes: float64(28), int64(7), str(7)
memory usage: 546.6 KB
stock.plot(figsize= (20,10))

<Axes: xlabel='Date'>
plt.show()
tikers = ["SPY", "IYW", "VT", "DBA", "TLT", "PDBC", "IAU"]
stockdata = yf.download(tickers,start=start,end=end,auto_adjust=True)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    stockdata = yf.download(tickers,start=start,end=end,auto_adjust=True)
NameError: name 'tickers' is not defined. Did you mean: 'tikers'?
stockdata = yf.download(tikers,start=start,end=end,auto_adjust=True)

[                       0%                       ]
[**************        29%                       ]  2 of 7 completed
[**************        29%                       ]  2 of 7 completed
[**********************57%**                     ]  4 of 7 completed
[**********************71%*********              ]  5 of 7 completed
[**********************86%****************       ]  6 of 7 completed
[*********************100%***********************]  7 of 7 completed
stock = data["Close"]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    stock = data["Close"]
NameError: name 'data' is not defined. Did you mean: 'date'?
stocks = stockdata["Close"]
stocks
Ticker            DBA        IAU  ...         TLT          VT
Date                              ...                        
2020-01-02  14.560220  29.219999  ...  113.300827   71.985428
2020-01-03  14.392557  29.620001  ...  115.045685   71.334305
2020-01-06  14.427855  29.920000  ...  114.392441   71.598289
2020-01-07  14.463152  30.040001  ...  113.830048   71.378281
2020-01-08  14.392557  29.820000  ...  113.077583   71.668655
...               ...        ...  ...         ...         ...
2026-06-17  26.840000  79.639999  ...   86.330002  155.847000
2026-06-18  26.629999  79.330002  ...   86.750000  157.660004
2026-06-22  26.650000  78.800003  ...   86.089996  157.559998
2026-06-23  26.600000  77.330002  ...   86.199997  154.330002
2026-06-24  26.559999  74.989998  ...   87.379997  154.259995

[1627 rows x 7 columns]
stock.plot(figsize = (30,15))

<Axes: xlabel='Date'>
plt.show()
stocks.plot(figsize = (30,15))
<Axes: xlabel='Date'>
plt.show()
tickers = ["RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS", "TRENT.NS","BHARTIARTL.NS","NESTLEIND.NS","BAJAJ-AUTO.NS"]
indata = yf.download(tickers,start="2018-01-01",end=end,auto_adjust=True)

[                       0%                       ]
[***********           22%                       ]  2 of 9 completed
[****************      33%                       ]  3 of 9 completed
[********************* 44%                       ]  4 of 9 completed
[********************* 44%                       ]  4 of 9 completed
[********************* 44%                       ]  4 of 9 completed
[**********************78%************           ]  7 of 9 completed
[**********************89%******************     ]  8 of 9 completed
[*********************100%***********************]  9 of 9 completed
instocks = indata["close"]

instocks = indata["Close"]
instocks
Ticker      BAJAJ-AUTO.NS  BHARTIARTL.NS  ...       TCS.NS     TRENT.NS
Date                                      ...                          
2018-01-01    2601.655273     453.573090  ...  1069.273315   328.102356
2018-01-02    2606.005615     443.821136  ...  1063.453125   323.747467
2018-01-03    2563.531250     445.238800  ...  1066.464111   325.133087
2018-01-04    2582.039551     449.362976  ...  1073.921143   328.993073
2018-01-05    2594.220215     463.969391  ...  1086.894775   346.660217
...                   ...            ...  ...          ...          ...
2026-06-19   10066.000000    1910.800049  ...  2125.000000  3205.800049
2026-06-22   10191.000000    1916.599976  ...  2127.800049  3180.600098
2026-06-23   10025.000000    1901.599976  ...  2059.600098  3142.899902
2026-06-24    9750.000000    1877.300049  ...  2109.000000  3247.000000
2026-06-25    9853.000000    1870.800049  ...  2144.399902  3284.600098

[2096 rows x 9 columns]
instocks.plot(figsize= (30,18))
<Axes: xlabel='Date'>
plt.show()
plt.show()
def allplots():
    for i in range(3):
        df.plot(figsize = (20,10))
        plt.show()
        stocks.plot(figsize = (30,15))
        plt.show()
        instocks.plot(figsize= (30,18))
        plt.show()

        
allplots()
covid = stocks['2020-2-1':'2020-7-31']
stocks.plot()
<Axes: xlabel='Date'>
plt.show()
covid.plot(figsize= 30,15)
SyntaxError: positional argument follows keyword argument
covid.plot(figsize= (30,15))
<Axes: xlabel='Date'>
plt.show()
x = covid.index
sy = covid[['SPY']]
iy = covid[['IAU']]
df = covid[['DBA']]
dy df
SyntaxError: invalid syntax
dy = df
ty = covid[['TLT']]
df = yf.download('SPY', datetime(2025,5,25), datetime.today())

[*********************100%***********************]  1 of 1 completed
dy
Ticker            DBA
Date                 
2020-02-03  13.783676
2020-02-04  13.810147
2020-02-05  13.818973
2020-02-06  13.916041
2020-02-07  13.977812
...               ...
2020-07-27  12.239409
2020-07-28  12.168815
2020-07-29  12.274707
2020-07-30  12.318830
2020-07-31  12.512965

[126 rows x 1 columns]
df
Price            Close        High         Low        Open    Volume
Ticker             SPY         SPY         SPY         SPY       SPY
Date                                                                
2025-05-27  582.948303  583.106057  570.404751  577.938767  72588500
2025-05-28  579.575745  584.545858  578.846021  583.352624  68445500
2025-05-29  581.863586  584.969907  577.938825  584.831835  69973300
2025-05-30  581.212769  582.928618  575.148070  580.759129  90601200
2025-06-02  584.486694  584.565541  576.942807  579.605359  61630500
...                ...         ...         ...         ...       ...
2026-06-17  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24  733.239990  739.950012  730.840027  735.169983  56924000

[271 rows x 5 columns]
fig, axs = plt.subplots(1,3, figsize = (15,5))
axs[0].plot(x,sy)
[<matplotlib.lines.Line2D object at 0x00000204C11AFE00>]
axs[1].plot(y,iy)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    axs[1].plot(y,iy)
NameError: name 'y' is not defined. Did you mean: 'yf'?
axs[1].plot(x,iy)
[<matplotlib.lines.Line2D object at 0x00000204C11AFCB0>]
axs[2].plot(x,ty)
[<matplotlib.lines.Line2D object at 0x00000204BCFB0050>]
fig.suptitle('Covid-19')
Text(0.5, 0.98, 'Covid-19')
fig.show()
fig.show()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    fig.show()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\figure.py", line 2804, in show
    self.canvas.manager.show()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\backends\_backend_tk.py", line 608, in show
    self.canvas.manager.window.attributes('-topmost', 1)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 2185, in wm_attributes
    return self.tk.call('wm', 'attributes', self._w, *args)
_tkinter.TclError: can't invoke "wm" command: application has been destroyed
#ty(gold) and sy (stock)
intickers = ["RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS", "TRENT.NS","BHARTIARTL.NS","NESTLEIND.NS","BAJAJ-AUTO.NS"]
metickers = ["BZ=F","GC=F","PPA","^GSPC"]
tikers = ["SPY", "IYW", "VT", "DBA", "TLT", "PDBC", "IAU"]
df
Price            Close        High         Low        Open    Volume
Ticker             SPY         SPY         SPY         SPY       SPY
Date                                                                
2025-05-27  582.948303  583.106057  570.404751  577.938767  72588500
2025-05-28  579.575745  584.545858  578.846021  583.352624  68445500
2025-05-29  581.863586  584.969907  577.938825  584.831835  69973300
2025-05-30  581.212769  582.928618  575.148070  580.759129  90601200
2025-06-02  584.486694  584.565541  576.942807  579.605359  61630500
...                ...         ...         ...         ...       ...
2026-06-17  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24  733.239990  739.950012  730.840027  735.169983  56924000

[271 rows x 5 columns]
df.drop(['Ticker','High','Low','Open','Close'],axis=1,inplace= True)
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Ticker'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    df.drop(['Ticker','High','Low','Open','Close'],axis=1,inplace= True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 6300, in drop
    return super().drop(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 4644, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 4686, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 2846, in drop
    loc = self.get_loc(level_codes)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 3523, in get_loc
    loc = self._get_level_indexer(key, level=0)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 3885, in _get_level_indexer
    idx = self._get_loc_single_level_index(level_index, key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\multi.py", line 3458, in _get_loc_single_level_index
    return level_index.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Ticker'
df.columns
MultiIndex([( 'Close', 'SPY'),
            (  'High', 'SPY'),
            (   'Low', 'SPY'),
            (  'Open', 'SPY'),
            ('Volume', 'SPY')],
           names=['Price', 'Ticker'])
df.drop(['High','Low','Open','Close'],axis=1,inplace= True)
df
Price         Volume
Ticker           SPY
Date                
2025-05-27  72588500
2025-05-28  68445500
2025-05-29  69973300
2025-05-30  90601200
2025-06-02  61630500
...              ...
2026-06-17  85945200
2026-06-18  80875700
2026-06-22  46628100
2026-06-23  66846800
2026-06-24  56924000

[271 rows x 1 columns]
df = df.reset_index()
df
Price        Date    Volume
Ticker                  SPY
0      2025-05-27  72588500
1      2025-05-28  68445500
2      2025-05-29  69973300
3      2025-05-30  90601200
4      2025-06-02  61630500
..            ...       ...
266    2026-06-17  85945200
267    2026-06-18  80875700
268    2026-06-22  46628100
269    2026-06-23  66846800
270    2026-06-24  56924000

[271 rows x 2 columns]
df.columns = ['Date', 'Volume']
df
          Date    Volume
0   2025-05-27  72588500
1   2025-05-28  68445500
2   2025-05-29  69973300
3   2025-05-30  90601200
4   2025-06-02  61630500
..         ...       ...
266 2026-06-17  85945200
267 2026-06-18  80875700
268 2026-06-22  46628100
269 2026-06-23  66846800
270 2026-06-24  56924000

[271 rows x 2 columns]
df.index
RangeIndex(start=0, stop=271, step=1)
df.index()
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    df.index()
TypeError: 'RangeIndex' object is not callable
df.setindex('Date')
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    df.setindex('Date')
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'setindex'. Did you mean: 'set_index'?
df.set_index('Date')
              Volume
Date                
2025-05-27  72588500
2025-05-28  68445500
2025-05-29  69973300
2025-05-30  90601200
2025-06-02  61630500
...              ...
2026-06-17  85945200
2026-06-18  80875700
2026-06-22  46628100
2026-06-23  66846800
2026-06-24  56924000

[271 rows x 1 columns]
q = df.index
w = df['Volume']
plt.figure(figsize = (15,3))
<Figure size 1500x300 with 0 Axes>
plt.bar(q,w)
<BarContainer object of 271 artists>
plt.show()
w
0      72588500
1      68445500
2      69973300
3      90601200
4      61630500
         ...   
266    85945200
267    80875700
268    46628100
269    66846800
270    56924000
Name: Volume, Length: 271, dtype: int64
plt.plot(df['Date'],df['Volume'])
[<matplotlib.lines.Line2D object at 0x00000204C39F38C0>]
plt.show()
plt.bar
plt.bar(df['Date'],df['Volume'])
<BarContainer object of 271 artists>
plt.show()
plt.bar(df['Date'],df['Volume'])
<BarContainer object of 271 artists>
plt.show()
ticker = 'PDBC'
start = datetime(2020,1,1)
end = datetime.today()
fig = plt.figure(figsize=(12,8))
top_grid = plt.subplot2grid((4,4),(0,0),rowspan=3,colspan=4)
bottom_grid = plt.subplot2grid((4,4),(3,0), rowspan =1,colspan=4)
top_grid.plot(df.index,df['Close'],label='Close')
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Close'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    top_grid.plot(df.index,df['Close'],label='Close')
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Close'
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 271 entries, 0 to 270
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype        
---  ------  --------------  -----        
 0   Date    271 non-null    datetime64[s]
 1   Volume  271 non-null    int64        
dtypes: datetime64[s](1), int64(1)
memory usage: 4.4 KB
df.head()
        Date    Volume
0 2025-05-27  72588500
1 2025-05-28  68445500
2 2025-05-29  69973300
3 2025-05-30  90601200
4 2025-06-02  61630500
df = get_stockdata(ticker,start,end)

[*********************100%***********************]  1 of 1 completed
top_grid.plot(df.index,df['Close'],label='Close')
[<matplotlib.lines.Line2D object at 0x00000204C5146A50>]
bottom_grid.plot(df.index,df['Volume'],label='Volume')
[<matplotlib.lines.Line2D object at 0x00000204C5146BA0>]
plt.tight_layout()
plt.legend()
<matplotlib.legend.Legend object at 0x00000204C51467B0>
plt.show()
spy
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    spy
NameError: name 'spy' is not defined. Did you mean: 'sy'?
SPY
Price      Ticker       Close        High         Low        Open    Volume
Ticker                    SPY         SPY         SPY         SPY       SPY
Date                                                                       
2020-01-02    SPY  296.125244  296.143492  293.992293  294.912936  59151200
2020-01-03    SPY  293.882965  295.004144  292.688877  292.743566  77709700
2020-01-06    SPY  295.004181  295.086214  292.014370  292.132872  55653900
2020-01-07    SPY  294.174622  294.912950  293.727958  294.438942  40496400
2020-01-08    SPY  295.742401  296.954709  294.119898  294.365998  68296000
...           ...         ...         ...         ...         ...       ...
2026-06-17    SPY  739.056030  750.217279  737.320450  749.359442  85945200
2026-06-18    SPY  746.739990  748.229980  743.859985  747.760010  80875700
2026-06-22    SPY  744.390015  750.179993  743.130005  747.700012  46628100
2026-06-23    SPY  733.580017  739.630005  732.299988  733.809998  66846800
2026-06-24    SPY  733.239990  739.950012  730.840027  735.169983  56924000

[1627 rows x 6 columns]
stock.head()
Price      Ticker       Close        High  ...        Low       Open    Volume
Ticker                    SPY         SPY  ...        IAU        IAU       IAU
Date                                       ...                                
2020-01-02    SPY  296.125244  296.143492  ...  29.120001  29.200001  18539150
2020-01-03    SPY  293.882965  295.004144  ...  29.520000  29.600000   9172600
2020-01-06    SPY  295.004181  295.086214  ...  29.820000  30.139999  15387150
2020-01-07    SPY  294.174622  294.912950  ...  29.940001  29.959999  10537000
2020-01-08    SPY  295.742401  296.954709  ...  29.660000  30.160000  17847550

[5 rows x 42 columns]
stockdata.head()
Price           Close                        ...    Volume                   
Ticker            DBA        IAU        IYW  ...       SPY       TLT       VT
Date                                         ...                             
2020-01-02  14.560220  29.219999  57.811768  ...  59151200  11034100   946100
2020-01-03  14.392557  29.620001  57.234665  ...  77709700  12366000  2310500
2020-01-06  14.427855  29.920000  57.587757  ...  55653900  11369800  2641500
2020-01-07  14.463152  30.040001  57.609669  ...  40496400   8381200  1339100
2020-01-08  14.392557  29.820000  58.184322  ...  68296000  10621700  3532800

[5 rows x 35 columns]
dir()
['DBA', 'IAU', 'IYW', 'PDBC', 'SPY', 'TLT', 'VT', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__warningregistry__', 'allplots', 'axs', 'bottom_grid', 'covid', 'date', 'datetime', 'df', 'df2', 'df3', 'dy', 'end', 'fig', 'get_stockdata', 'indata', 'instocks', 'intickers', 'iy', 'metickers', 'np', 'pd', 'plt', 'q', 'start', 'stock', 'stockdata', 'stocks', 'sy', 'ticker', 'tickers', 'tikers', 'time', 'timezone', 'top_grid', 'ty', 'w', 'x', 'yf']
stocks.head()
Ticker            DBA        IAU        IYW  ...         SPY         TLT         VT
Date                                         ...                                   
2020-01-02  14.560220  29.219999  57.811768  ...  296.125366  113.300827  71.985428
2020-01-03  14.392557  29.620001  57.234665  ...  293.882965  115.045685  71.334305
2020-01-06  14.427855  29.920000  57.587757  ...  295.004181  114.392441  71.598289
2020-01-07  14.463152  30.040001  57.609669  ...  294.174713  113.830048  71.378281
2020-01-08  14.392557  29.820000  58.184322  ...  295.742432  113.077583  71.668655

[5 rows x 7 columns]
stocks['SPY']
Date
2020-01-02    296.125366
2020-01-03    293.882965
2020-01-06    295.004181
2020-01-07    294.174713
2020-01-08    295.742432
                 ...    
2026-06-17    739.056030
2026-06-18    746.739990
2026-06-22    744.390015
2026-06-23    733.580017
2026-06-24    733.239990
Name: SPY, Length: 1627, dtype: float64
stocks['SPY'].shift(1)
Date
2020-01-02           NaN
2020-01-03    296.125366
2020-01-06    293.882965
2020-01-07    295.004181
2020-01-08    294.174713
                 ...    
2026-06-17    748.401978
2026-06-18    739.056030
2026-06-22    746.739990
2026-06-23    744.390015
2026-06-24    733.580017
Name: SPY, Length: 1627, dtype: float64
spy_daily_pc=(stock['SPY'].shift(1)-1)*100
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'SPY'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    spy_daily_pc=(stock['SPY'].shift(1)-1)*100
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
KeyError: 'SPY'
spy_daily_pc=(stocks['SPY'].shift(1)-1)*100
spy_daily_pc
Date
2020-01-02             NaN
2020-01-03    29512.536621
2020-01-06    29288.296509
2020-01-07    29400.418091
2020-01-08    29317.471313
                  ...     
2026-06-17    74740.197754
2026-06-18    73805.603027
2026-06-22    74573.999023
2026-06-23    74339.001465
2026-06-24    73258.001709
Name: SPY, Length: 1627, dtype: float64
sspy_daily_pc.plot()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    sspy_daily_pc.plot()
NameError: name 'sspy_daily_pc' is not defined. Did you mean: 'spy_daily_pc'?
spy_daily_pc.plot()
<Axes: xlabel='Date'>
plt.show()
spy_daily_pc.iloc[0]=0
plt.hist(spy_daily_pc,bins=50)
(array([  1.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
         0.,   0.,   2.,   8.,   8.,  13.,  26.,  30.,  56.,  58.,  25.,
        47.,  84., 102., 141., 111., 141., 111.,  35.,  23.,  18.,  38.,
        36.,  34.,  41.,  54.,  39.,  56.,  41.,  17.,  24.,  21.,  48.,
        51.,  39.,  10.,   6.,  18.,  14.]), array([    0.        ,  1513.2364502 ,  3026.47290039,  4539.70935059,
        6052.94580078,  7566.18225098,  9079.41870117, 10592.65515137,
       12105.89160156, 13619.12805176, 15132.36450195, 16645.60095215,
       18158.83740234, 19672.07385254, 21185.31030273, 22698.54675293,
       24211.78320312, 25725.01965332, 27238.25610352, 28751.49255371,
       30264.72900391, 31777.9654541 , 33291.2019043 , 34804.43835449,
       36317.67480469, 37830.91125488, 39344.14770508, 40857.38415527,
       42370.62060547, 43883.85705566, 45397.09350586, 46910.32995605,
       48423.56640625, 49936.80285645, 51450.03930664, 52963.27575684,
       54476.51220703, 55989.74865723, 57502.98510742, 59016.22155762,
       60529.45800781, 62042.69445801, 63555.9309082 , 65069.1673584 ,
       66582.40380859, 68095.64025879, 69608.87670898, 71122.11315918,
       72635.34960938, 74148.58605957, 75661.82250977]), <BarContainer object of 50 artists>)
plt
plt.show()
spy_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    spy_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 9151, in _arith_method
    new_data = self._dispatch_frame_op(other, op, axis=axis)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 9194, in _dispatch_frame_op
    bm = self._mgr.operate_blockwise(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\managers.py", line 1691, in operate_blockwise
    return operate_blockwise(self, other, array_op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\ops.py", line 65, in operate_blockwise
    res_values = array_op(lvals, rvals)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\string_.py", line 1218, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
spy_daily_pc = (stocks-stocks.shift(1))/stocks.shift(1)*100
stock_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    stock_daily_pc = (stock-stock.shift(1))/stock.shift(1)*100
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 9151, in _arith_method
    new_data = self._dispatch_frame_op(other, op, axis=axis)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 9194, in _dispatch_frame_op
    bm = self._mgr.operate_blockwise(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\managers.py", line 1691, in operate_blockwise
    return operate_blockwise(self, other, array_op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\ops.py", line 65, in operate_blockwise
    res_values = array_op(lvals, rvals)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\string_.py", line 1218, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
stock_daily = (stock-stock.shift(1))/stock.shift(1)*100
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    stock_daily = (stock-stock.shift(1))/stock.shift(1)*100
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 9151, in _arith_method
    new_data = self._dispatch_frame_op(other, op, axis=axis)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 9194, in _dispatch_frame_op
    bm = self._mgr.operate_blockwise(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\managers.py", line 1691, in operate_blockwise
    return operate_blockwise(self, other, array_op)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\ops.py", line 65, in operate_blockwise
    res_values = array_op(lvals, rvals)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\array_ops.py", line 279, in arithmetic_op
    res_values = op(left, right)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arraylike.py", line 198, in __sub__
    return self._arith_method(other, operator.sub)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\string_.py", line 1218, in _cmp_method
    result[valid] = op(self._ndarray[valid], other)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
stockdaily_pc = (stocks-stocks.shift(1))/stocks.shift(1)*100
stockdaily_pc.head()
Ticker           DBA       IAU       IYW  ...       SPY       TLT        VT
Date                                      ...                              
2020-01-02       NaN       NaN       NaN  ...       NaN       NaN       NaN
2020-01-03 -1.151512  1.368931 -0.998244  ... -0.757247  1.540022 -0.904521
2020-01-06  0.245248  1.012827  0.616920  ...  0.381518 -0.567813  0.370067
2020-01-07  0.244648  0.401072  0.038049  ... -0.281172 -0.491635 -0.307282
2020-01-08 -0.488101 -0.732361  0.997495  ...  0.532921 -0.661042  0.406811

[5 rows x 7 columns]
stock_d_cr=stockdaily_pc.cumsum()
stock_d_cr
Ticker            DBA         IAU         IYW  ...         SPY        TLT         VT
Date                                           ...                                  
2020-01-02        NaN         NaN         NaN  ...         NaN        NaN        NaN
2020-01-03  -1.151512    1.368931   -0.998244  ...   -0.757247   1.540022  -0.904521
2020-01-06  -0.906264    2.381757   -0.381324  ...   -0.375729   0.972209  -0.534454
2020-01-07  -0.661616    2.782830   -0.343275  ...   -0.656901   0.480574  -0.841736
2020-01-08  -1.149717    2.050469    0.654220  ...   -0.123980  -0.180467  -0.434925
>>> ...               ...         ...         ...  ...         ...        ...        ...
2026-06-17  67.591346  110.975550  171.021966  ...  104.840481 -18.239205  89.589555
>>> 2026-06-18  66.808928  110.586301  173.936048  ...  105.880180 -17.752702  90.752878
2026-06-22  66.884032  109.918207  173.821678  ...  105.565482 -18.513513  90.689447
>>> 2026-06-23  66.696418  108.052724  169.909011  ...  104.113287 -18.385739  88.639437
2026-06-24  66.546039  105.026726  169.424156  ...  104.066935 -17.016829  88.594075
>>> 
[1627 rows x 7 columns]
>>> stockdaily_pc.plt(figsize=(20,10))
  
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    stockdaily_pc.plt(figsize=(20,10))
>>>   File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
>>>     return object.__getattribute__(self, name)
>>> AttributeError: 'DataFrame' object has no attribute 'plt'. Did you mean: 'lt'?
stockdaily_pc.plot(figsize=(20,10))
>>> <Axes: xlabel='Date'>
>>> df_corr = stockdaily_pc.corr()
>>> df_corr
>>> Ticker       DBA       IAU       IYW      PDBC       SPY       TLT        VT
Ticker                                                                      
DBA     1.000000  0.142505  0.186022  0.460625  0.223922 -0.102164  0.244270
IAU     0.142505  1.000000  0.158111  0.294874  0.149830  0.206229  0.213712
IYW     0.186022  0.158111  1.000000  0.219365  0.918311 -0.063414  0.884631
PDBC    0.460625  0.294874  0.219365  1.000000  0.291024 -0.158824  0.312059
SPY     0.223922  0.149830  0.918311  0.291024  1.000000 -0.108657  0.974775
TLT    -0.102164  0.206229 -0.063414 -0.158824 -0.108657  1.000000 -0.094404
VT      0.244270  0.213712  0.884631  0.312059  0.974775 -0.094404  1.000000
plt.imshow(df_corr,cmap='hot',interpolation='none')
<matplotlib.image.AxesImage object at 0x00000204C11DFE00>
plt.colorbar()
<matplotlib.colorbar.Colorbar object at 0x00000204B84356A0>
plt.xticks(range(len(df_corr)),df_corr.columns)
([<matplotlib.axis.XTick object at 0x00000204C545D590>, <matplotlib.axis.XTick object at 0x00000204C5138910>, <matplotlib.axis.XTick object at 0x00000204BCFD9450>, <matplotlib.axis.XTick object at 0x00000204BCFD9810>, <matplotlib.axis.XTick object at 0x00000204BCFD9BD0>, <matplotlib.axis.XTick object at 0x00000204BCFD9F90>, <matplotlib.axis.XTick object at 0x00000204BCFDA350>], [Text(0, 0, 'DBA'), Text(1, 0, 'IAU'), Text(2, 0, 'IYW'), Text(3, 0, 'PDBC'), Text(4, 0, 'SPY'), Text(5, 0, 'TLT'), Text(6, 0, 'VT')])
plt.yticks(range(len(df_corr)),df_corr.columns)
>>> ([<matplotlib.axis.YTick object at 0x00000204C545D950>, <matplotlib.axis.YTick object at 0x00000204C11E6710>, <matplotlib.axis.YTick object at 0x00000204C11E65D0>, <matplotlib.axis.YTick object at 0x00000204C11E7B10>, <matplotlib.axis.YTick object at 0x00000204C11E6E90>, <matplotlib.axis.YTick object at 0x00000204C11E5950>, <matplotlib.axis.YTick object at 0x00000204C11E6210>], [Text(0, 0, 'DBA'), Text(0, 1, 'IAU'), Text(0, 2, 'IYW'), Text(0, 3, 'PDBC'), Text(0, 4, 'SPY'), Text(0, 5, 'TLT'), Text(0, 6, 'VT')])
plt.gcf.set_size_inches(10,10)
>>> Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
>>>     plt.gcf.set_size_inches(10,10)
AttributeError: 'function' object has no attribute 'set_size_inches'
>>> plt.gcf().set_size_inches(10, 10)
