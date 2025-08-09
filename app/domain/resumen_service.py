from app.ports.resumidor_port import ResumidorPort


def servicio_resumen(input_text: str, adapter: ResumidorPort) -> str:
    """
    Service function to summarize text using the provided adapter.
    args:
        input_text (str): The text to be summarized.
        adapter (ResumidorPort): The adapter to use for summarization.
    returns:
        str: The summarized text.
    """
    if input_text is None or input_text.strip() == "":
        raise ValueError("Input text cannot be empty or None")
    if len(input_text) > 100000:
        raise ValueError("Input text exceeds maximum length of 100,000 characters")
    try:
        resumen = adapter.resumir(input_text)
        return resumen
    except Exception as e:
        print(f"Error during summarization: {str(e)}")
        raise RuntimeError(f"Error during summarization: {str(e)}")
