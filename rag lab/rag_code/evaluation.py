# Placeholder for metrics – real ones require labeled data

def evaluate_retrieval(relevant_docs, retrieved_docs):
    relevant_set = set(relevant_docs)
    retrieved_set = set(retrieved_docs)
    tp = len(relevant_set.intersection(retrieved_set))
    precision = tp / len(retrieved_set) if retrieved_set else 0
    recall = tp / len(relevant_set) if relevant_set else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0
    return precision, recall, f1
