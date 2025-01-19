import pandas as pd

def load_data(0):
    """
     Loads the Iris dataset from an online source.
     Returns:
     pandas.DataFrame: The loaded dataset containing
    features and labels.
     """
    url = "https://raw.githubusercontent.com/mwaskom/seaborndata/master/iris.csv"
    data = pd.read_csv(url)
    return data