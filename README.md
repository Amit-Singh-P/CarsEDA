# 🚗 Used Cars EDA Dashboard

An interactive **Streamlit** web app that performs **Exploratory Data Analysis (EDA)** on a used cars dataset to uncover trends in price, mileage, brand, fuel type, transmission, and more. This project helps buyers, sellers, and analysts make data-driven decisions in the second-hand automobile market.

---

## 📌 Problem Statement

The used car industry is booming, yet potential buyers and sellers often lack access to clear and comprehensive insights.  
This project solves that by:

- Cleaning and processing real-world used car data.
- Creating an interactive web dashboard for exploring trends.
- Empowering users to analyze cars by brand, price, mileage, and other features.

---

## 🚀 Features

✅ Sidebar navigation with **5 main sections**  
✅ Raw and cleaned data comparison  
✅ Metric cards for **quick insights**  
✅ Detailed insights with memory usage, null values, and unique counts  
✅ **Interactive Visualizations** (Univariate, Bivariate, Multivariate)  
✅ Heatmaps, scatter plots, box plots, bar plots with `hue` support  
✅ Dynamic layout with icons and styled UI

---

## 🖥️ App Sections

| Section         | Description |
|-----------------|-------------|
| **Home**        | Project introduction, problem statement, banner image |
| **Data Overview** | View raw vs cleaned data, key metrics, and cleaning summary |
| **Insights**    | Dataset info, null values, top-driven cars, average price by brand |
| **Visualizations** | Univariate, bivariate, and multivariate analysis with plots |
| **About**       | Author info, project tech stack, GitHub link |

---

## 📊 Tech Stack

- **Python**
- **Streamlit** – for UI and interactivity
- **Pandas** – for data processing
- **Seaborn / Matplotlib** – for charts
- **Numerize** – to display formatted numeric values
- **Pillow (PIL)** – to display images

---

## 📁 Folder Structure

CarsEDA/
│
├── app.py # Main Streamlit app
├── Cars (1).csv # Raw dataset
├── Cars_cleaned.csv # Cleaned dataset
├── image.jpg # Banner image
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---
## Home Page
<img width="1451" alt="Screenshot 2025-06-28 at 10 49 36 PM" src="https://github.com/user-attachments/assets/5ce19e3c-f324-4df7-84b5-9fec0c1652e6" />

---
## 🔧 Setup Instructions

1. **Clone the repository**
git clone https://github.com/Amit-Singh-P/CarsEDA.git
cd CarsEDA

2. **Create a virtual environment (recommended)**
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the app**
streamlit run app.py


📄 License
This project is licensed under the MIT License – feel free to use and adapt!

⭐️ Show Your Support
If you found this project useful:

Give it a ⭐️ on GitHub

Share your feedback

Fork and try your own analysis!




