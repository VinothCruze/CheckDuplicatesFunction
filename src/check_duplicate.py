def check_duplicates(dataframe: pd.DataFrame, columns: list)-> dict:
  

  """
  Function to check for the duplicates in the provided dataframe and the column(s)

    Args:
        dataframe (pandas.DataFrame): DataFrame to check the duplicate values
        columns (list): list of columns to check for the duplicates
    Return:
        results(dict): dictionary with the below values
                       - count: number of duplicate occurences.
                       - samples: dataframe with group count of duplicate rows for the columns
    Raises: 
          Value error: if the dataframe isnt of pandas dataframe type or an empty dataframe
          returns: if the input columns doesnt match the existing columns in the dataframe
    """

  # check if dataframe is of dataframe type and empty or not
  if not isinstance(dataframe, pd.DataFrame):
    raise ValueError("Input must be a DataFrame")
  if dataframe.empty:
    raise ValueError("Input DataFrame is empty")
  # check if provided column(s) arent empty
  if columns:
    # check if provided column(s) exist in the dataframe
    columns_undefined = []
    for col in columns:
        if col not in dataframe.columns:
            columns_undefined.append(col)
    if len(columns_undefined) == 0:
      # checking the count of duplicates
      count = dataframe.duplicated(subset=columns, keep="first")
      # checking for the samples with groupby count values
      duplicate_values = dataframe[dataframe.duplicated(columns)].groupby(columns).size().reset_index(name='number_of_duplicates')
      result = {
          'count': count.sum(),
          'samples': duplicate_values.to_dict('records')
      } 
      return result 
    else:
      raise ValueError("The following column(s) are missing in the dataframe:{}, please check the provided input.".format(columns_undefined))
  else:
    raise ValueError("The provided column value is null.")

  
