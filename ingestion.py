from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text_from_pdf():
    """Extracts text from PDF files in the 'documents' directory.
    
    Returns:
        The text extracted from the PDF files. 
    """
    text = ""

    documents_path = Path("documents")

    for pdf_path in documents_path.glob("*.pdf"):
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

def chunk_text(text):
    """Splits the text into chunks using RecursiveCharacterTextSplitter.
    
    Args:
        text: The text to be split into chunks.
        
    Returns:
        A list of text chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = text_splitter.split_text(text)

    return chunks

def embed_text(chunks, model):
    """Embeds the text chunks using the specified sentence transformer model.
    
    Args:
        chunks: A list of text chunks to be embedded.
        model: The sentence transformer model to use for generating embeddings.
        
    Returns:
        A list of embeddings corresponding to the text chunks.
    """
    embeddings = model.encode(chunks)

    return embeddings