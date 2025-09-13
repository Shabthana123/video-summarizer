from transformers import pipeline

def summarize_text(
    text: str,
    model_name: str = "facebook/bart-large-cnn",
    max_length: int = 40,
    min_length: int = 10
) -> str:
    """Summarizes the given text using a pre-trained transformer model."""

    # Tokenize text length (approx. word count)
    input_length = len(text.split())

    # Dynamically adjust max_length so it's always < input_length
    adjusted_max = min(max_length, max(5, input_length - 1))
    adjusted_min = min(min_length, max(5, adjusted_max // 2))

    summarizer = pipeline("summarization", model=model_name)

    summary = summarizer(
        text,
        max_length=adjusted_max,
        min_length=adjusted_min,
        do_sample=False  # Ensures deterministic output
    )
    
    return summary[0]["summary_text"]
