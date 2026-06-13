# 📊 AI SQL Agent

AI SQL Agent is an AI-powered analytics platform that converts natural language questions into SQL queries, executes them on structured datasets, and generates meaningful insights through an interactive dashboard.

---

## 🚀 Features

- 📂 CSV File Upload
- 🤖 Natural Language to SQL Conversion
- 🗄️ SQLite Database Integration
- 📊 Automatic Data Visualization
- 📈 KPI Metrics Dashboard
- 💡 AI-Powered Business Insights
- 📥 Excel Report Download
- 🕒 Query History Tracking
- ⚡ Interactive Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Matplotlib
- Google Gemini API
- OpenPyXL

---

## 📂 Project Structure

```text
AI-SQL-Agent/

├── app.py
├── db_manager.py
├── sql_generator.py
├── insight_generator.py
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/NandKumarTirth/AI-SQL-Agent.git
cd AI-SQL-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install streamlit pandas matplotlib google-generativeai openpyxl
```

---

## 🔑 Configure Gemini API

Open:

```python
sql_generator.py
```

and

```python
insight_generator.py
```

Replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your Gemini API Key.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📊 Workflow

```text
Upload CSV
      ↓
Create SQLite Database
      ↓
Ask Question in Natural Language
      ↓
Generate SQL using Gemini
      ↓
Execute Query
      ↓
Display Results
      ↓
Generate Charts
      ↓
AI Business Insights
      ↓
Download Excel Report
```

---

## 📸 Example Questions

```text
Show all employees

Show top 5 salaries

Average salary by department

Count employees by department

Who has the highest salary?
```

---

## 🎯 Use Cases

- Business Analytics
- Sales Analysis
- HR Analytics
- Financial Reporting
- Dataset Exploration
- Data-Driven Decision Making

---

## 📈 Key Capabilities

- Converts plain English into SQL queries
- Executes queries automatically
- Generates visual insights
- Produces AI-generated business recommendations
- Exports results to Excel
- Tracks previous analysis history

---

## 👨‍💻 Author

**Nand Kumar Tirth**

GitHub:
https://github.com/NandKumarTirth

---

## ⭐ Future Enhancements

- Conversational Data Chat
- Multi-CSV Support
- Dashboard Builder
- PDF Report Generation
- Query Explanation Engine
- Advanced Data Analytics Agent
