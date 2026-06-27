Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])

plt.show()
SyntaxError: multiple statements found while compiling a single statement
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
[<matplotlib.lines.Line2D object at 0x000002051BBC7770>]
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
[<matplotlib.lines.Line2D object at 0x000002051BCA4C20>]
plt.show
<function show at 0x000002051B9573D0>
plt.show()
x,y = range(100),[value ** 2 for value in x]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x,y = range(100),[value ** 2 for value in x]
NameError: name 'x' is not defined
x = range(100)

y = [value ** 2 for value in x]
plt.plot(x,y, linewidth=5.0, color='red')
[<matplotlib.lines.Line2D object at 0x00000205225EA120>]
plt.title('hello world of chart')
Text(0.5, 1.0, 'hello world of chart')
plt.ylabel('y-some numbers')
Text(0, 0.5, 'y-some numbers')
plt.xlabel('x-some numbers')
Text(0.5, 0, 'x-some numbers')
plt.show()
days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_year)), days_in_year)
<BarContainer object of 9 artists>
plt.show()
plt.figure(figsize = (13, 6))

<Figure size 1300x600 with 0 Axes>
plt.xticks(rotation='vertical', size = 10)
(array([0. , 0.2, 0.4, 0.6, 0.8, 1. ]), [Text(0.0, 0, '0.0'), Text(0.2, 0, '0.2'), Text(0.4, 0, '0.4'), Text(0.6000000000000001, 0, '0.6'), Text(0.8, 0, '0.8'), Text(1.0, 0, '1.0')])
plt.barh(x, y)
<BarContainer object of 100 artists>
plt.show()
df
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    df
NameError: name 'df' is not defined
import sys
import pandas as pd
df = pd.read_csv(r"C:\Users\Lenovo\Documents\Day7\housing.csv")
df
      Avg. Area Income  ...                                            Address
0          79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1          79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2          61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3          63345.24005  ...                          USS Barnett\nFPO AP 44820
4          59982.19723  ...                         USNS Raymond\nFPO AE 09386
...                ...  ...                                                ...
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]
df.head(80)
    Avg. Area Income  ...                                            Address
0        79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1        79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2        61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3        63345.24005  ...                          USS Barnett\nFPO AP 44820
4        59982.19723  ...                         USNS Raymond\nFPO AE 09386
..               ...  ...                                                ...
75       70848.78866  ...                  USCGC Thompson\nFPO AA 13237-3887
76       59787.40450  ...   65884 Johns Valley Apt. 621\nEthanbury, NY 07783
77       64826.37189  ...                   Unit 2139 Box 3667\nDPO AP 49517
78       65925.85380  ...           253 Golden Island\nEast Donald, CT 91882
79       64419.25264  ...  4861 Steven Plains Suite 066\nPort Reginaland,...

[80 rows x 7 columns]
df.head(10)
   Avg. Area Income  ...                                            Address
0       79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1       79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2       61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3       63345.24005  ...                          USS Barnett\nFPO AP 44820
4       59982.19723  ...                         USNS Raymond\nFPO AE 09386
5       80175.75416  ...  06039 Jennifer Islands Apt. 443\nTracyport, KS...
6       64698.46343  ...  4759 Daniel Shoals Suite 442\nNguyenburgh, CO ...
7       78394.33928  ...     972 Joyce Viaduct\nLake William, TN 17778-6483
8       59927.66081  ...                          USS Gilbert\nFPO AA 20957
9       81885.92718  ...                   Unit 9446 Box 0958\nDPO AE 97025

[10 rows x 7 columns]
df.tail(10)
      Avg. Area Income  ...                                            Address
4990       52723.87656  ...         86727 Kelly Plaza\nLake Veronica, IL 04474
4991       74102.19189  ...         2871 John Lodge\nAmychester, GU 61734-5597
4992       87499.12574  ...              Unit 2096 Box 9559\nDPO AE 80983-8797
4993       69639.14090  ...  5259 David Causeway Apt. 975\nSouth Alexstad, ...
4994       73060.84623  ...             5224 Lamb Passage\nNancystad, GA 16579
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[10 rows x 7 columns]
df.shape()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    df.shape()
TypeError: 'tuple' object is not callable
df.shape
(5000, 7)
df.col()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    df.col()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'col'. Did you mean: 'cov'?
df.cov
<bound method DataFrame.cov of       Avg. Area Income  ...                                            Address
0          79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1          79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2          61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3          63345.24005  ...                          USS Barnett\nFPO AP 44820
4          59982.19723  ...                         USNS Raymond\nFPO AE 09386
...                ...  ...                                                ...
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]>
df.mean
<bound method DataFrame.mean of       Avg. Area Income  ...                                            Address
0          79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1          79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2          61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3          63345.24005  ...                          USS Barnett\nFPO AP 44820
4          59982.19723  ...                         USNS Raymond\nFPO AE 09386
...                ...  ...                                                ...
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]>
df.sum
<bound method DataFrame.sum of       Avg. Area Income  ...                                            Address
0          79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1          79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2          61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3          63345.24005  ...                          USS Barnett\nFPO AP 44820
4          59982.19723  ...                         USNS Raymond\nFPO AE 09386
...                ...  ...                                                ...
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]>
df.keys()
Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address'],
      dtype='str')
