def build_prompt(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"""Use the following context to answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:"""
    return prompt
