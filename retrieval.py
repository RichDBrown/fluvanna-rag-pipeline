import numpy as np

def get_question():
    """Prompts the user to enter a question.
    
    Returns:
        The question entered by the user.
    """
    question = input("Enter your question: ")
    return question

def get_top_chunks(query, model, embeddings, chunks):
    """Retrieves the top 3 most relevant text chunks based on the query.
    
    Args:
        query: The user's question.
        model: The sentence transformer model.
        embeddings: The list of embeddings corresponding to the text chunks.
        chunks: The list of text chunks.

    Returns:
        A list of the top 3 most relevant text chunks.
    """
    query_embedding = model.encode([query])[0]

    document_norms = np.linalg.norm(embeddings, axis=1)
    query_norm = np.linalg.norm(query_embedding)

    similarities = (embeddings @ query_embedding) / (document_norms * query_norm)

    results = sorted(zip(chunks, similarities), key=lambda x: x[1], reverse=True)

    return [chunk for chunk, score in results[:3]]