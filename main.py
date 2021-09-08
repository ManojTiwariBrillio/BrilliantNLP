import text_preprocessing
from document_vectorization.custom_trained import sklearn_count_vec
from utils.define_vectorization_report import define_report
from utils.report_generation import perfromance_report
from utils.fetch_data import most_similar

import pandas as pd
import numpy as np

FILE_NAME=r"C:\Users\manoj.tiwari\OneDrive - Brillio\Documents\Convergint\ConvergintNLP_InitialDraft\ConvergintNLP_InitialDraft\raw data (3).xlsx"
raw_df = pd.read_excel(FILE_NAME)

df = raw_df[raw_df['equipment'] == "Interior PTZ Camera"].reset_index()

preprocessed_problems = text_preprocessing.get_clean_data(df['problem'].values)

count_vectorizer, count_vectorized_problems = sklearn_count_vec.count_vec(preprocessed_problems)
# print(type(count_vectorizer))
# print(count_vectorized_problems[:2])

report = define_report()

report_cv = perfromance_report(count_vectorized_problems)
report = report.append(report_cv)

most_similar(count_vectorized_problems[0], count_vectorized_problems, dataframe=df)




