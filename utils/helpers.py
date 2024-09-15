import re
import json

def validate_ticker(ticker):
    return bool(re.match(r'^[A-Z]{3,5}$', ticker))

def sanitize_input(input_text):
    return re.sub(r'[^\w\s-]', '', input_text).strip()

def extract_json_from_markdown(text):
    json_match = re.search(r'```json\s*([\s\S]*?)\s*```', text)
    if json_match:
        return json_match.group(1).strip()

    # If no JSON block is found, try to find a JSON-like structure
    json_match = re.search(r'({[\s\S]*})', text)
    if json_match:
        return json_match.group(1).strip()

    return text  # Return the original text if no JSON-like structure is found
