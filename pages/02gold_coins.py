import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# To suppress Streamlit's deprecation warning for global use of pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)

# Path to the expense CSV file
excel_file_path = r"data/expense.csv"


# Function to perform the main analysis and display results
def execution():
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(excel_file_path)

    # Calculate and display the total amount converted to "gold coins"
    total = dataframe["Amount"].max()
    st.subheader(f"Gold coins : {str(int(total) // 200)}:coin:")

    # Date input fields for filtering expenses by date range
    date_from = st.date_input("From Date :date:")
    date_to = st.date_input("To Date :date:")

    # Slider for filtering expenses by amount range
    st.write("Amount :money_with_wings:")
    amount_min = st.slider("Minimum value",
                           min_value=0,
                           max_value=20000,
                           value=0,
                           step=10)
    amount_max = st.slider("Maximum value",
                           min_value=0,
                           max_value=20000,
                           value=20000,
                           step=10)

    # Multiselect for filtering expenses by category
    category = st.multiselect("Categories :card_index_dividers:", [
        "Housing", "Utilities", "Transportation", "Food", "Healthcare",
        "Insurance", "Debt Payments", "Entertainment", "Personal Care",
        "Education", "Savings", "Taxes", "Miscellaneous"
    ],
                              placeholder="You can choose multiple option(s)")

    # Convert the "Date" column to datetime format
    dataframe["Date"] = pd.to_datetime(dataframe["Date"])
    date_from, date_to = pd.to_datetime(date_from), pd.to_datetime(date_to)

    # Apply filters based on user inputs
    if len(category) == 0:
        condition = ((dataframe["Date"] >= date_from) &
                     (dataframe["Date"] <= date_to) &
                     (dataframe["Amount"] >= amount_min) &
                     (dataframe["Amount"] <= amount_max))
        dataframe = dataframe[condition]
    else:
        condition = ((dataframe["Date"] >= date_from) &
                     (dataframe["Date"] <= date_to) &
                     (dataframe["Amount"] >= amount_min) &
                     (dataframe["Amount"] <= amount_max) &
                     (dataframe["Category"].isin(category)))
        dataframe = dataframe[condition]

    # Display the filtered expenses
    st.title("Expenses :receipt:")
    st.dataframe(
        dataframe[["Category", "Description", "Currency Type","Amount"]].reset_index(drop=True))

    # Display a line chart of the filtered expenses by amount
    st.title("Amount :money_with_wings:")
    st.line_chart(dataframe["Amount"])

    # Display a pie chart of the filtered expenses by category
    st.title("Categories :card_index_dividers:")
    category_dataframe = dataframe.groupby('Category')['Amount'].sum()

    # Create a pie chart figure and axes
    fig, ax = plt.subplots()
    ax.pie(category_dataframe,
           labels=category_dataframe.index,
           autopct='%.2f',
           textprops={
               'fontsize': 8.5,
               "color": "black"
           },
           shadow=True)
    fig.set_facecolor('none')

    # Display the pie chart
    st.pyplot(fig)


# Try to execute the function and handle exceptions
try:
    execution()
except Exception as e:
    st.title("Please add some expenses :money_with_wings: ")
    st.write(e)
