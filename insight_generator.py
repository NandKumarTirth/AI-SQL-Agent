import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_insights(df):

    prompt = f"""
You are a professional data analyst.

Analyze the dataset below and provide:

1. Key Findings
2. Trends
3. Important Insights
4. Business Recommendations

Dataset:

{df.head(20).to_string()}
"""

    response = model.generate_content(
        prompt
    )

    return response.text