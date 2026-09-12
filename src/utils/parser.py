# src/utils/parser.py

def extract_clean_text(output) -> str:
    """Extracts plain text from Gemini/LangChain structured response blocks."""
    if isinstance(output, str):
        return output

    if isinstance(output, list):
        text_parts = []
        for item in output:
            if isinstance(item, dict) and "text" in item:
                text_parts.append(item["text"])
            elif isinstance(item, str):
                text_parts.append(item)
        return "".join(text_parts).strip()

    return str(output)