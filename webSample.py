import streamlit as st
import pandas as pd

# data = sampleData
data = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
        "third column": [100, 200, 300, 400],
        "fourth column": [140, 210, 310, 410],
    }
)


def showGraph():
    st.line_chart(data)


def showTable():
    st.table(data)


if __name__ == "__main__":

    if (st.button("Click me", key=1, help="Don't Click me...")):
        showGraph()
        showTable()
