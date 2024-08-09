import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime 


st.header('st.slider')

st.subheader('Slider')

age=st.slider('How old are you?', 0, 130, 25)
st.write("I'm", age, 'years old')


st.subheader('Range time slider')

appointment=st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12,45))
)
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)


# ~day7
# st.write('st.write')

# st.write('hello, *world!* :sunglasses:')

# st.write(1234)

# df = pd.DataFrame({
#     'first column': [1,2,3,4],
#     'second column':[10,20,30,40]
# })

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# df2 = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a','b','c'])

# c=alt.Chart(df2).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
# )
# st.write(c)


# day5

# st.write('hello world!')

# st.header('st.button')

# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')
