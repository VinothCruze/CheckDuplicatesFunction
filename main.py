# import libraries
import pandas as pd
from check_duplicate import check_duplicates

# dataframe definition
df_1 = pd.DataFrame(
                data=[
                ['A','a', 'x', 1],
                ['A','b', 'x', 1],
                ['A','c', 'x', 1],
                ['B','a', 'x', 1],
                ['B','b', 'x', 1],
                ['B','c', 'x', 1],
                ['A','a', 'y', 1],
                ],
                columns=['col_1', 'col_2', 'col_3', 'col_4']
                )

result_1 = check_duplicates(df1, ['col_1'])
result_2 = check_duplicates(df1, ['col_1', 'col_2'])
result_3 = check_duplicates(df1, ['col_1', 'col_2', 'col_3'])
print(result_1)
print(result_2)
print(result_3)
