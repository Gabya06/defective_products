# Defective Products Analysis with Streamlit

## Project Overview
This project demonstrates how to build a Streamlit web application for analyzing product defects using data visualization techniques in Matplotlib and Seaborn. The dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/fahmidachowdhury/manufacturing-defects/data), contains product defect reports with repair costs, defect severity levels, and inspection methods. The goal is to generate insights through *interactive visualizations* and streamline *data exploration*.


## Table of Contents
- [Introduction](#introduction)
- [Data Visualization with Matplotlib and Seaborn](#data-viz)
- [Building an Interactive Dashboard with Streamlit](#streamlit)
- [Running the Streamlit App](#run-app)
- [Conclusion](#conclusion)

<a name="introduction"></a>
### Introduction
Understanding and effectively communicating sentiment analysis results requires clear and insightful visualizations. This project showcases how to use Matplotlib and Seaborn to create meaningful charts and how to build an interactive web application using Streamlit.

<a name="data-viz"></a>
### Data Visualization with Matplotlib and Seaborn
We cover several visualization techniques, including:
- **Bar Charts**: Used to compare sentiment distributions across different categories.
- **Line Charts**: Illustrating sentiment trends over time.

Each chart includes customization techniques such as adding labels, adjusting legends, and using color palettes to enhance readability.

<a name="streamlit"></a>
### Building an Interactive Dashboard with Streamlit
The project extends visualization capabilities by integrating Streamlit to build an interactive dashboard. Users can:
- Select different datasets for visualization.
- Apply filters to refine insights.
- View dynamic updates based on user input.

<a name="run-app"></a>
### Running the Streamlit App
To run the interactive dashboard, follow these steps:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL in your web browser to explore the dashboard.

<a name="conclusion"></a>
### Conclusion
This project demonstrates how combining Matplotlib, Seaborn, and Streamlit can enhance the presentation and interpretation of analysis results. The interactive visualizations provide a powerful way to explore data and derive meaningful insights.

---
For more details, refer to the full blog post [medium.com](https://medium.com/@gabya06/creating-your-first-streamlit-app-with-matplotlib-seaborn-7e888e8a7470).