df.values()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    df.values()
TypeError: 'numpy.ndarray' object is not callable
numpy.ndarry
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    numpy.ndarry
NameError: name 'numpy' is not defined
import numpy as np
np.ndarry
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    np.ndarry
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\numpy\__init__.py", line 805, in __getattr__
    raise AttributeError(f"module {__name__!r} has no attribute {attr!r}")
AttributeError: module 'numpy' has no attribute 'ndarry'. Did you mean: 'ndarray'?
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 7 columns):
 #   Column                        Non-Null Count  Dtype  
---  ------                        --------------  -----  
 0   Avg. Area Income              5000 non-null   float64
 1   Avg. Area House Age           5000 non-null   float64
 2   Avg. Area Number of Rooms     5000 non-null   float64
 3   Avg. Area Number of Bedrooms  5000 non-null   float64
 4   Area Population               5000 non-null   float64
 5   Price                         5000 non-null   float64
 6   Address                       5000 non-null   str    
dtypes: float64(6), str(1)
memory usage: 273.6 KB
df.describe()
       Avg. Area Income  Avg. Area House Age  ...  Area Population         Price
count       5000.000000          5000.000000  ...      5000.000000  5.000000e+03
mean       68583.108984             5.977222  ...     36163.516039  1.232073e+06
std        10657.991214             0.991456  ...      9925.650114  3.531176e+05
min        17796.631190             2.644304  ...       172.610686  1.593866e+04
25%        61480.562390             5.322283  ...     29403.928700  9.975771e+05
50%        68804.286405             5.970429  ...     36199.406690  1.232669e+06
75%        75783.338665             6.650808  ...     42861.290770  1.471210e+06
max       107701.748400             9.519088  ...     69621.713380  2.469066e+06

[8 rows x 6 columns]
type(df)
<class 'pandas.DataFrame'>
df.to_timedelta()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    df.to_timedelta()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'to_timedelta'
df.fillna('NANA')
      Avg. Area Income  ...                                            Address
0          79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1          79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2          61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3          63345.24005  ...                          USS Barnett\nFPO AP 44820
4          59982.19723  ...                         USNS Raymond\nFPO AE 09386
...                ...  ...                                                ...
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]
df.explode()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    df.explode()
TypeError: DataFrame.explode() missing 1 required positional argument: 'column'
df.explode(Income)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    df.explode(Income)
NameError: name 'Income' is not defined
df.explode(Avg. Area Income)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
df.columns
Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address'],
      dtype='str')
df.explode(Price)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    df.explode(Price)
NameError: name 'Price' is not defined. Did you mean: 'slice'?
df.explode(slice)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    df.explode(slice)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 11488, in explode
    raise ValueError("column must be a scalar, tuple, or list thereof")
ValueError: column must be a scalar, tuple, or list thereof
df.slice()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    df.slice()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'slice'. Did you mean: '_slice'?
df
      Avg. Area Income  ...                                            Address
0          79545.45857  ...  208 Michael Ferry Apt. 674\nLaurabury, NE 3701...
1          79248.64245  ...  188 Johnson Views Suite 079\nLake Kathleen, CA...
2          61287.06718  ...  9127 Elizabeth Stravenue\nDanieltown, WI 06482...
3          63345.24005  ...                          USS Barnett\nFPO AP 44820
4          59982.19723  ...                         USNS Raymond\nFPO AE 09386
...                ...  ...                                                ...
4995       60567.94414  ...                   USNS Williams\nFPO AP 30153-7653
4996       78491.27543  ...              PSC 9258, Box 8489\nAPO AA 42991-3352
4997       63390.68689  ...  4215 Tracy Garden Suite 076\nJoshualand, VA 01...
4998       68001.33124  ...                          USS Wallace\nFPO AE 73316
4999       65510.58180  ...  37778 George Ridges Apt. 509\nEast Holly, NV 2...

