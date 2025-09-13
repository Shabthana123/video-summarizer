""" 
create 2 functions
1. chuncked text 
2. check summerization

"""

def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    """
    Splits the input text into chunks of specified size with a given overlap.

    Args:
        text (str): The input text to be chunked.
        chunk_size (int): The maximum size of each chunk. Default is 2000 characters.
        overlap (int): The number of overlapping characters between consecutive chunks. Default is 200 characters.

    Returns:
        list: A list of text chunks.
    """
    
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        
        #  Move the start index forward by chunk_size minus overlap
        start += chunk_size - overlap

        if start < 0:
            start = 0
            
    return chunks

def chunked_summarize(text: str, summerize_func, max_chunk_size: int = 2000, overlap: int = 200) -> str:
    """
    Summarizes the input text by chunking it and applying a summarization function to each chunk.

    Args:
        text (str): The input text to be summarized.
        summerize_func (callable): A function that takes a string and returns its summary.
        max_chunk_size (int): The maximum size of each chunk. Default is 2000 characters.

    Returns:
        str: The combined summary of all chunks.
    """
    
    text_chunks = chunk_text(text, chunk_size=max_chunk_size, overlap= overlap)
    partial_summaries = [summerize_func(chunk) for chunk in text_chunks]
    
    combined_summary = " ".join(partial_summaries)
    
    final_summary = summerize_func(combined_summary)
    
    return final_summary