def get_unique_values(df, col):
    """
    Return the value of a given transaction in a block
        for the dataframe `df`.
    """
    return len(df[col].unique())