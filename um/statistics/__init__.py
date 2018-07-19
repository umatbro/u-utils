import pandas as pd


def filter_outliers(data: pd.Series, std: int=3) -> pd.Series:
    """
    Remove outliers from ``Series``.

    :param data: data to be filtered
    :param std: number of standard deviations to be filtered. Default is 3
    :return: ``Series`` filtered out of outliers
    """
    return data[(data - data.mean()).abs() <= (std * data.std())]
