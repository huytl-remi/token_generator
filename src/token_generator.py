import json
import re
from .openai_client import generate_text

def generate_tokens(text_input, image_file=None):
    if image_file:
        prompt = f"""Based on this image and the text '{text_input}', generate three unique token concepts. Provide your response with a JSON object like below:
            {{
              "image_analysis": {{
                "key_elements": ["element1", "element2", "element3"],
                "colors": ["color1", "color2", "color3"],
                "themes": ["theme1", "theme2", "theme3"]
              }},
              "tokens": [
                {{
                  "name": "Token Name",
                  "ticker": "TKR",
                  "description": "Brief description of the token (max 20 words)",
                  "visual_elements": ["element1", "element2", "element3"]
                }},
                {{
                  "name": "Token Name",
                  "ticker": "TKR",
                  "description": "Brief description of the token (max 20 words)",
                  "visual_elements": ["element1", "element2", "element3"]
                }},
                {{
                  "name": "Token Name",
                  "ticker": "TKR",
                  "description": "Brief description of the token (max 20 words)",
                  "visual_elements": ["element1", "element2", "element3"]
                }}
              ]
            }}
            """
    else:
        prompt = f"""Based on this text '{text_input}', generate three unique token concepts. Provide your response with a JSON object like below:
            {{
                "tokens": [
                {{
                    "name": "Token Name",
                    "ticker": "TKR",
                    "description": "Brief description of the token (max 20 words)",
                    "visual_elements": ["element1", "element2", "element3"]
                }},
                {{
                    "name": "Token Name",
                    "ticker": "TKR",
                    "description": "Brief description of the token (max 20 words)",
                    "visual_elements": ["element1", "element2", "element3"]
                }},
                {{
                    "name": "Token Name",
                    "ticker": "TKR",
                    "description": "Brief description of the token (max 20 words)",
                    "visual_elements": ["element1", "element2", "element3"]
                }}
                ]
            }}
            Ensure each concept is distinct and aligns with the input.
            """

    system_message = """
    You are an AI assistant creating unique token concepts. Each concept should include a token name,
    ticker symbol (3-5 characters), a brief description (max 20 words), and key visual elements.
    Provide your response in a JSON format with an array of three token objects.
    """

    response = generate_text(prompt, system_message)
    if response:
        parsed_response = parse_json_response(response)
        if parsed_response:
            if 'tokens' in parsed_response:
                return parsed_response['tokens']
            elif isinstance(parsed_response, list):
                return parsed_response
        print("Error: Unexpected response format")
    return []

def extract_json_from_markdown(text):
    # Find JSON-like structures in the text
    json_match = re.search(r'```json\s*([\s\S]*?)\s*```', text) or re.search(r'{[\s\S]*}', text)
    if json_match:
        return json_match.group(1) if json_match.group(1) else json_match.group(0)
    return None

def parse_json_response(response):
    try:
        # First, try to extract JSON from markdown
        json_str = extract_json_from_markdown(response)

        # Try to parse the extracted string as JSON
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None
