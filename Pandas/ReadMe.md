# Pandas Tutorial

## Introduction

(pan)el (da)ta

* Do not asign sub dataframes directly do it as:

```python
sDF = DF.copy()
```

* Reset index when adding or modifying rows

* xlx files

```python
oFile = File[:File.rindex('/')] + '/' + File.split('/')[-2] +'_Master.xlsx';
```

* Create a Pandas Excel writer using XlsxWriter as the engine.

writer = pandas.ExcelWriter(oFile, engine='xlsxwriter');

* Write each dataframe to a different worksheet.

```python
for (df, date) in zip(MasterDF, Dates):
	df.to_excel(writer, index = False, sheet_name = date);
```

* Close the Pandas Excel writer and output the Excel file.

```python
writer.save()
```

* A value is trying to be set on a copy of a slice from a DataFrame

```python
tDF.loc[idx, "race"] = race_pred
DFb.loc[:]["Result"] = l;
```


## Commands

1. append row

```python
DF = pandas.DataFrame(columns = ["c1", "c2"]);
DF = pandas.concat([DF, pandas.DataFrame([{"c1" : 0, "c2": 1}])], ignore_index = True);
```

2. Select several columns

```python
DF[["RS-18_0","RS-18_1"]]
```

3. modify values columns pandas by row

```python
sDF = DF_S[DF_S['track'] == val];
p = numpy.array((sDF.x1+sDF.x2)/2 + 1j*(sDF.y1+sDF.y2)/2);
dp = numpy.concatenate((p[WindowSize:],numpy.zeros(WindowSize)));
y = numpy.abs(p-dp);
y[-WindowSize:] = numpy.inf;
DF.loc[sDF.index,'Moving'] = y;
```

4. header names

```python
46. pandas header names
DF = pandas.DataFrame(columns=['filename', 'frame_num', 'x1', 'y1' ,'x2', 'y2', 'Confidence', 'track' , 'Class' ]);


DF = pandas.read_csv(File, names = ["id","x0","y0", "x1","y1", "score"], sep = " ");

```

5. lambda

```python
Y_val = DF['FileName'].apply(lambda x: x.split('-num')[-1]);
Y_val = Y_val.apply(lambda x: int(x.split('.txt')[0]));
```

6. select modify column

```python
DF.iloc[:, [True, False, True, False]]

```

7. add more rows dataframe

```python

Stats = {"Date": str(datetime.datetime.now()), "Model": "ABC", "RunTime": int(34), "Parameters": 34, "Acc": 0.7, "Split": 0.8  , "Settings": "set" }

DF = pandas.concat([DF, pandas.DataFrame([Stats])], ignore_index = True)


```

8. dataframe with specific names

```python
DF = pandas.DataFrame(columns = ["Date", "Model", "RunTime", "Parameters", "Acc", "Split", "Settings"]);
```


9. find substring columns contains string column

```
DF[DF['col'].str.contains('abc')]
```

10. json

```python
x = pandas.read_json(inputfile, lines=True);
```


11. iterate rows

```python
for _ , row in DF.iterrows():
```

70. select columns and rows

```python
DF.iloc[[1,2,3],:]
DF.iloc[:,[1,2,3]]
```

12. change specific rows and columns



13.  concatenate dataframes

```ptyhon
pandas.concat([s1, s2])
DF = pandas.concat([DF1,DF2,DF3,DF4,DF5]);
```

14. rename columns

```python.
DF.rename(columns={"A": "a", "B": "c"})
```

15. append insert new row

```python
DF = pandas.DataFrame(columns=['File', 'Landmark']);

DF = pandas.concat([DF, pandas.DataFrame({"File": File, "Landmark": Landmark}, index=[0])], ignore_index = True);
```

16. vectors to numpy

```python
X = DF["SentenceEmbeddingVector"].apply(lambda x: numpy.fromstring(x[1:-1], dtype = float, sep = ',') );
X = numpy.vstack(X.to_numpy())
```

17. reset index

```python
DF = DF.reset_index(drop = True)
```


18. create dataframe variable column name

```python
DF = pandas.DataFrame(columns=['X_'+str(i) for i in range(2, 16)])
```

19. map values column
```python
DF['variety'] = DF['variety'].map({'Setosa': 0, 'Versicolor': 2, 'Virginica': 4})
```
20. drop columns except

```python
DF.drop(DF.columns.difference(['Moving','Ownership_val','Ownership_speed']), 1, inplace=True);
```

21. Change column data type pandas for correlation

```python
STab["STM"].astype('float').corr(STab["Engagement"].astype('float'))
```

22. Add column prefix

```python
DF = pandas.DataFrame(data = Trajectories);
DF = DF.add_prefix('X_');
DF.to_csv('./CSV/Train_Trajectories.csv', sep=',', index = False);
```

36. at index

```python
for k, row in DF.iterrows():
	if math.isnan(DF.at[k,'track']):
```

23. index of unique values

```python
_, idx = numpy.unique(DF['Foreman'], return_index = True)
```

24. select except rows

```python
DF[DF.index.isin([3,5])]
```


25. sort columns pandas by

```python
DF.sort_values(by=['col1'], ascending = False)
```

26. unique values in column index

```python
DF.sort_index().groupby('Foreman').filter(lambda group: len(group) == 1)
```

27. map lambda column

```python
map_rule = {0: 'male', 1: 'female'}
df['gender_id'] = df['gender'].map(lambda x: map_rule[x])

```

28. apply function multicolum

```python
def fnc(a,b):
	return a-b

DF.apply(lambda x : fnc(x.a, x.b) , axis = 1)

```

29. reading matrix from CSV
```python
DF = pandas.read_csv(Options.File);
X = DF.ZVector.apply(lambda x : numpy.fromstring(x[1:-1], dtype = float, sep = ",")); # Z latent GAN vectors
X = numpy.vstack(X.values);

```

30. insert columns
```python
DF.insert(loc = 1, column = 'Class', value = Cls)
```

31. drop row
```python
DF.drop([0, 1])
```
32. add more columns

```python
DF = DF.reindex(columns = list(DF.columns) + ["RightEye", "LeftEye", "Nose", "RightMouth", "LeftMouth", "BB_Face"]);
```

33. add variable columns names dictionary

```python
	Demographics = {
	"Asian" : [],
	"Indian": [],
	"African": [],
	"Caucasian": [],
	"MiddleEast": [],
	"Latino": [],
	"Target": []};
	
	for _ , row in DF.iterrows():
		sDF = DF_meta[ DF_meta["Class_ID"] == row["ID"] ];
		for k in Demographics.keys():
			Demographics.get(k).append(sDF[k].values[0]);


	for k in Demographics.keys():
		DF = DF.assign(**{k: Demographics.get(k)})
```

34. Sample

```python
DF.sample(frac = 0.5, replace = True, random_state = 1);

```