[5000 rows x 7 columns]
pip install xlrd
SyntaxError: invalid syntax
pip list
SyntaxError: invalid syntax
import xlrd as xl
xl
<module 'xlrd' from 'C:\\Users\\Lenovo\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\xlrd\\__init__.py'>
dir(xl)
['Book', 'FILE_FORMAT_DESCRIPTIONS', 'FMLA_TYPE_ARRAY', 'FMLA_TYPE_CELL', 'FMLA_TYPE_COND_FMT', 'FMLA_TYPE_DATA_VAL', 'FMLA_TYPE_NAME', 'FMLA_TYPE_SHARED', 'Operand', 'PEEK_SIZE', 'Ref3D', 'XLDateError', 'XLRDError', 'XLS_SIGNATURE', 'XL_CELL_BLANK', 'XL_CELL_BOOLEAN', 'XL_CELL_DATE', 'XL_CELL_EMPTY', 'XL_CELL_ERROR', 'XL_CELL_NUMBER', 'XL_CELL_TEXT', 'ZIP_SIGNATURE', '__VERSION__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'biff_text_from_num', 'biffh', 'book', 'cellname', 'cellnameabs', 'colname', 'compdoc', 'count_records', 'decompile_formula', 'dump', 'dump_formula', 'empty_cell', 'error_text_from_code', 'evaluate_name_formula', 'formatting', 'formula', 'info', 'inspect_format', 'oBOOL', 'oERR', 'oNUM', 'oREF', 'oREL', 'oSTRG', 'oUNK', 'okind_dict', 'open_workbook', 'open_workbook_xls', 'os', 'pprint', 'rangename3d', 'rangename3drel', 'sheet', 'sys', 'timemachine', 'xldate', 'xldate_as_datetime', 'xldate_as_tuple', 'zipfile']
fd = pd.read_json('./data/World University Rankings 2021/universities_ranking.json', orient = 'records')
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 948, in _get_data_from_filepath
    self.handles = get_handle(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: './data/World University Rankings 2021/universities_ranking.json'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    fd = pd.read_json('./data/World University Rankings 2021/universities_ranking.json', orient = 'records')
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 829, in read_json
    json_reader = JsonReader(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 931, in __init__
    data = self._get_data_from_filepath(filepath_or_buffer)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 957, in _get_data_from_filepath
    raise FileNotFoundError(
FileNotFoundError: File ./data/World University Rankings 2021/universities_ranking.json does not exist
fd = pd.read_json('./data/World University Rankings 2021/universities_ranking.json', orient = 'records')
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 948, in _get_data_from_filepath
    self.handles = get_handle(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: './data/World University Rankings 2021/universities_ranking.json'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    fd = pd.read_json('./data/World University Rankings 2021/universities_ranking.json', orient = 'records')
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 829, in read_json
    json_reader = JsonReader(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 931, in __init__
    data = self._get_data_from_filepath(filepath_or_buffer)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\json\_json.py", line 957, in _get_data_from_filepath
    raise FileNotFoundError(
FileNotFoundError: File ./data/World University Rankings 2021/universities_ranking.json does not exist
fd = pd.read_json(r"C:\Users\Lenovo\Documents\Day7\world-university-rankings-2021\universities_ranking.json", orient = 'records')
fd
      ranking  ... gender ratio
0           1  ...      46 : 54
1           2  ...      44 : 56
2           3  ...      49 : 51
3           4  ...      36 : 64
4           5  ...      39 : 61
...       ...  ...          ...
1521     1522  ...      42 : 58
1522     1523  ...      57 : 43
1523     1524  ...      54 : 46
1524     1525  ...      59 : 41
1525     1526  ...      34 : 66

[1526 rows x 7 columns]
>>> fd.keys()
Index(['ranking', 'title', 'location', 'number students',
       'students staff ratio', 'perc intl students', 'gender ratio'],
      dtype='str')
>>> pip install pandas-DataReader
SyntaxError: invalid syntax
>>> fd = pd.get_data_fred('GS10')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    fd = pd.get_data_fred('GS10')
AttributeError: module 'pandas' has no attribute 'get_data_fred'
>>> import pandas_datareader as pdr
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    import pandas_datareader as pdr
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas_datareader\__init__.py", line 5, in <module>
    from .data import (
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas_datareader\data.py", line 273, in <module>
    @deprecate_kwarg("access_key", "api_key")
TypeError: deprecate_kwarg() missing 1 required positional argument: 'new_arg_name'
>>> pip install yfinance
...   
SyntaxError: invalid syntax
>>> aapl = yf.download("AAPL", start="2026-01-01", end="2026-06-01")
...   
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    aapl = yf.download("AAPL", start="2026-01-01", end="2026-06-01")
NameError: name 'yf' is not defined. Did you mean: 'y'?
>>> import yfinance as yf
>>> aapl = yf.download("AAPL", start="2026-01-01", end="2026-06-01")

>>> [*********************100%***********************]  1 of 1 completed
aapl
Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date                                                                
2026-01-02  270.507446  277.324767  268.501164  271.755128  37838100
2026-01-05  266.764404  271.006523  265.646486  270.138141  45647200
2026-01-06  261.873474  267.053852  261.633929  266.504884  52352100
2026-01-07  259.847229  263.191023  259.328204  262.711932  48309800
2026-01-08  258.559631  258.809168  255.225814  256.543358  50419300
...                ...         ...         ...         ...       ...
2026-05-22  308.820007  311.399994  305.839996  306.119995  43670200
2026-05-26  308.329987  311.820007  307.670013  309.559998  48000500
2026-05-27  310.850006  313.260010  308.299988  308.329987  50430900
2026-05-28  312.510010  312.799988  309.570007  310.679993  48220400
2026-05-29  312.059998  315.000000  309.529999  311.779999  70026800

>>> [102 rows x 5 columns]
plt.plot(aapl)
>>> [<matplotlib.lines.Line2D object at 0x0000020522F84980>, <matplotlib.lines.Line2D object at 0x0000020522F84AD0>, <matplotlib.lines.Line2D object at 0x0000020522F84C20>, <matplotlib.lines.Line2D object at 0x0000020522F84D70>, <matplotlib.lines.Line2D object at 0x0000020522F84EC0>]
