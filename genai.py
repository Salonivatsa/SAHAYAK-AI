import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_ai_response(prediction, confidence):

    prompt = f"""
You are Sahayak AI, a disaster assistance AI.

A trained image classification model has given this prediction:

Prediction: {prediction}
Confidence: {confidence:.2f}%

Based on this prediction, help the user in simple language.



Keep the response short, clear and practical.
"""  

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text

if __name__ == "__main__":
    prediction = "Accident"
    confidence = 92.5

    response = get_ai_response(prediction, confidence)

    print("\nSahayak AI:")
    print(response)