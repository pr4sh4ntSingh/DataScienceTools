# DataScienceTools
These reprository contains day to day used code that are being used by any Data Scientist in object oriented manner.
I use it extensively for my day to day job. So it is good idea to open source it. You are more than welcome to add more functionalities.

Here I will demonstrate use of this code using famous titanic dataset.

```
import pandas as pd
import description
df=pd.read_csv('train.csv') # this is Titanic dataset. 
```
## Initialize object using your dataset
```
des=description(df)
```
## 1. Show meta information for your dataset.
Most important thing is to feel your dataset before you start doing anything with it. There are some static information about data that is very important to know.
Following function gives static details about dataset like total number of rows and columns, how many columns are for each data type and what are the columns for each data type.

```
des.show_meta()
```
