from generation import generate_response
from ingestion import chunk_text, embed_text, extract_text_from_pdf
from retrieval import get_question, get_top_chunks
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-base-en-v1.5")

# Injestion
text = extract_text_from_pdf()
chunks = chunk_text(text)
text_embeddings = embed_text(chunks, model)

# Retrieval
query = get_question()
top_chunks = get_top_chunks(query, model, text_embeddings, chunks)

# Generation
response = generate_response(top_chunks, query)
print('\n--- RESPONSE ---\n')
print(response)