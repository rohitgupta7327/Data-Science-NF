# A company tracked its monthly sales performance during the year 2025.  The data is given below:

# info = {
#     "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

#     "Units_Sold": [10, 15, 20, 18, 25, 30,
#                    35, 32, 28, 40, 45, 50],

#     "Revenue": [100, 150, 200, 180, 250, 300,
#                 350, 320, 280, 400, 450, 500]
# }
# Tasks
# 1. Line Plot:  Create a line graph showing the monthly revenue trend throughout the year.

# 2. Bar Chart:  Create a bar chart displaying units sold each month.

# 3. Pie Chart:  Show the percentage contribution of revenue for the first six months (Jan–Jun).

# 4. Histogram:  Create a histogram of monthly revenues to analyze the distribution of revenue values.

# 5. Scatter Plot:  Plot Units Sold vs Revenue and examine whether there is a relationship between them.




##########################################
# Line Plot: Monthly Revenue Trend
###########################################
import pandas as pd
import matplotlib.pyplot as plt
info = {
    "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

    "Units_Sold": [10, 15, 20, 18, 25, 30,
                   35, 32, 28, 40, 45, 50],

    "Revenue": [100, 150, 200, 180, 250, 300,
                350, 320, 280, 400, 450, 500]
}
plt.figure(figsize=(10, 5))

plt.plot(
    info["Months"],
    info["Revenue"],
    color="blue",
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Revenue"
)
# Show value at each coordinate
for month, revenue in zip(info["Months"], info["Revenue"]):
    plt.text(
        month,          # x-coordinate
        revenue + 5,    # y-coordinate (slightly above point)
        str(revenue),   # text to display 
        ha='center' 
    )
plt.title("Month VS Reveue")
plt.xlabel("Months") 
plt.ylabel("Revenue") 
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

plt.show()

##########################################
# Bar Chart: Monthly Revenue Trend
###########################################
from matplotlib.legend import Legend
import matplotlib.pyplot as plt

info = {
    "Months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

    "Revenue": [100, 150, 200, 180, 250, 300,
                350, 320, 280, 400, 450, 500]
}

bars = plt.bar(
    info["Months"],
    info["Revenue"],
    color="skyblue",
    edgecolor="black",
    label="Monthly Revenue"      # Added label for the legend
)

# Show values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 5,
        str(height),
        ha='center'
    )

plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.legend() 
plt.show()

##########################################
# Pie Chart: Monthly Revenue Trend
###########################################

import matplotlib.pyplot as plt

revenue = [100, 150, 200, 180, 250, 300,
           350, 320, 280, 400, 450, 500]

quarters = [
    sum(revenue[0:3]),   # Q1
    sum(revenue[3:6]),   # Q2
    sum(revenue[6:9]),   # Q3
    sum(revenue[9:12])   # Q4
]

labels = ["Q1", "Q2", "Q3", "Q4"]

plt.figure(figsize=(8,8))

plt.pie(
    quarters,
    labels=labels,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(quarters)/100)})',
    startangle=90,
    shadow=True
)

plt.title("Quarter-wise Revenue Distribution")
plt.tight_layout()
plt.show()


##########################################
# Scatter Chart: Monthly Revenue Trend
###########################################

import matplotlib.pyplot as plt

info = {
    "Units_Sold": [10,15,20,18,25,30,35,32,28,40,45,50],

    "Revenue": [100,150,200,180,250,300,350,320,280,400,450,500],

    "Months": ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]
}

plt.figure(figsize=(8,5))

plt.scatter(
    info["Units_Sold"],
    info["Revenue"],
    color="green",
    s=100
)

# Show month names beside points
for month, x, y in zip(
        info["Months"],
        info["Units_Sold"],
        info["Revenue"]):

    plt.annotate(
        month,
        (x, y),
        textcoords="offset points",
        xytext=(5,5)
    )
plt.colorbar(label="intensity")
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue")
plt.grid(True, alpha=0.6)

plt.show()