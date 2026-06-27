Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
url = "https://ourworldindata.org/explorers/covid.csv?v=1&csvType=full&useColumnShortNames=true&pickerSort=asc&pickerMetric=location&hideControls=false&Metric=Vaccine+doses&Interval=7-day+rolling+average&Relative+to+Population=false&Color+by+test+positivity=false&Relative+to+population=true"
df = pd.read_csv(url, storage_options= {'User-Agent': 'Our World In Data fetch/2.0')
                 
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
df = pd.read_csv(url, storage_options= {'User-Agent': 'Our World In Data fetch/2.0'})
                 
df.head()
                 
        entity code         day  daily_vaccinations_smoothed_per_million
0  Afghanistan  AFG  2021-02-23                                33.679287
1  Afghanistan  AFG  2021-02-24                                33.679287
2  Afghanistan  AFG  2021-02-25                                33.679287
3  Afghanistan  AFG  2021-02-26                                33.679287
4  Afghanistan  AFG  2021-02-27                                33.679287
df.info()
                 
<class 'pandas.DataFrame'>
RangeIndex: 202840 entries, 0 to 202839
Data columns (total 4 columns):
 #   Column                                   Non-Null Count   Dtype  
---  ------                                   --------------   -----  
 0   entity                                   202840 non-null  str    
 1   code                                     202840 non-null  str    
 2   day                                      202840 non-null  str    
 3   daily_vaccinations_smoothed_per_million  202840 non-null  float64
dtypes: float64(1), str(3)
memory usage: 6.2 MB
dir()
                 
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'df', 'pd', 'url']
import numpy as np
import datetime
import matplotlib.pyplot as pdf
del pdf
import matplotlib.pyplot as plt
from datetime import date,datetime,time,timezone
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 202840 entries, 0 to 202839
Data columns (total 4 columns):
 #   Column                                   Non-Null Count   Dtype  
---  ------                                   --------------   -----  
 0   entity                                   202840 non-null  str    
 1   code                                     202840 non-null  str    
 2   day                                      202840 non-null  str    
 3   daily_vaccinations_smoothed_per_million  202840 non-null  float64
dtypes: float64(1), str(3)
memory usage: 6.2 MB
plt.style.use('ggplot')
df.plt(figsize = (20,10))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df.plt(figsize = (20,10))
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'plt'. Did you mean: 'lt'?
df.plot(figsize = (20,10))
<Axes: >
plt.show()
df.columns()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    df.columns()
TypeError: 'Index' object is not callable
df.columns
Index(['entity', 'code', 'day', 'daily_vaccinations_smoothed_per_million'], dtype='str')
df.rolling(window=5).mean()
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 353, in _prep_values
    values = values.to_numpy(np.float64, na_value=np.nan)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\numpy_.py", line 589, in to_numpy
    result = np.asarray(result, dtype=dtype)
ValueError: could not convert string to float: 'Afghanistan'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 470, in _apply_columnwise
    arr = self._prep_values(arr)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 357, in _prep_values
    raise TypeError(f"cannot handle this type -> {values.dtype}") from err
