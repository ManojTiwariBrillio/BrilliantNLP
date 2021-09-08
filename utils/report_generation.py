# Compute Cosine Similarity
from .dot_product import dot_product_cos_sim
from .define_vectorization_report import define_report

from .vector_similarity_vectorized import TS_SS

import time
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


def perfromance_report(vectorzied_sentences, top=5):
    TOP = top
    sorted_tops = []

    start = time.time()
    cos_sim = cosine_similarity(vectorzied_sentences, vectorzied_sentences)
    end = time.time()

    start_np = time.time()
    cos_sim_np = dot_product_cos_sim(vectorzied_sentences.toarray(), vectorzied_sentences.T.toarray())
    end_np = time.time()

    similarity = TS_SS()
    start_tsss = time.time()
    cos_sim_tsss = similarity(vectorzied_sentences.toarray(), vectorzied_sentences.toarray())
    end_tsss = time.time()

    for i in range(cos_sim.shape[0]):
        sorted_top = np.sort(cos_sim[i])[::-1][1:6]
        if len(sorted_tops) == 0:
            sorted_tops = sorted_top
        else:
            sorted_tops = np.vstack((sorted_tops, sorted_top))

    top_avg = np.mean(sorted_tops, axis=0)
    top_max = np.max(sorted_tops, axis=0)
    top_min = np.min(sorted_tops, axis=0)

    time_delta = end - start
    time_delta_np = end_np - start_np
    time_delta_tsss = end_tsss - start_tsss

    print("Seconds:", time_delta)
    print("Minutes:", time_delta / 60)

    cos_sim_report_df = pd.DataFrame(top_avg, columns=['Count_Vec'])
    cos_sim_report_df = cos_sim_report_df.T
    cos_sim_report_df.rename(columns={0: "Avg Top-1", 1: "Avg Top-2", 2: "Avg Top-3", 3: "Avg Top-4", 4: "Avg Top-5"},
                     inplace=True)
    cos_sim_report_df['Emb Len'] = vectorzied_sentences.get_shape()[1]
    cos_sim_report_df['Sklearn'] = time_delta
    cos_sim_report_df['Dot Prod'] = time_delta_np
    cos_sim_report_df['Dot Prod'] = time_delta_tsss
    return cos_sim_report_df