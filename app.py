import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from db_manager import (
    create_database,
    run_query
)

from sql_generator import (
    generate_sql
)

from insight_generator import (
    generate_insights
)

st.set_page_config(
    page_title="AI SQL Agent",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI SQL Agent")

st.markdown(
    "Ask questions in natural language and let AI generate SQL queries."
)

if "query_history" not in st.session_state:
    st.session_state.query_history = []

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    columns = create_database(
        uploaded_file
    )

    st.success(
        "✅ Database Created Successfully"
    )

    st.subheader(
        "📋 Available Columns"
    )

    st.write(columns)

    question = st.text_input(
        "Ask a question about your data"
    )

    if st.button(
        "🚀 Analyze"
    ):

        if question.strip():

            with st.spinner(
                "🤖 Generating SQL..."
            ):

                sql_query = generate_sql(
                    columns,
                    question
                )

            st.subheader(
                "🧠 Generated SQL"
            )

            st.code(
                sql_query,
                language="sql"
            )

            try:

                result = run_query(
                    sql_query
                )

                st.session_state.query_history.append(
                    {
                        "question": question,
                        "sql": sql_query
                    }
                )

                st.subheader(
                    "📊 Results"
                )

                st.dataframe(
                    result,
                    use_container_width=True
                )

                # KPI Metrics

                st.subheader(
                    "📈 Dataset Metrics"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Rows",
                        len(result)
                    )

                with col2:
                    st.metric(
                        "Columns",
                        len(result.columns)
                    )

                with col3:
                    numeric_cols = result.select_dtypes(
                        include="number"
                    ).columns

                    st.metric(
                        "Numeric Columns",
                        len(numeric_cols)
                    )

                # Chart

                if len(result) > 0:

                    numeric_cols = result.select_dtypes(
                        include="number"
                    ).columns

                    if len(numeric_cols) > 0:

                        chart_column = numeric_cols[0]

                        st.subheader(
                            "📊 Visualization"
                        )

                        fig, ax = plt.subplots()

                        result[chart_column].plot(
                            kind="bar",
                            ax=ax
                        )

                        st.pyplot(fig)

                # AI Insights

                if len(result) > 0:

                    with st.spinner(
                        "🤖 Generating Insights..."
                    ):

                        insights = generate_insights(
                            result
                        )

                    st.subheader(
                        "💡 AI Business Insights"
                    )

                    st.write(
                        insights
                    )

                # Excel Download

                excel_file = "query_result.xlsx"

                result.to_excel(
                    excel_file,
                    index=False
                )

                with open(
                    excel_file,
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download Excel Report",
                        data=file,
                        file_name="query_result.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

            except Exception as e:

                st.error(
                    f"SQL Error: {e}"
                )

        else:

            st.warning(
                "Please enter a question."
            )

    if st.session_state.query_history:

        st.subheader(
            "🕒 Query History"
        )

        for item in reversed(
            st.session_state.query_history
        ):

            st.markdown(
                f"**Question:** {item['question']}"
            )

            st.code(
                item["sql"],
                language="sql"
            )

            st.divider()