TypeError: cannot handle this type -> str

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    df.rolling(window=5).mean()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 2653, in mean
    return super().mean(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 1706, in mean
    return self._apply(window_func, name="mean", numeric_only=numeric_only)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 595, in _apply
    return self._apply_columnwise(homogeneous_func, name, numeric_only)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\window\rolling.py", line 472, in _apply_columnwise
    raise DataError(
pandas.errors.DataError: Cannot aggregate non-numeric type: str
df['daily_vaccinations_smoothed_per_million'].rolling(window=3).mean()
0                NaN
1                NaN
2          33.679287
3          33.679287
4          33.679287
             ...    
202835    237.862530
202836    237.862530
202837    237.862530
202838    237.862530
202839    237.862530
Name: daily_vaccinations_smoothed_per_million, Length: 202840, dtype: float64
dailvaccinemean = [df['daily_vaccinations_smoothed_per_million'].rolling(window=5).mean()]
dailvaccinemean
[0                NaN
1                NaN
2                NaN
3                NaN
4          33.679287
             ...    
202835    237.862530
202836    237.862530
202837    237.862530
202838    237.862530
202839    237.862530
Name: daily_vaccinations_smoothed_per_million, Length: 202840, dtype: float64]
india = df[df['entity'] == 'India'].copy()
india['day'] = pd.to_datetime(india['day'])
india['7dayrolling'] = (india['daily_vaccinations_smoothed_per_million'].rolling(window=7).mean())
india
      entity code  ... daily_vaccinations_smoothed_per_million  7dayrolling
86239  India  IND  ...                              134.122270          NaN
86240  India  IND  ...                               78.678740          NaN
86241  India  IND  ...                              106.178760          NaN
86242  India  IND  ...                              118.356960          NaN
86243  India  IND  ...                              113.157130          NaN
...      ...  ...  ...                                     ...          ...
87539  India  IND  ...                                0.006113     0.006350
87540  India  IND  ...                                0.005412     0.006160
87541  India  IND  ...                                0.006013     0.006067
87542  India  IND  ...                                0.005512     0.005884
87543  India  IND  ...                                0.005512     0.005756

[1305 rows x 5 columns]
india[['day','daily_vaccinations_smoothed_per_million','rolling_7day']].head(15)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    india[['day','daily_vaccinations_smoothed_per_million','rolling_7day']].head(15)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4384, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 6302, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 6355, in _raise_if_missing
    raise KeyError(f"{not_found} not in index")
KeyError: "['rolling_7day'] not in index"
india
      entity code  ... daily_vaccinations_smoothed_per_million  7dayrolling
86239  India  IND  ...                              134.122270          NaN
86240  India  IND  ...                               78.678740          NaN
86241  India  IND  ...                              106.178760          NaN
86242  India  IND  ...                              118.356960          NaN
86243  India  IND  ...                              113.157130          NaN
...      ...  ...  ...                                     ...          ...
87539  India  IND  ...                                0.006113     0.006350
87540  India  IND  ...                                0.005412     0.006160
87541  India  IND  ...                                0.006013     0.006067
87542  India  IND  ...                                0.005512     0.005884
87543  India  IND  ...                                0.005512     0.005756

[1305 rows x 5 columns]
india[['day','daily_vaccinations_smoothed_per_million','7dayrolling']].head(15)
             day  daily_vaccinations_smoothed_per_million  7dayrolling
86239 2021-01-16                                134.12227          NaN
86240 2021-01-17                                 78.67874          NaN
86241 2021-01-18                                106.17876          NaN
86242 2021-01-19                                118.35696          NaN
86243 2021-01-20                                113.15713          NaN
86244 2021-01-21                                122.01453          NaN
86245 2021-01-22                                139.36633   115.982103
86246 2021-01-23                                139.40923   116.737383
86247 2021-01-24                                139.42757   125.415787
86248 2021-01-25                                157.32270   132.722064
86249 2021-01-26                                135.76369   135.208740
86250 2021-01-27                                155.29172   141.227967
86251 2021-01-28                                188.86812   150.778480
86252 2021-01-29                                211.40940   161.070347
86253 2021-01-30                                216.69083   172.110576
plt.figure(figsize=(30,12))
<Figure size 3000x1200 with 0 Axes>
plt.plot(india['day'],india['daily_vaccinations_smoothed_per_million'],label='Original')
[<matplotlib.lines.Line2D object at 0x000002B8CF3BD6A0>]
plt.plot(india['day'],india['7dayrolling'],label='7-Day Rolling Average',linewidth=3)
[<matplotlib.lines.Line2D object at 0x000002B8CF3BD7F0>]
plt.legend()
<matplotlib.legend.Legend object at 0x000002B8CF3BD010>
plt.show()
stats = df.groupby('entity')['daily_vaccinations_smoothed_per_million'].agg(['count', 'mean', 'std', 'min', 'max'])
stats
                   count         mean          std        min         max
entity                                                                   
Afghanistan         1042   542.489740   873.066372  27.584158   5394.6400
Africa              1350   449.279698   444.243004   0.000000   2901.7104
Albania              973  1122.786926  1361.868404   0.029471   6212.0015
Algeria              583   575.970110  1061.525865   0.000000   5649.5605
Andorra              972  2022.105665  3826.779803   0.488711  22096.4280
...                  ...          ...          ...        ...         ...
Wallis and Futuna    671  2278.680800  5093.166356  87.836200  37599.2150
World               1350  1271.829675  1581.845319   0.000000   5472.3745
Yemen                945    35.793458    46.254427   0.205561    267.9140
Zambia               991   681.685586  1115.643324   2.526287   8946.0550
Zimbabwe            1046   828.473107  1172.654623  19.042805   7551.5660

[229 rows x 5 columns]
import folium
m = folium.Map(location=[12.824992918765316, 80.04509124625007],zoom_start=13)
m
<folium.folium.Map object at 0x000002B8CDF74C20>
m.show_in_browser()
Your map should have been opened in your browser automatically.
Press ctrl+c to return.
m = folium.Map(location=[12.824992918765316, 80.04509124625007],zoom_start=13,tiles="stamenwatercolor")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    m = folium.Map(location=[12.824992918765316, 80.04509124625007],zoom_start=13,tiles="stamenwatercolor")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\folium.py", line 345, in __init__
    tile_layer = TileLayer(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\raster_layers.py", line 142, in __init__
    raise ValueError("Custom tiles must have an attribution.")
ValueError: Custom tiles must have an attribution.
m = folium.Map(location=[12.824992918765316, 80.04509124625007],zoom_start=13,tiles="Stadia.StamenWatercolor")
m.show_in_browser()
Your map should have been opened in your browser automatically.
Press ctrl+c to return.
n = folium.Map(location=[12.824992918765316, 80.04509124625007],zoom_start=13,tiles="CartoDB Positron")
n.show_in_browser()
Your map should have been opened in your browser automatically.
Press ctrl+c to return.
o = folium.Map(location=[12.824992918765316, 80.04509124625007],zoom_start=13,tiles="CartoDB dark\
_matter")
url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
geo = state_geo = f"{url}/us-states.json"
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
pd.read_csv("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/US_Unemployment_Oct2012.csv")
   State  Unemployment
0     AL           7.1
1     AK           6.8
2     AZ           8.1
3     AR           7.2
4     CA          10.1
5     CO           7.7
6     CT           8.4
7     DE           7.1
8     FL           8.2
9     GA           8.8
10    HI           5.4
11    ID           6.6
12    IL           8.8
13    IN           8.4
14    IA           5.1
15    KS           5.6
16    KY           8.1
17    LA           5.9
18    ME           7.2
19    MD           6.8
20    MA           6.7
21    MI           9.1
22    MN           5.6
23    MS           9.1
24    MO           6.7
25    MT           5.8
26    NE           3.9
27    NV          10.3
28    NH           5.7
29    NJ           9.6
30    NM           6.8
31    NY           8.4
32    NC           9.4
33    ND           3.2
34    OH           6.9
35    OK           5.2
36    OR           8.5
37    PA           8.0
38    RI          10.1
39    SC           8.8
40    SD           4.4
41    TN           7.8
42    TX           6.4
43    UT           5.5
44    VT           5.0
45    VA           5.8
46    WA           7.8
47    WV           7.5
48    WI           6.8
49    WY           5.1
>>> state_data = pd.read_csv("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/US_Unemployment_Oct2012.csv")
... 
>>> m = folium.Map(location=[48, -102], zoom_start=3)
>>> folium.Choropleth(
...     geo_data=state_geo,
...     name = "chloropeth",
...     data=df,
...     columns=["State", "Unemployment"],
...     key_on="feature.id",
...     fill_color="YlGn",
...     fill_opacity=0.7,
...     line_opacity=0.2,
...     legend_name="Unemployment Rate (%)"
... ).add_to(m)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    folium.Choropleth(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\folium\features.py", line 1577, in __init__
    color_data = data.set_index(columns[0])[columns[1]].to_dict()  # type: ignore
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 6989, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['State'] are in the columns"
>>> print(df.columns)
Index(['entity', 'code', 'day', 'daily_vaccinations_smoothed_per_million'], dtype='str')
>>> folium.Choropleth(
...     geo_data=state_geo,
...     name = "chloropeth",
...     data=state_data,
...     columns=["State", "Unemployment"],
...     key_on="feature.id",
...     fill_color="YlGn",
...     fill_opacity=0.7,
...     line_opacity=0.2,
...     legend_name="Unemployment Rate (%)"
... ).add_to(m)
<folium.features.Choropleth object at 0x000002B8CF391590>

>>> folium.LayerControl().add_to(m)
<folium.map.LayerControl object at 0x000002B8CF823620>
>>> m
<folium.folium.Map object at 0x000002B8CF842F90>
>>> m.show_in_browser()
Your map should have been opened in your browser automatically.
Press ctrl+c to return.
