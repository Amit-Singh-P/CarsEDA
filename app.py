import streamlit as st
from PIL import Image
import time
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io


# ---------------------
# Set up the page
# ---------------------
st.set_page_config(
    page_title="Cars EDA Project",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------
# Sidebar Navigation
# ---------------------
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "Data Overview", "Insights", "Visualizations", "About"],
        icons=["house", "bar-chart", "lightbulb", "pie-chart", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "10px", "background-color": "#4b4b4b"},
            "icon": {"color": "#399086", "font-size": "20px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "left",
                "margin": "5px",
            },
            "nav-link-selected": {"background-color": "#95eadd"},
        },
    )


# ---------------------
# Home Page
# ---------------------
if selected == "Home":
    st.title("🚗 Cars Exploratory Data Analysis (EDA) Project")
    st.subheader("Understand the Used Car Market with Data-Driven Insights")

    with st.spinner("Loading image..."):
        time.sleep(1)
        car_image = Image.open("image.jpg")
        st.image(car_image, caption="Used Cars Market", use_container_width=True)

    with st.expander("📌 Problem Statement"):
        st.markdown("""
        The used car market is expanding rapidly, but buyers often struggle to make informed decisions due to lack of clear and comprehensive data insights.

        This project provides an in-depth **Exploratory Data Analysis (EDA)** on used car listings to reveal trends and patterns in:
        - 📍 Location
        - 🏷️ Manufacturing year
        - ⛽ Fuel type
        - 🚗 Mileage
        - 💰 Price

        📊 These insights help both **buyers** and **sellers** make confident, data-driven decisions.
        """)

    st.markdown("---")
    st.markdown("⬅️ Use the sidebar to explore more about the data and visual insights.")

# ---------------------
# Data Overview
# ---------------------

