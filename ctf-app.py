import streamlit as st

st.title(""" #Hello World!""" )
st.write( """
##Let's check some facts!
""" )

# Collect data, aggregate number of students
# Perform RDD
# Interpret results, write conclusion

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
