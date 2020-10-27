import streamlit as st
import pandas as pd
import numpy as np

st.title(""" Hello World!""" )
st.write( """
Let's check some facts!
""" )

# Collect data, aggregate number of students
data = pd.read_csv('wo_inges_ho.csv', delimiter=';')
st.button("Re-run")

st.title("Exploratory Analysis")
print(data.describe())

time_series = data.iloc[:,-10:].sum()
st.line_chart(time_series)

student_growth = np.diff(time_series.values)
st.line_chart(student_growth)

# Perform RDD

# Interpret results, write conclusion
