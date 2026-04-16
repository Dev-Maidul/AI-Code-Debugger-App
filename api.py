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

Your job is  just to explain errors, but to FIX them 
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
## 🚨 Error Explanation
- What is the error?
- Why it happens?

🎨 FORMATTING RULES:
- Use clean Markdown.
- Use emojis (🚨 💡 ✅).
- Highlight important terms using **bold**.
- Keep response structured and professional.

---

⚠️ IMPORTANT RULES:
- Do NOT stop at explanation only.
- If the image is unclear, say: "Image is unclear, please upload a clearer screenshot."

---

Now analyze the image and provide the full debugging result 
"""
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text