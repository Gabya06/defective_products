"""Demo Streamlit App for Defective Products Analysis"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pandas as pd

import seaborn as sns

import streamlit as st


st.set_page_config(layout="wide")

# data pre-processing
df = pd.read_csv("defects_data.csv", parse_dates=["defect_date"])
# add a column for month
df = df.assign(defect_month=df.defect_date.dt.strftime("%Y-%m"))

# stats on severity & costs of repairs
severity_stats = df.groupby("severity").agg(
    {"defect_type": "count", "repair_cost": "sum"}
)
severity_stats.rename(columns={"defect_type": "counts"}, inplace=True)

# monthly defects
monthly_defects = df.groupby("defect_month", as_index=False).product_id.count()

# add a bar chart for defects by month
fig, ax = plt.subplots(figsize=(8, 4))
g = sns.barplot(
    data=monthly_defects, x="defect_month", y="product_id", ax=ax, color="blue"
)
# _ = ax.set_title("Number of Defects by Month", color="red")
_ = ax.set_xlabel("")
_ = ax.set_ylabel("count")
_ = ax.bar_label(
    ax.containers[-1],
    fmt="Total Defects:\n%.0f",
    label_type="center",
    color="white",
    size=8,
    font="Verdana",
    style="oblique",
)

# product stats
product_stats = (
    df.groupby("product_id", as_index=False)
    .agg({"defect_id": "count", "repair_cost": "sum"})
    .sort_values(by="repair_cost", ascending=False)
)
top_repairs = product_stats[:10]


# ------------------------ start app ------------------------
st.title("Defective Products Insights")
st.dataframe(
    data=df.head(20),
    hide_index=True,
    use_container_width=True,
)

st.divider()
st.subheader("📈 Monthly Product Defect Trends", divider="grey")
st.write("  ")
# add left and right columns
left, right = st.columns(2, gap="small")
# plot figure
left.pyplot(fig=fig, use_container_width=True)


right.dataframe(
    monthly_defects.style.format(thousands=",", precision=2).highlight_max(
        subset=["product_id"]
    ),
    use_container_width=True,
)

# total repair costs
fig, ax = plt.subplots(figsize=(6, 4))
g = sns.barplot(
    data=top_repairs,
    y="product_id",
    x="repair_cost",
    order=top_repairs.product_id,
    palette="Set1",
    errorbar=None,
    orient="h",
)
_ = ax.get_xaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, p: format(int(x), ","))
)
_ = ax.set_xlabel("Total Repair Cost")
_ = ax.set_ylabel("Product Id")


st.subheader(
    "💰Top 10 Product Repair Cost",
    divider="blue",
)
left_col, right_col = st.columns(2, gap="small")
# plot figure
left_col.pyplot(fig=fig, use_container_width=True)

# show dataframe
right_col.dataframe(
    top_repairs.style.format(thousands=",", precision=2).highlight_max(
        subset=["repair_cost"]
    ),
    use_container_width=True,
    hide_index=True,
)

# repairs by inspection
inspection_avg_costs = df.groupby(
    ["defect_month", "inspection_method"], as_index=False
).agg({"product_id": "count", "repair_cost": "mean"})

left_col2, right_col2 = st.columns(2, gap="small")
left_col2.subheader(
    "📝 Repair Cost by Inspection Method",
    divider="blue",
)
left_col2.bar_chart(
    data=inspection_avg_costs,
    x="defect_month",
    y="repair_cost",
    horizontal=False,
    color="inspection_method",
    x_label="",
    y_label="Repair Cost",
    use_container_width=True,
)


# repairs by severity
severity_avg_costs = df.groupby(["defect_month", "severity"], as_index=False).agg(
    {"product_id": "count", "repair_cost": "mean"}
)

right_col2.subheader(
    "📝 Repair Cost by Severity Method",
    divider="blue",
)

right_col2.bar_chart(
    data=severity_avg_costs,
    x="defect_month",
    y="repair_cost",
    horizontal=False,
    color="severity",
    x_label="",
    y_label="Repair Cost",
    use_container_width=True,
)
