import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# To suppress Streamlit's deprecation warning for global use of pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)

# Path to the expense CSV file
excel_file_path = "data/expense.csv"


# Function to perform the main analysis and display results
def execution():
    try:
        # Read the CSV file into a DataFrame
        dataframe = pd.read_csv(excel_file_path)

        if len(dataframe) != 0:
            # Display the entry with the maximum amount spent
            max_Amount = dataframe[dataframe["Amount"] ==
                                   dataframe["Amount"].max()]
            st.subheader("You are spending the most here :cry:")
            st.dataframe(max_Amount.reset_index(drop=True))

            # Display the entry with the minimum amount spent
            min_Amount = dataframe[dataframe["Amount"] ==
                                   dataframe["Amount"].min()]
            st.subheader("You are spending the least here :blush:")
            st.dataframe(min_Amount.reset_index(drop=True))

            # Display the date with the most number of transactions
            st.subheader("You made the most number of transactions on :date:")
            most_transactions_date = dataframe.groupby(
                by="Date").size().nlargest(1).index
            st.dataframe(most_transactions_date)

            # Display the date with the least number of transactions
            st.subheader("You made the least number of transactions on :date:")
            least_transactions_date = dataframe.groupby(
                by="Date").size().nsmallest(1).index
            st.dataframe(least_transactions_date)

            # Display the category with the most spending
            mode_Category = dataframe["Category"].mode()
            st.subheader(
                "The categories for which you are spending the most :cry:")
            st.dataframe(mode_Category.reset_index(drop=True))

            # Display the category with the least spending
            st.subheader(
                "The categories for which you are spending the least :blush:")
            least_spent_category = dataframe['Category'].value_counts().idxmin(
            )
            st.dataframe(
                dataframe[dataframe['Category'] == least_spent_category]
                ["Category"].reset_index(drop=True))

            # Generate a word cloud from the 'Description' column
            Description_data = ' '.join(list(dataframe["Description"].values))

            def generate_wordcloud(text):
                wordcloud = WordCloud(width=400,
                                      height=400,
                                      background_color=None).generate(text)
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                st.pyplot()

            st.subheader("Description cloud :cloud:")
            generate_wordcloud(Description_data)
        else:
            st.header("Please add some expenses before analyzing it")
    except FileNotFoundError:
        st.header("Please add some expenses before analyzing it")


# Execute the main function
execution()
