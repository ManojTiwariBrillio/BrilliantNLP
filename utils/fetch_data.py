from sklearn.metrics.pairwise import cosine_similarity

def most_similar(vectorized_query_sent, vectorized_sentences, dataframe, top=5):
    cos_sim = cosine_similarity(vectorized_query_sent, vectorized_sentences)

    df = dataframe
    top = top
    for sent_idx, sim_score in enumerate(cos_sim):
        sim_score = sim_score
        indices = (-sim_score).argsort()[1:top + 1]
        # print(indices, sim_score[indices])
        print("Query Sentence: ")
        print("=" * 50)
        print(df.loc[0, "problem"])
        counter = 1
        for i in indices:
            print("\n")
            print("-" * 50)
            print(f"Rank {counter} - Similarity {sim_score[i]}")
            print("=" * 50)
            print(df.loc[i, "problem"])
            counter += 1
