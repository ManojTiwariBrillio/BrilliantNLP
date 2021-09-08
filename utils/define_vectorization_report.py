import pandas as pd

def define_report():
    report = pd.DataFrame(columns=["Avg Top-1", "Avg Top-2", "Avg Top-3", "Avg Top-4", "Avg Top-5", "Emb Len", "Sklearn", "Dot Prod", "TS-SS"])
    return report