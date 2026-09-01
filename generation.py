from google import genai
import os
from dotenv import load_dotenv

def generate_response(top_chunks, query):
    """Generate a response based on the top chunks and the user's query.
    
    Args:
        top_chunks: A list of the top relevant text chunks.
        query: The user's question.
    
    Returns:
        The generated text response.
    """
    load_dotenv(dotenv_path=".env.local")
    api_key = os.getenv("GEM_AI_KEY")

    client = genai.Client(api_key=api_key)

    context = "\n\n".join(top_chunks)

    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        system_instruction='''You are a helpful assistant. Answer the user's question based ONLY on the following context. If the answer cannot be found in the context, say "I don't know."''',
        input=f"""
        --- CONTEXT ---
        {context}

        --- QUESTION ---
        {query}
        """
    )

    return interaction.output_text