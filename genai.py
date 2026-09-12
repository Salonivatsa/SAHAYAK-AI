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

Your response should include:
1. What the model detected
2. A short explanation
3. What the user should do now
4. Important safety precautions
5. Ask the user for feedback about whether the prediction is correct

Do not claim that the prediction is 100% certain.
If confidence is low, clearly tell the user that the prediction may be incorrect.

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