def basic_search(vector_db, query, k=3):
    results = vector_db.similarity_search(query, k=k)
    return results

def mmr_search(vector_db, query, k=5, lambda_mult=0.5):
    results = vector_db.max_marginal_relevance_search(query, k=k, lambda_mult=lambda_mult)
    return results
