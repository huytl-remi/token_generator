from .openai_client import generate_image_url

def generate_image(token):
    prompt = f"""
    Design a simple, memorable logo for a token named '{token['name']}'.
    The logo should represent: {token['description']}

    Incorporate these key visual elements: {', '.join(token['visual_elements'])}

    The logo should be:
    - Minimalist and clean
    - Suitable for various sizes (from app icons to large displays)
    - Using a limited color palette (2-3 colors maximum)
    - No text or lettering
    - Centered in the image with ample white space around it
    - Easily recognizable and distinct

    The image should have a square aspect ratio with a plain, subtle background.
    Do not include the token name or any text in the logo itself.
    """
    image_url = generate_image_url(prompt)
    return image_url
