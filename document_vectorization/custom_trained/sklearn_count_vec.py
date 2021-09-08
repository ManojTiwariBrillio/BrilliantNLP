from sklearn.feature_extraction.text import CountVectorizer

def count_vec(preprocessed_sentences):
    # BoW
    count_vect = CountVectorizer()  # in scikit-learn
    count_vect.fit(preprocessed_sentences)

    print("some feature names ", count_vect.get_feature_names()[:10])
    print('=' * 50)

    final_counts = count_vect.transform(preprocessed_sentences)

    print("the type of count vectorizer ", type(final_counts))
    print("the shape of out text BOW vectorizer ", final_counts.get_shape())
    print("the number of unique words ", final_counts.get_shape()[1])
    return count_vect, final_counts