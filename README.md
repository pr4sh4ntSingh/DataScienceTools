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
One might not be able to appreciate this function here because there are only 12 columns in this dataset but this information is very much useful if number of columns is more than 100.
```
des.show_meta()
```
Output:
```
---------------------------------------------
No of Rows 891

No of Columns 12
--------------------3 Sample rows-------------
   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  

-----Column Types wise no of column------------
int64      5
object     5
float64    2
dtype: int64

-----Column names group by col type------------
int64
[ PassengerId , Survived , Pclass , SibSp , Parch ,  ]
object
[ Name , Sex , Ticket , Cabin , Embarked ,  ]
float64
[ Age , Fare ,  ]

```

Rest of Read me docs will be published soon. However it's pretty much self-explanatory. 
