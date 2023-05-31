# import libraries
import pandas as pd
import logging
from typing import Union, Any

# Configure logging
logging.basicConfig(filename='check_duplicates_log.log', level=logging.DEBUG, filemode='w')


def check_duplicates(dataframe: pd.DataFrame, columns: list) -> Union[ValueError, dict[str, Any]]:
    """
    Function to check for the duplicates in the provided dataframe and the column(s)

      Args:
          dataframe (pandas.DataFrame): DataFrame to check the duplicate values
          columns (list): list of columns to check for the duplicates
      Return:
          results(dict): dictionary with the below values
                         - count: number of duplicate occurrences.
                         - samples: dataframe with group count of duplicate rows for the columns
      Raises:
            Value error: if the dataframe isn't of pandas dataframe type or an empty dataframe
            returns: if the input columns doesn't match the existing columns in the dataframe
      """

    # check if dataframe is of dataframe type and empty or not
    if not isinstance(dataframe, pd.DataFrame):
        logging.error("Input must be a DataFrame")
        return ValueError("Error:Input must be a DataFrame")
    if dataframe.empty:
        logging.error("Input DataFrame is empty")
        return ValueError("Error:Input DataFrame is empty")
    # check if provided column(s) aren't empty
    if columns:
        # check if provided column(s) exist in the dataframe
        columns_undefined = []
        for col in columns:
            if col not in dataframe.columns:
                columns_undefined.append(col)
        if len(columns_undefined) == 0:
            # checking the count of duplicates
            count = dataframe.duplicated(subset=columns, keep="first")
            # checking for the samples with group by count values
            duplicate_values = dataframe[dataframe.duplicated(columns)].groupby(columns).size().reset_index(
                name='number_of_duplicates')
            result = {
                'count': count.sum(),
                'samples': duplicate_values.to_dict('records')
            }
            return result
        else:
            logging.debug(
                "The following column(s) are missing in the dataframe:{}, please check the provided input.".format(
                    columns_undefined))
            return ValueError(
                "Error:The following column(s) are missing in the dataframe:{}, please check the provided input.".
                format(columns_undefined))
    else:
        logging.debug("The provided column value is null.")
        return ValueError("Error:The provided column value is null.")
