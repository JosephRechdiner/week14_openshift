import numpy as np
import pandas as pd
from pandas import DataFrame

class DataAnalizer:
    @staticmethod
    def claculate_risk_level(df: DataFrame):
        df["risk_level"] = pd.cut(df["range_km"], bins=[1, 20, 100, 300, np.inf], labels=["low", "medium", "high", "extreme"])
        return df
    
    @staticmethod
    def remove_null(df: DataFrame):
        df = df.fillna("Unknown")
        return df