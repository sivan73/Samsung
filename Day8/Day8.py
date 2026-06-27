Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas_datareader as pdr
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pandas_datareader as pdr
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas_datareader\__init__.py", line 5, in <module>
    from .data import (
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas_datareader\data.py", line 273, in <module>
    @deprecate_kwarg("access_key", "api_key")
TypeError: deprecate_kwarg() missing 1 required positional argument: 'new_arg_name'
import wbgapi as wb
wb
<module 'wbgapi' from 'C:\\Users\\Lenovo\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\wbgapi\\__init__.py'>
all_indicators = wb.series.info().DataFrame()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    all_indicators = wb.series.info().DataFrame()
AttributeError: 'Featureset' object has no attribute 'DataFrame'
all_indicators = wb.series.DataFrame()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    all_indicators = wb.series.DataFrame()
AttributeError: module 'wbgapi.series' has no attribute 'DataFrame'
import pandas as pd
all_indicators = pd.DataFrame(wb.series.list())
print(all_indicators.iloc[:5, :2])
                  id                                              value
0  AG.CON.FERT.PT.ZS  Fertilizer consumption (% of fertilizer produc...
1     AG.CON.FERT.ZS  Fertilizer consumption (kilograms per hectare ...
2     AG.LND.AGRI.K2                         Agricultural land (sq. km)
3     AG.LND.AGRI.ZS                 Agricultural land (% of land area)
4     AG.LND.ARBL.HA                             Arable land (hectares)
all_indicators
                                              
                     id                                              value
0     AG.CON.FERT.PT.ZS  Fertilizer consumption (% of fertilizer produc...
1        AG.CON.FERT.ZS  Fertilizer consumption (kilograms per hectare ...
2        AG.LND.AGRI.K2                         Agricultural land (sq. km)
3        AG.LND.AGRI.ZS                 Agricultural land (% of land area)
4        AG.LND.ARBL.HA                             Arable land (hectares)
...                 ...                                                ...
1481        VC.IDP.NWCV  Internally displaced persons, new displacement...
1482        VC.IDP.NWDS  Internally displaced persons, new displacement...
1483  VC.IHR.PSRC.FE.P5  Intentional homicides, female (per 100,000 fem...
1484  VC.IHR.PSRC.MA.P5     Intentional homicides, male (per 100,000 male)
1485     VC.IHR.PSRC.P5         Intentional homicides (per 100,000 people)

[1486 rows x 2 columns]
indicator_search = wb.search("Life expectancy")
                                                        
indicator_search
                                                        

indicator_search.iloc[:5,:2]
                                                        
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    indicator_search.iloc[:5,:2]
AttributeError: 'MetadataCollection' object has no attribute 'iloc'
indicator_search = wb.search("life expectancy")
                                                        
indicator_search = pd.DataFrame(wb.search("life expectancy"))
                                                        
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    indicator_search = pd.DataFrame(wb.search("life expectancy"))
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 869, in __init__
    raise ValueError("DataFrame constructor not properly called!")
ValueError: DataFrame constructor not properly called!
indicator_search = pd.DataFrame(wb.search("life expectancy"))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    indicator_search = pd.DataFrame(wb.search("life expectancy"))
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 869, in __init__
    raise ValueError("DataFrame constructor not properly called!")
ValueError: DataFrame constructor not properly called!
indicator_search = pd.DataFrame(wb.series.list(q="life expectancy"))
print(indicator_search.iloc[:5, :2])
                  id                                     value
0  SP.DYN.LE00.FE.IN  Life expectancy at birth, female (years)
1     SP.DYN.LE00.IN   Life expectancy at birth, total (years)
2  SP.DYN.LE00.MA.IN    Life expectancy at birth, male (years)
pivot_result = wb.data.DataFrame('SP.DYN.LE00.IN', time=range(1980, 2000), economy='all')
print(pivot_result.head())
            YR1980     YR1981     YR1982  ...     YR1997     YR1998     YR1999
economy                                   ...                                 
ABW      70.771000  71.344000  71.485000  ...  72.904000  72.940000  72.857000
AFE      49.816713  50.020493  50.290829  ...  51.570887  51.317955  51.807077
AFG      39.258000  39.406000  36.058000  ...  53.212000  52.487000  54.532000
AFW      46.696229  47.075219  47.373942  ...  49.218970  49.452590  49.823913
AGO      42.242000  42.556000  42.857000  ...  46.688000  45.452000  45.808000

[5 rows x 20 columns]
import pandas as pd
song = pd.read_csv(r"C:\Users\Lenovo\Documents\Day8\spotify_global_2019_most_streamed_tracks_audio_features.csv")
song
     Country  ...                                         Artist_img
0     global  ...  https://i.scdn.co/image/4b914c6470c8458674538a...
1     global  ...  https://i.scdn.co/image/2622edec99d68d1d141886...
2     global  ...  https://i.scdn.co/image/b1dfbe843b0b9f54ab2e58...
3     global  ...  https://i.scdn.co/image/c128f5ef4d210a67610acd...
4     global  ...  https://i.scdn.co/image/6bd59cfbd3e1e6394af710...
...      ...  ...                                                ...
1712  global  ...  https://i.scdn.co/image/652b6bb0dfaf8aa444f441...
1713  global  ...  https://i.scdn.co/image/60d0c075d6de8417a0c44d...
1714  global  ...  https://i.scdn.co/image/1d5a05673975ba0c378cd2...
1715  global  ...  https://i.scdn.co/image/984dfbcdcf7880b022478b...
1716  global  ...  https://i.scdn.co/image/f9e65e111cbb16276d2c27...

[1717 rows x 24 columns]
song.head(10)
  Country  ...                                         Artist_img
0  global  ...  https://i.scdn.co/image/4b914c6470c8458674538a...
1  global  ...  https://i.scdn.co/image/2622edec99d68d1d141886...
2  global  ...  https://i.scdn.co/image/b1dfbe843b0b9f54ab2e58...
3  global  ...  https://i.scdn.co/image/c128f5ef4d210a67610acd...
4  global  ...  https://i.scdn.co/image/6bd59cfbd3e1e6394af710...
5  global  ...  https://i.scdn.co/image/01dae15758ba1a3d18e6e3...
6  global  ...  https://i.scdn.co/image/ea76c82c05174105751f85...
7  global  ...  https://i.scdn.co/image/5ed13d249e562fea4e296a...
8  global  ...  https://i.scdn.co/image/eb88f6dde0844337248826...
9  global  ...  https://i.scdn.co/image/93fec27f9aac86526b9010...

[10 rows x 24 columns]
song.info()
<class 'pandas.DataFrame'>
RangeIndex: 1717 entries, 0 to 1716
Data columns (total 24 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Country            1717 non-null   str    
 1   Rank               1717 non-null   float64
 2   Track_id           1717 non-null   str    
 3   Streams            1717 non-null   int64  
 4   Track Name         1717 non-null   str    
 5   Artist             1717 non-null   str    
 6   URL                1717 non-null   str    
 7   acousticness       1717 non-null   float64
 8   danceability       1717 non-null   float64
 9   energy             1717 non-null   float64
 10  instrumentalness   1717 non-null   float64
 11  liveness           1717 non-null   float64
 12  loudness           1717 non-null   float64
 13  speechiness        1717 non-null   float64
 14  valence            1717 non-null   float64
 15  tempo              1717 non-null   float64
 16  time_signature     1717 non-null   int64  
 17  duration_ms        1717 non-null   int64  
 18  key                1717 non-null   int64  
 19  mode               1717 non-null   int64  
 20  Artist_id          1717 non-null   str    
 21  Artist_popularity  1717 non-null   int64  
 22  Artist_follower    1717 non-null   int64  
 23  Artist_img         1717 non-null   str    
dtypes: float64(10), int64(7), str(7)
memory usage: 322.1 KB
song.describe()
              Rank       Streams  ...  Artist_popularity  Artist_follower
count  1717.000000  1.717000e+03  ...        1717.000000     1.717000e+03
mean    859.000000  5.166175e+07  ...          87.246942     8.645130e+06
std     495.799523  1.047532e+08  ...           7.808209     1.105793e+07
min       1.000000  5.242300e+05  ...          47.000000     1.090000e+02
25%     430.000000  1.763026e+06  ...          83.000000     1.370858e+06
50%     859.000000  9.623926e+06  ...          87.000000     3.998147e+06
75%    1288.000000  4.829352e+07  ...          93.000000     1.099547e+07
max    1717.000000  1.166186e+09  ...         100.000000     5.746376e+07

[8 rows x 17 columns]
song.columns()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    song.columns()
TypeError: 'Index' object is not callable
df = song[["Rank","Artist","Track Name","Artist_popularity","Streams","tempo","danceability","energy"]]
df.head()
   Rank         Artist        Track Name  ...    tempo  danceability  energy
0   1.0        Ava Max  Sweet but Psycho  ...  133.002         0.719   0.704
1   2.0  Billie Eilish           bad guy  ...  135.128         0.701   0.425
2   3.0  Ariana Grande           7 rings  ...  140.048         0.778   0.317
3   4.0    Tones and I      Dance Monkey  ...   98.078         0.825   0.593
4   5.0   Shawn Mendes          Señorita  ...  116.967         0.759   0.548

[5 rows x 8 columns]
pop_song = df[df["Artist_popularity"]>90]
pop_song.head()
   Rank         Artist    Track Name  ...    tempo  danceability  energy
1   2.0  Billie Eilish       bad guy  ...  135.128         0.701   0.425
2   3.0  Ariana Grande       7 rings  ...  140.048         0.778   0.317
3   4.0    Tones and I  Dance Monkey  ...   98.078         0.825   0.593
4   5.0   Shawn Mendes      Señorita  ...  116.967         0.759   0.548
5   6.0   Daddy Yankee     Con Calma  ...   93.989         0.737   0.860

[5 rows x 8 columns]
rank = pop_song["Artist"].value_counts()
rank
Artist
Post Malone      45
Juice WRLD       31
Ariana Grande    28
Billie Eilish    27
Taylor Swift     27
                 ..
Eminem            1
Nicki Minaj       1
Rihanna           1
Bass Santana      1
Bruno Mars        1
Name: count, Length: 62, dtype: int64
type(rank)
<class 'pandas.Series'>
pop_song["Artist"].unique()
<StringArray>
[             'Billie Eilish',              'Ariana Grande',
                'Tones and I',               'Shawn Mendes',
               'Daddy Yankee',              'Lewis Capaldi',
                'Post Malone',                     'Halsey',
                  'Sam Smith',                 'Ed Sheeran',
                   'Anuel AA',                  'Bad Bunny',
                    'J. Cole',               'Travis Scott',
                 'Juice WRLD',                   'Maroon 5',
                     'Khalid',                       'Sech',
                      'Drake',               'XXXTENTACION',
                       'Lauv',                   'J Balvin',
     'A Boogie Wit da Hoodie',            'Imagine Dragons',
                      'Queen',                      'Ozuna',
                  'Nicky Jam',                     'Maluma',
                'Chris Brown',                   'Lil Baby',
                     'DaBaby',                        'BTS',
               'Selena Gomez',                    'Cardi B',
                   'Dua Lipa',             'Camila Cabello',
                      'Dalex',           'The Chainsmokers',
                 'Young Thug',                       'Tyga',
               'Taylor Swift',              'Justin Quiles',
                    'KAROL G',                'Myke Towers',
               'Lil Uzi Vert',               'Harry Styles',
                 'The Weeknd',                 'Kanye West',
              'Michael Bublé',              'Justin Bieber',
                'Roddy Ricch',             'Kendrick Lamar',
                     'Future', 'YoungBoy Never Broke Again',
                   'Coldplay',                     'Eminem',
                'Nicki Minaj',               'Trippie Redd',
                      'Gunna',                    'Rihanna',
               'Bass Santana',                 'Bruno Mars']
Length: 62, dtype: str
'BTS' in rank
True
bts
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    bts
NameError: name 'bts' is not defined
plt.show
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    plt.show
NameError: name 'plt' is not defined
import matplotlib
plt.show
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    plt.show
NameError: name 'plt' is not defined
matplotlib.show
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    matplotlib.show
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\_api\__init__.py", line 232, in __getattr__
    raise AttributeError(
AttributeError: module 'matplotlib' has no attribute 'show'
matplotlib.show()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    matplotlib.show()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\_api\__init__.py", line 232, in __getattr__
    raise AttributeError(
AttributeError: module 'matplotlib' has no attribute 'show'
import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
import matlotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    import matlotlib.pyplot as plt
ModuleNotFoundError: No module named 'matlotlib'
import matplotlib.pyplot as plt
plt.show()
pop_song
        Rank         Artist  ... danceability  energy
1        2.0  Billie Eilish  ...        0.701   0.425
2        3.0  Ariana Grande  ...        0.778   0.317
3        4.0    Tones and I  ...        0.825   0.593
4        5.0   Shawn Mendes  ...        0.759   0.548
5        6.0   Daddy Yankee  ...        0.737   0.860
...      ...            ...  ...          ...     ...
1694  1695.0   Bass Santana  ...        0.936   0.514
1696  1697.0   XXXTENTACION  ...        0.726   0.419
1701  1702.0      Nicky Jam  ...        0.595   0.773
1708  1709.0          Queen  ...        0.535   0.650
1709  1710.0     Bruno Mars  ...        0.704   0.859

[618 rows x 8 columns]
x = pop_song["energy"]
y = pop_song["Rank"]
plt.scatter(x,y, color ="red", alpha = 0.5)
<matplotlib.collections.PathCollection object at 0x0000018F8928EF90>
plt.show()
cor = pop_song(method = 'pearson',numeric_only = True)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    cor = pop_song(method = 'pearson',numeric_only = True)
TypeError: 'DataFrame' object is not callable
pandas.DataFrame.corr(method='pearson')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    pandas.DataFrame.corr(method='pearson')
NameError: name 'pandas' is not defined
pd
<module 'pandas' from 'C:\\Users\\Lenovo\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pandas\\__init__.py'>
pd.DataFrame.corr(method='pearson')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    pd.DataFrame.corr(method='pearson')
TypeError: DataFrame.corr() missing 1 required positional argument: 'self'
pd.df.corr(method='pearson')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    pd.df.corr(method='pearson')
AttributeError: module 'pandas' has no attribute 'df'
df
        Rank              Artist  ... danceability  energy
0        1.0             Ava Max  ...        0.719   0.704
1        2.0       Billie Eilish  ...        0.701   0.425
2        3.0       Ariana Grande  ...        0.778   0.317
3        4.0         Tones and I  ...        0.825   0.593
4        5.0        Shawn Mendes  ...        0.759   0.548
...      ...                 ...  ...          ...     ...
1712  1713.0                 Sia  ...        0.628   0.698
1713  1714.0                  LX  ...        0.764   0.744
1714  1715.0            Bee Gees  ...        0.708   0.567
1715  1716.0    MC Kevin o Chris  ...        0.896   0.756
1716  1717.0  Henrique & Juliano  ...        0.690   0.670

[1717 rows x 8 columns]
correlation_matrix = df.corr(method='pearson')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    correlation_matrix = df.corr(method='pearson')
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 13133, in corr
    mat = data.to_numpy(dtype=float, na_value=np.nan, copy=False)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 2081, in to_numpy
    result = self._mgr.as_array(dtype=dtype, copy=copy, na_value=na_value)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\managers.py", line 1872, in as_array
    arr = self._interleave(dtype=dtype, na_value=na_value)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\internals\managers.py", line 1925, in _interleave
    arr = blk.values.to_numpy(  # type: ignore[union-attr]
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\arrays\numpy_.py", line 589, in to_numpy
    result = np.asarray(result, dtype=dtype)
ValueError: could not convert string to float: 'Ava Max'
corr
  
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    corr
NameError: name 'corr' is not defined
cor
  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    cor
NameError: name 'cor' is not defined. Did you mean: 'chr'?
cor = pop_song.corr
  
cor
  
<bound method DataFrame.corr of         Rank         Artist  ... danceability  energy
1        2.0  Billie Eilish  ...        0.701   0.425
2        3.0  Ariana Grande  ...        0.778   0.317
3        4.0    Tones and I  ...        0.825   0.593
4        5.0   Shawn Mendes  ...        0.759   0.548
5        6.0   Daddy Yankee  ...        0.737   0.860
...      ...            ...  ...          ...     ...
1694  1695.0   Bass Santana  ...        0.936   0.514
1696  1697.0   XXXTENTACION  ...        0.726   0.419
1701  1702.0      Nicky Jam  ...        0.595   0.773
1708  1709.0          Queen  ...        0.535   0.650
1709  1710.0     Bruno Mars  ...        0.704   0.859

[618 rows x 8 columns]>
plt.matshow(cor)
  
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    plt.matshow(cor)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\pyplot.py", line 2677, in matshow
    figsize = figaspect(A)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\figure.py", line 3713, in figaspect
    nr, nc = arg.shape[:2]
ValueError: not enough values to unpack (expected 2, got 0)
cor = pop_song.corr(method='pearson',numeric_only = True)
  
cor
  
                       Rank  Artist_popularity  ...  danceability    energy
Rank               1.000000          -0.125771  ...     -0.014811  0.015078
Artist_popularity -0.125771           1.000000  ...     -0.084745  0.019909
Streams           -0.667177           0.076414  ...      0.084925 -0.061912
tempo              0.055495           0.033521  ...      0.040506  0.245615
danceability      -0.014811          -0.084745  ...      1.000000  0.116359
energy             0.015078           0.019909  ...      0.116359  1.000000

[6 rows x 6 columns]
plt.matshow(cor)
  
<matplotlib.image.AxesImage object at 0x0000018F89643E00>
plt.colorbar()
  
<matplotlib.colorbar.Colorbar object at 0x0000018F89EA81A0>
plt.show()
  
plt.figure(figsize=(8,6))
  
<Figure size 800x600 with 0 Axes>
import seaborn
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    import seaborn
ModuleNotFoundError: No module named 'seaborn'
import seaborn as sns
sns.heatmap(cor,anot=True)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    sns.heatmap(cor,anot=True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\seaborn\matrix.py", line 459, in heatmap
    plotter.plot(ax, cbar_ax, kwargs)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\seaborn\matrix.py", line 306, in plot
    mesh = ax.pcolormesh(self.plot_data, cmap=self.cmap, **kws)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\__init__.py", line 1524, in inner
    return func(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\axes\_axes.py", line 6534, in pcolormesh
    collection = mcoll.QuadMesh(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\collections.py", line 2390, in __init__
    Collection.__init__(self, **kwargs)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\collections.py", line 209, in __init__
    self._internal_update(kwargs)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\artist.py", line 1235, in _internal_update
    return self._update_props(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\artist.py", line 1208, in _update_props
    raise AttributeError(
AttributeError: QuadMesh.set() got an unexpected keyword argument 'anot'
sns.heatmap(cor, annot= True)
<Axes: >
plt.show
<function show at 0x0000018F891FE140>
plt.show()
df2 = sns.load_dataset('titanic', cache = Ture)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    df2 = sns.load_dataset('titanic', cache = Ture)
NameError: name 'Ture' is not defined
df2 = sns.load_dataset('titanic', cache = True)
df2
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0           0       3    male  22.0  ...   NaN  Southampton     no  False
1           1       1  female  38.0  ...     C    Cherbourg    yes  False
2           1       3  female  26.0  ...   NaN  Southampton    yes   True
3           1       1  female  35.0  ...     C  Southampton    yes  False
4           0       3    male  35.0  ...   NaN  Southampton     no   True
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
886         0       2    male  27.0  ...   NaN  Southampton     no   True
887         1       1  female  19.0  ...     B  Southampton    yes   True
888         0       3  female   NaN  ...   NaN  Southampton     no  False
889         1       1    male  26.0  ...     C    Cherbourg    yes   True
890         0       3    male  32.0  ...   NaN   Queenstown     no   True

[891 rows x 15 columns]
df2.describe()
         survived      pclass         age       sibsp       parch        fare
count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
df2.shape()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    df2.shape()
TypeError: 'tuple' object is not callable
df2.shape
(891, 15)
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 1717 entries, 0 to 1716
Data columns (total 8 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Rank               1717 non-null   float64
 1   Artist             1717 non-null   str    
 2   Track Name         1717 non-null   str    
 3   Artist_popularity  1717 non-null   int64  
 4   Streams            1717 non-null   int64  
 5   tempo              1717 non-null   float64
 6   danceability       1717 non-null   float64
 7   energy             1717 non-null   float64
dtypes: float64(4), int64(2), str(2)
memory usage: 107.4 KB
df['deck'].value_counts(dropna=True)
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'deck'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    df['deck'].value_counts(dropna=True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'deck'
deck
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    deck
NameError: name 'deck' is not defined
df2.deck
0      NaN
1        C
2      NaN
3        C
4      NaN
      ... 
886    NaN
887      B
888    NaN
889      C
890    NaN
Name: deck, Length: 891, dtype: category
Categories (7, str): ['A', 'B', 'C', 'D', 'E', 'F', 'G']
df2['deck'].value_counts(dropna= True)
deck
C    59
B    47
D    33
E    32
A    15
F    13
G     4
Name: count, dtype: int64
df2.isnull()
     survived  pclass    sex    age  ...   deck  embark_town  alive  alone
0       False   False  False  False  ...   True        False  False  False
1       False   False  False  False  ...  False        False  False  False
2       False   False  False  False  ...   True        False  False  False
3       False   False  False  False  ...  False        False  False  False
4       False   False  False  False  ...   True        False  False  False
..        ...     ...    ...    ...  ...    ...          ...    ...    ...
886     False   False  False  False  ...   True        False  False  False
887     False   False  False  False  ...  False        False  False  False
888     False   False  False   True  ...   True        False  False  False
889     False   False  False  False  ...  False        False  False  False
890     False   False  False  False  ...   True        False  False  False

[891 rows x 15 columns]
df2.notnull()
     survived  pclass   sex    age  ...   deck  embark_town  alive  alone
0        True    True  True   True  ...  False         True   True   True
1        True    True  True   True  ...   True         True   True   True
2        True    True  True   True  ...  False         True   True   True
3        True    True  True   True  ...   True         True   True   True
4        True    True  True   True  ...  False         True   True   True
..        ...     ...   ...    ...  ...    ...          ...    ...    ...
886      True    True  True   True  ...  False         True   True   True
887      True    True  True   True  ...   True         True   True   True
888      True    True  True  False  ...  False         True   True   True
889      True    True  True   True  ...   True         True   True   True
890      True    True  True   True  ...  False         True   True   True

[891 rows x 15 columns]
df.isnull().sum()
Rank                 0
Artist               0
Track Name           0
Artist_popularity    0
Streams              0
tempo                0
danceability         0
energy               0
dtype: int64
df.notnull().sum()
Rank                 1717
Artist               1717
Track Name           1717
Artist_popularity    1717
Streams              1717
tempo                1717
danceability         1717
energy               1717
dtype: int64
df2.isnull().sum()
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
df2.notnull().sum()
survived       891
pclass         891
sex            891
age            714
sibsp          891
parch          891
fare           891
embarked       889
class          891
who            891
adult_male     891
deck           203
embark_town    889
alive          891
alone          891
dtype: int64
df2.isnull().sum().sum()
np.int64(869)
df2.isnotnull().sum().sum()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    df2.isnotnull().sum().sum()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'isnotnull'. Did you mean: 'notnull'?
df2.notnull().sum().sum()
np.int64(12496)
(len(df2)-df2.count()).sum()
np.int64(869)
df2.dropna()
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
1           1       1  female  38.0  ...     C    Cherbourg    yes  False
3           1       1  female  35.0  ...     C  Southampton    yes  False
6           0       1    male  54.0  ...     E  Southampton     no   True
10          1       3  female   4.0  ...     G  Southampton    yes  False
11          1       1  female  58.0  ...     C  Southampton    yes   True
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
871         1       1  female  47.0  ...     D  Southampton    yes  False
872         0       1    male  33.0  ...     B  Southampton     no   True
879         1       1  female  56.0  ...     C    Cherbourg    yes  False
887         1       1  female  19.0  ...     B  Southampton    yes   True
889         1       1    male  26.0  ...     C    Cherbourg    yes   True

[182 rows x 15 columns]
age_df = df.dropna(axis = 0, how = 'any', subset = ['age'])
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    age_df = df.dropna(axis = 0, how = 'any', subset = ['age'])
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 7801, in dropna
    raise KeyError(np.array(subset)[check].tolist())
KeyError: ['age']
age_df = df2.dropna(axis = 0, how = 'any', subset = ['age'])
age_df
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0           0       3    male  22.0  ...   NaN  Southampton     no  False
1           1       1  female  38.0  ...     C    Cherbourg    yes  False
2           1       3  female  26.0  ...   NaN  Southampton    yes   True
3           1       1  female  35.0  ...     C  Southampton    yes  False
4           0       3    male  35.0  ...   NaN  Southampton     no   True
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
885         0       3  female  39.0  ...   NaN   Queenstown     no  False
886         0       2    male  27.0  ...   NaN  Southampton     no   True
887         1       1  female  19.0  ...     B  Southampton    yes   True
889         1       1    male  26.0  ...     C    Cherbourg    yes   True
890         0       3    male  32.0  ...   NaN   Queenstown     no   True

[714 rows x 15 columns]
no = df2.dropna()
no.isnull().sum()
survived       0
pclass         0
sex            0
age            0
sibsp          0
parch          0
fare           0
embarked       0
class          0
who            0
adult_male     0
deck           0
embark_town    0
alive          0
alone          0
dtype: int64
df3 = sns.load_dataset('titanic', cache= True)
df3
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0           0       3    male  22.0  ...   NaN  Southampton     no  False
1           1       1  female  38.0  ...     C    Cherbourg    yes  False
2           1       3  female  26.0  ...   NaN  Southampton    yes   True
3           1       1  female  35.0  ...     C  Southampton    yes  False
4           0       3    male  35.0  ...   NaN  Southampton     no   True
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
886         0       2    male  27.0  ...   NaN  Southampton     no   True
887         1       1  female  19.0  ...     B  Southampton    yes   True
888         0       3  female   NaN  ...   NaN  Southampton     no  False
889         1       1    male  26.0  ...     C    Cherbourg    yes   True
890         0       3    male  32.0  ...   NaN   Queenstown     no   True

[891 rows x 15 columns]
df3.head()
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True

[5 rows x 15 columns]
df3['age'].head(10)
0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
5     NaN
6    54.0
7     2.0
8    27.0
9    14.0
Name: age, dtype: float64
avg_age = df['age'].mean(axis= 0)
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    avg_age = df['age'].mean(axis= 0)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'age'
avg_age = df3['age'].mean(axis = 0)
avg_age
np.float64(29.69911764705882)
medianage = df3['age'].median(axis = 0)
medianage
np.float64(28.0)
df3.age
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ... 
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: age, Length: 891, dtype: float64
df3['age'].fillna(avg_age, inplace = True)

Warning (from warnings module):
  File "<pyshell#111>", line 1
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
Such inplace method never works to update the original DataFrame or Series, because the intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' instead, to perform the operation inplace on the original object, or try to avoid an inplace operation using 'df[col] = df[col].method(value)'.

See the documentation for a more detailed explanation: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html
0      22.000000
1      38.000000
2      26.000000
3      35.000000
4      35.000000
         ...    
886    27.000000
887    19.000000
888    29.699118
889    26.000000
890    32.000000
Name: age, Length: 891, dtype: float64
df3.fillna({'age'}, inplace= True)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    df3.fillna({'age'}, inplace= True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 7163, in fillna
    raise ValueError(f"invalid fill value with a {type(value)}")
ValueError: invalid fill value with a <class 'set'>
df3.fillna({col:'age'}, inplace = True)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    df3.fillna({col:'age'}, inplace = True)
NameError: name 'col' is not defined. Did you mean: 'cor'?
df3.age
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ... 
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: age, Length: 891, dtype: float64
df3.fillna({'age':888}, inplace = True)
     survived  pclass     sex    age  ...  deck  embark_town  alive  alone
0           0       3    male   22.0  ...   NaN  Southampton     no  False
1           1       1  female   38.0  ...     C    Cherbourg    yes  False
2           1       3  female   26.0  ...   NaN  Southampton    yes   True
3           1       1  female   35.0  ...     C  Southampton    yes  False
4           0       3    male   35.0  ...   NaN  Southampton     no   True
..        ...     ...     ...    ...  ...   ...          ...    ...    ...
886         0       2    male   27.0  ...   NaN  Southampton     no   True
887         1       1  female   19.0  ...     B  Southampton    yes   True
888         0       3  female  888.0  ...   NaN  Southampton     no  False
889         1       1    male   26.0  ...     C    Cherbourg    yes   True
890         0       3    male   32.0  ...   NaN   Queenstown     no   True

[891 rows x 15 columns]
df3['age'] = df3['age'].fillna(avg_age)
df2.isna()
     survived  pclass    sex    age  ...   deck  embark_town  alive  alone
0       False   False  False  False  ...   True        False  False  False
1       False   False  False  False  ...  False        False  False  False
2       False   False  False  False  ...   True        False  False  False
3       False   False  False  False  ...  False        False  False  False
4       False   False  False  False  ...   True        False  False  False
..        ...     ...    ...    ...  ...    ...          ...    ...    ...
886     False   False  False  False  ...   True        False  False  False
887     False   False  False  False  ...  False        False  False  False
888     False   False  False   True  ...   True        False  False  False
889     False   False  False  False  ...  False        False  False  False
890     False   False  False  False  ...   True        False  False  False

[891 rows x 15 columns]
df3.isnull()
     survived  pclass    sex    age  ...   deck  embark_town  alive  alone
0       False   False  False  False  ...   True        False  False  False
1       False   False  False  False  ...  False        False  False  False
2       False   False  False  False  ...   True        False  False  False
3       False   False  False  False  ...  False        False  False  False
4       False   False  False  False  ...   True        False  False  False
..        ...     ...    ...    ...  ...    ...          ...    ...    ...
886     False   False  False  False  ...   True        False  False  False
887     False   False  False  False  ...  False        False  False  False
888     False   False  False  False  ...   True        False  False  False
889     False   False  False  False  ...  False        False  False  False
890     False   False  False  False  ...   True        False  False  False

[891 rows x 15 columns]
df3['age'].isna()
0      False
1      False
2      False
3      False
4      False
       ...  
886    False
887    False
888    False
889    False
890    False
Name: age, Length: 891, dtype: bool
df3['age'].isna().sum()
np.int64(0)
df3.describe()
         survived      pclass         age       sibsp       parch        fare
count  891.000000  891.000000  891.000000  891.000000  891.000000  891.000000
mean     0.383838    2.308642  200.203333    0.523008    0.381594   32.204208
std      0.486592    0.836071  342.889268    1.102743    0.806057   49.693429
min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%      0.000000    2.000000   22.000000    0.000000    0.000000    7.910400
50%      0.000000    3.000000   32.000000    0.000000    0.000000   14.454200
75%      1.000000    3.000000   54.000000    1.000000    0.000000   31.000000
max      1.000000    3.000000  888.000000    8.000000    6.000000  512.329200
df3.isnull().sum()
survived         0
pclass           0
sex              0
age              0
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
df3['embarked'].dropna()
0      S
1      C
2      S
3      S
4      S
      ..
886    S
887    S
888    S
889    C
890    Q
Name: embarked, Length: 889, dtype: str
df3.insnull().sum()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    df3.insnull().sum()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'insnull'. Did you mean: 'isnull'?
df3.isnull().sum()
survived         0
pclass           0
sex              0
age              0
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
df3['embarked'].isnull()
0      False
1      False
2      False
3      False
4      False
       ...  
886    False
887    False
888    False
889    False
890    False
Name: embarked, Length: 891, dtype: bool
df3['embarked'].isnull().sum()
np.int64(2)
df3['embarked'].dropnull()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    df3['embarked'].dropnull()
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6206, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'dropnull'. Did you mean: 'notnull'?
df3['embarked'].dropna()
0      S
1      C
2      S
3      S
4      S
      ..
886    S
887    S
888    S
889    C
890    Q
Name: embarked, Length: 889, dtype: str
df3['embarked'].dropna().sum()
'SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQSQQCSSSCSCSSCSSCSSCCSSSSSSSCSSSSSSSSQSSSSSSSSSSSSSCCSSSSSSSSSSSQSCSSCSQSCSSSCSSCQSCSCSSSSCSSSCCSSQSSSSSSSSSSSCQSSSSSSSSSSSSSSQSSCSSCSSSCSSSSQSQSSSSSCCQSQSSSSCSSSCQCSSSSQCSSCSSSSSSSSSSSSSSSSSSSSSCQSSCQSSSSSSSSSCCSCSQSSSQSSSSSSSSCQSSSQSQSSSSCSSSQSCCSSCCSSCQQSQSSCCCCCCSSSSSSSCSSQSSCSSSCQSSSSSSCSSSSSSSSSSSSSSCSCSSSQQSCCSQSCCQCCSSCSCSCCSCCSSSSSSQCSSSCSSSSSSSSSSSSSSSSSQQSSSSSSSCQSSSSSSQSSSSSSSSSSSSSSSSSSSCSSSCCSCSSSQSSSSSSSSQCSSSCSSSSSSSSSSCSSCSSSSSCSCCSSSSQQSSCSSSSQSSCSSSQSSSSCCCQSSSSSCCCSSSCSCSSSSCSSCSSCSQCSSCCSSQSSSSSSSCSSSSQSSSSCSSCSCCSSCSSSCSQSSSSCCSSSSCSSSCSSSQQSSSSSSCSCSSSQSSQSSCSSSSSSSSCSSCCSCSSSSSQQSSQSCSCSSSSSSSSSSSSSSSSSCQCSSSCSSSSSCSCSSSQCSCSCQSSSSSCCSSSSSCSQSSSSSSSSQSSSCSSSSSCSSSSCSSSSSSQSSSSSSSSSSSSCSSSCQQSSSSCSSQSQSCSSSSSSQSCQSSCSSSSCSSSSCSSSSSSSSSSSSSCSSSSSSSQSCQCSCSSCSSSCSSCCSSSCSCSSCSSSSSCCSSSSSSCSSSSSSSCCSSSCSSSSSQSSSCQ'
df3['embarked'] = df3['embarked'].dropna().sum()
df3.embarked
0      SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
1      SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
2      SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
3      SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
4      SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
                             ...                        
886    SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
887    SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
888    SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
889    SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
890    SCSSSQSSSCSSSSSSQSSCSSQSSSCSQSCCQSCSCSSCSSCCQS...
Name: embarked, Length: 891, dtype: str
df3.isnull().sum()
survived         0
pclass           0
sex              0
age              0
sibsp            0
parch            0
fare             0
embarked         0
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
df3['deck'] = df3['embarked'].dropna()
df3.isnull().sum()
survived       0
pclass         0
sex            0
age            0
sibsp          0
parch          0
fare           0
embarked       0
class          0
who            0
adult_male     0
deck           0
embark_town    2
alive          0
alone          0
dtype: int64
df3['embark_town'] = df3['embark_town'].dropna()
df3.isnull().sum()
survived       0
pclass         0
sex            0
age            0
sibsp          0
parch          0
fare           0
embarked       0
class          0
who            0
adult_male     0
deck           0
embark_town    2
alive          0
alone          0
dtype: int64
df3['embark_town'] = df3['embark_town'].fillna('na')
df3.isnull().sum()
survived       0
pclass         0
sex            0
age            0
sibsp          0
parch          0
fare           0
embarked       0
class          0
who            0
adult_male     0
deck           0
embark_town    0
alive          0
alone          0
dtype: int64
df3.embark_town
0      Southampton
1        Cherbourg
2      Southampton
3      Southampton
4      Southampton
          ...     
886    Southampton
887    Southampton
888    Southampton
889      Cherbourg
890     Queenstown
Name: embark_town, Length: 891, dtype: str
town_count = df['embark_town'].value_counts(dropna = True)
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'embark_town'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    town_count = df['embark_town'].value_counts(dropna = True)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'embark_town'
town_count = df3['embark_town'].value_counts(dropna = True)
town_count
embark_town
Southampton    644
Cherbourg      168
Queenstown      77
na               2
Name: count, dtype: int64
most=town_count.idxmax()
most
'Southampton'
student_data = pd.read_csv("./data/student/student-mat.csv")
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    student_data = pd.read_csv("./data/student/student-mat.csv")
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 930, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: './data/student/student-mat.csv'
student_data = pd.read_csv(r"C:\Users\Lenovo\Downloads\student-mat.csv")
student_data
    school;sex;age;address;famsize;Pstatus;Medu;Fedu;Mjob;Fjob;reason;guardian;traveltime;studytime;failures;schoolsup;famsup;paid;activities;nursery;higher;internet;romantic;famrel;freetime;goout;Dalc;Walc;health;absences;G1;G2;G3
0    GP;"F";18;"U";"GT3";"A";4;4;"at_home";"teacher...                                                                                                                                                                                 
1    GP;"F";17;"U";"GT3";"T";1;1;"at_home";"other";...                                                                                                                                                                                 
2    GP;"F";15;"U";"LE3";"T";1;1;"at_home";"other";...                                                                                                                                                                                 
3    GP;"F";15;"U";"GT3";"T";4;2;"health";"services...                                                                                                                                                                                 
4    GP;"F";16;"U";"GT3";"T";3;3;"other";"other";"h...                                                                                                                                                                                 
..                                                 ...                                                                                                                                                                                 
390  MS;"M";20;"U";"LE3";"A";2;2;"services";"servic...                                                                                                                                                                                 
391  MS;"M";17;"U";"LE3";"T";3;1;"services";"servic...                                                                                                                                                                                 
392  MS;"M";21;"R";"GT3";"T";1;1;"other";"other";"c...                                                                                                                                                                                 
393  MS;"M";18;"R";"LE3";"T";3;2;"services";"other"...                                                                                                                                                                                 
394  MS;"M";19;"U";"LE3";"T";1;1;"other";"at_home";...                                                                                                                                                                                 

[395 rows x 1 columns]
>>> plt.hist(student_data['absences'])
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'absences'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    plt.hist(student_data['absences'])
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Lenovo\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'absences'
>>> student_data.columns()
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    student_data.columns()
TypeError: 'Index' object is not callable
>>> student_data.describe()
       school;sex;age;address;famsize;Pstatus;Medu;Fedu;Mjob;Fjob;reason;guardian;traveltime;studytime;failures;schoolsup;famsup;paid;activities;nursery;higher;internet;romantic;famrel;freetime;goout;Dalc;Walc;health;absences;G1;G2;G3
count                                                 395                                                                                                                                                                                 
unique                                                395                                                                                                                                                                                 
top     GP;"F";18;"U";"GT3";"A";4;4;"at_home";"teacher...                                                                                                                                                                                 
freq                                                    1                                                                                                                                                                                 
