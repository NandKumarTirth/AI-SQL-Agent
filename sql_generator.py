import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_sql(
    columns,
    question
):

    prompt = f"""
You are an SQL expert.

Database Table Name:
data

Available Columns:
{columns}

Convert the user's question into a valid SQLite query.

Return ONLY SQL.

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.replace(
        "```sql",
        ""
    ).replace(
        "```",
        ""
    ).strip()