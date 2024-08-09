import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime 

st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('You selected:', options)


# day10
st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)

st.write('Your favorite color is ', option)


# day9
# st.header('Line chart')

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns = ['a','b','c']
# )

# st.line_chart(chart_data)




# day 8
# st.header('st.slider')

# st.subheader('Slider')

# age=st.slider('How old are you?', 0, 130, 25)
# st.write("I'm", age, 'years old')

# st.subheader('Range slider')

# values = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
# st.write('Values:', values)


# st.subheader('Range time slider')

# appointment=st.slider(
#     "Schedule your appointment:",
#     value=(time(11, 30), time(12,45))
# )
# st.write("You're scheduled for:", appointment)

# st.subheader('Datetime slider')

# start_time = st.slider(
#     "When do you start?",
#     value=datetime(2020, 1, 1, 9, 30),
#     format="MM/DD/YY - hh:mm"
# )
# st.write("Start time:", start_time)


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