elif selected == "Data Overview":
    st.header("📈 Dataset Overview")


    raw_df = pd.read_csv("Cars (1).csv")
    clean_df = pd.read_csv("Cars_cleaned.csv")

    clean_df.drop(columns='Unnamed: 0', inplace=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Cars", f"{clean_df["Name"].count():,}")
    col2.metric("Average Price (In Lakhs)", numerize(clean_df["Price"].mean()))
    col3.metric("Unique Brands", len(clean_df["Brand"].unique()))



    st.header("🔍 Raw Dataset")
    st.dataframe(raw_df)

    st.markdown("---")

    st.header("✅ Cleaned Dataset")
    st.dataframe(clean_df)

    st.markdown("---")

    st.write("### Key Differences")
    st.markdown("""
    - **Missing Values** handled
    - **Columns cleaned** (data types, units removed)
    - **Consistent formatting** (e.g., bhp, kmpl as numeric)
    - **Separated brand/model** in clean data
    """)

    st.info("🔍 You can later add a data preview and summary stats here.")



# ---------------------
# Insights
# ---------------------
elif selected == "Insights":
    st.header("💡 Key Insights")
    st.success("Data-driven conclusions and recommendations go here.")


    df = pd.read_csv("Cars_cleaned.csv")

    df.drop(columns='Unnamed: 0', inplace=True)

    # Section: Basic Info
    st.markdown("## 🔍 1. Dataset Overview")
    mem_usage = df.memory_usage(deep=True).sum() / (1024 ** 2)

    info_df = pd.DataFrame({
        "📌 Column": df.columns,
        "✅ Non-Null Count": df.notnull().sum().values,
        "🔠 Data Type": df.dtypes.astype(str).values,
        "🔢 Unique Values": [df[col].nunique() for col in df.columns],
        "📍 Example Value": [df[col].dropna().iloc[0] if not df[col].dropna().empty else "N/A" for col in df.columns]
    })

    st.dataframe(info_df, use_container_width=True)

    st.markdown(f"""
    <div style="padding: 10px; background-color: #464f4e; border-left: 5px solid #2ecc71; border-radius: 5px">
    <b>🧾 Total Entries:</b> {len(df)}  
    <br><b>📊 Total Columns:</b> {df.shape[1]}  
    <br><b>🧠 Memory Usage:</b> {mem_usage:.2f} MB
    </div>
    """, unsafe_allow_html=True)

    st.subheader("2. Summary Statistics")
    st.write(df.describe())

    st.subheader("3. Null Values")
    st.write(df.isnull().sum())

    st.subheader("4. Unique Value Counts")
    for col in ['Fuel_Type', 'Transmission', 'Owner_Type', 'Colour', 'Brand']:
        st.write(f"**{col}**: {df[col].nunique()} unique values")
        st.write(df[col].value_counts())

    st.subheader("5. Top 5 Most Driven Cars")
    st.write(df.sort_values(by='Kilometers_Driven', ascending=False)[['Name', 'Kilometers_Driven']].head())

    st.subheader("6. Average Price by Brand")
    st.write(df.groupby("Brand")["Price"].mean().sort_values(ascending=False))



# ---------------------
# Visualizations
# ---------------------
elif selected == "Visualizations":
    st.header("📊 Visual Explorations")
    st.warning("Charts and interactive visualizations will appear here once the dataset is integrated.")


    st.title("Visualization and Analysis")

    # Load data (no caching)
    df = pd.read_csv("Cars_cleaned.csv")

    df.drop(columns='Unnamed: 0', inplace=True)


    analysis_type = st.radio("Choose Analysis Type", ("Univariate", "Bivariate", "Multivariate"))

    if analysis_type == "Univariate":
        st.header("Univariate Analysis")
        column = st.selectbox("Select column for univariate analysis", df.columns)

        if pd.api.types.is_numeric_dtype(df[column]):
            fig, ax = plt.subplots()
            sns.histplot(df[column], kde=True, ax=ax)
            ax.set_title(f'Distribution of {column}')
            st.pyplot(fig)
            
            fig2, ax2 = plt.subplots()
            sns.boxplot(x=df[column], ax=ax2)
            ax2.set_title(f'Boxplot of {column}')
            st.pyplot(fig2)
        else:
            fig, ax = plt.subplots()
            df[column].value_counts().plot(kind='bar', ax=ax)
            ax.set_title(f'Count plot of {column}')
            st.pyplot(fig)

    elif analysis_type == "Bivariate":
        st.header("Bivariate Analysis")
        col1 = st.selectbox("Select first column (usually numeric)", df.select_dtypes(include='number').columns)
        col2 = st.selectbox("Select second column", df.columns)

        if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
            ax.set_title(f'Scatter plot between {col1} and {col2}')
            st.pyplot(fig)
        elif pd.api.types.is_numeric_dtype(df[col1]) and not pd.api.types.is_numeric_dtype(df[col2]):
            fig, ax = plt.subplots()
            sns.boxplot(x=df[col2], y=df[col1], ax=ax)
            ax.set_title(f'Boxplot of {col1} grouped by {col2}')
            st.pyplot(fig)
        else:
            st.write("Bivariate plot not available for selected combination.")

    elif analysis_type == "Multivariate":
        st.header("Multivariate Analysis")

        # Heatmap for numeric columns correlation
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        st.subheader("Correlation Heatmap")
        selected_heatmap_cols = st.multiselect("Select numeric columns for heatmap", numeric_cols, default=numeric_cols[:5])
        if len(selected_heatmap_cols) >= 2:
            fig, ax = plt.subplots()
            sns.heatmap(df[selected_heatmap_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            ax.set_title('Correlation Heatmap')
            st.pyplot(fig)
        else:
            st.write("Select at least two numeric columns for heatmap.")

        st.subheader("Scatter / Bar plot with Hue")
        all_cols = df.columns.tolist()
        x_col = st.selectbox("Select X-axis column", all_cols, key='xcol')
        y_col = st.selectbox("Select Y-axis column", all_cols, key='ycol')
        hue_col = st.selectbox("Select Hue (legend) column", [None] + all_cols, key='huecol')

        plot_type = st.radio("Select plot type", ("Scatter Plot", "Bar Plot"))

        if x_col and y_col:
            fig, ax = plt.subplots()
            try:
                if plot_type == "Scatter Plot":
                    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col if hue_col != 'None' else None, ax=ax)
                else:  # Bar Plot
                    sns.barplot(data=df, x=x_col, y=y_col, hue=hue_col if hue_col != 'None' else None, ax=ax)
                ax.set_title(f'{plot_type} of {y_col} vs {x_col} grouped by {hue_col}')
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error plotting: {e}")


# ---------------------
# About
# ---------------------
elif selected == "About":
    st.header("ℹ️ About This App")
    st.markdown("""
    - **Project**: Used Cars EDA
    - **Author**: Amit Singh
    - **Tools Used**: Python, Streamlit, Pandas, Matplotlib/Seaborn
    - **GitHub**: https://github.com/Amit-Singh-P/CarsEDA/
    """)

    st.balloons()

