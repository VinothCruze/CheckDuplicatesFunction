# CheckduplicateFunction

Function to test the dataframe columns for duplicate values
Function is present under [/src/check_duplicate.py](https://github.com/VinothCruze/CheckDuplicatesFunction/blob/main/src/check_duplicate.py)


## Usage:
```
from check_duplicate import check_duplicates
## define dataframe with column and values
result = check_duplicates(dataframe, ['col_1', 'col_2', 'col_3'])
print(result)
```

## Edge case handling:

1)  checked whether the passed dataframe is of pandas dataframe **(if not isinstance(dataframe, pd.DataFrame))**
2)  checked whether the passed dataframe is empty or not **if (dataframe.empty:)**
3)  checked whether the provided columns present in the dataframe **columns_undefined section**
4)  checked whether the provided column(s) arent empty **if dataframe.empty**
5)  ensured the return type to dictionary type


## Outputs:
-- check_duplicates(dataframe, ['col_1'])
```
           {'count': 7, 'samples': [{'col_1': 'A', 'number_of_duplicates': 4}, 
                                    {'col_1': 'B', 'number_of_duplicates': 3}]}
 ```
                                    
-- check_duplicates(dataframe, ['col_1', 'col_2'])
```
           {'count': 2, 'samples': [{'col_1': 'A', 'col_2': 'a', 'number_of_duplicates': 2}]}
           
```
           
-- check_duplicates(dataframe, ['col_1', 'col_2', 'col_3'])
```
           {'count': 0, 'samples': []}
           
```           
           
 **function output details:**
 **count:** number of cases where duplicates occur.
 **samples:** dataframe with group count of duplicate rows for the columns 
 
 ## Unit testing:
  tested for the correctness of the output with the expected values. All the test cases passed!


