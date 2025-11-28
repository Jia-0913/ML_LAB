

from google import genai

client = genai.Client(api_key="AIzaSyAKk42jAMR41sMycxnRzaC5zqfQQphlrtA")

response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)