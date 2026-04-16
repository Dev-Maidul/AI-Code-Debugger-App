from google import genai
from dotenv import load_dotenv
import os
import io

load_dotenv()
my_api_key=os.getenv("GEMNI_API_KEY")

# client initialization
client=genai.Client(api_key=my_api_key)

#! Error explanation function
def error_explanator(images):
    prompt = f"""
You are a senior software engineer and AI Code Debugger.

Your job is  just to explain errors, not fix them and not provide code.
---

🔍 TASK:
Analyze the uploaded screenshot which contains code and/or an error message.

---

🎯 OBJECTIVES (MANDATORY):
1. Identify the programming language.
2. Detect the exact error or bug.
3. Clearly explain the issue (simple and beginner-friendly).
---

📌 RESPONSE FORMAT (STRICT):

- What is the error?
- Why it happens?

🎨 FORMATTING RULES:
- Use clean Markdown.
- Use emojis (🚨 💡 ✅).
- Highlight important terms using **bold**.
- Keep response structured and professional.

---

⚠️ IMPORTANT RULES:
- If the image is unclear, say: "Image is unclear, please upload a clearer screenshot."

---

Now analyze the image and provide the full debugging result 
"""
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text

#! Hints/Solution function
def hints_solutions(images,selected_option):
    prompt=f"Analyse the images and just provide the {selected_option}.Make sure to add necessary markdown"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text