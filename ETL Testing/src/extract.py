import pandas as pd

def read_customers(path):
    return pd.read_csv(path)

def read_orders(path):
    return pd.read_csv(path)
