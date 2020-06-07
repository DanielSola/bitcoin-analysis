def get_unique_values(df, col):
    """
    Return the number of unique values in the column `col`
        for the dataframe `df`.
    """
    return len(df[col].unique())