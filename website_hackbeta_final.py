import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go

st.set_page_config(page_title="Hack Beta Demo", page_icon=":tada:", layout="wide")

# Header section
st.title("Leather Magazine International Data Visualization :briefcase:")

# Project description using in-line markdown
st.markdown("### *Sift through data processed with our customized NLP algorithm.*")

# Link to website where data was scraped from
st.write("[Link to original website >](https://www.leathermag.com)")

# Divider
st.divider()

# Subheader w/ markdown
st.markdown("# Interact with the data below!")

# Add a selectbox so user can search for certain categories
category_selectbox = st.selectbox(
    'What are you searching for?',
    ('Entities', 'Products', 'Events'),
)

# Customize display based on user input on category_selectbox
if category_selectbox == 'Entities':
    st.markdown("## Select a range of years:")
    # User has date range options to choose from
    year_selectbox = st.selectbox(
        'Select a five-year range below:',
        ('2005-2009', '2010-2014', '2015-2019', '2020-2024'),
    )

    # Display date range bigger using string splicing
    start_year = year_selectbox[:4]
    end_year = year_selectbox[-4:]

    st.markdown(f"## You are now viewing :red[{category_selectbox}] data between 1 January {start_year} and 31 December {end_year}")

    st.markdown("*Note that only five-year ranges are currently supported.*")

    # Attach images depending on date range selection
    if year_selectbox == '2005-2009':
        st.image('2005-2009-entities.png', width=1000)
    elif year_selectbox == '2010-2014':
        st.image('2010-2014-entities.png', width=1000)
    elif year_selectbox == '2015-2019':
        st.image('2015-2019-entities.png', width=1000)
    elif year_selectbox == '2020-2024':
        st.image('2020-2024-entities.png', width=1000)
elif category_selectbox == 'Products':
    st.markdown(f"## You are now viewing :red[{category_selectbox}] data for all time")
    # Only one photo option for now
    st.image('products-alltime.png', width=1000)
elif category_selectbox == 'Events':
    st.image('events-density.png', width=1000)
else:  # Check if something was entered incorrectly
    st.error("This data category is not yet supported.")

st.divider()

st.title("Our Process")
st.markdown("""1. We used the `nltk` Python library to craft our custom NLP algorithm.

2. We used `matplotlib` to visualize the data into bar graphs.
3. We used `streamlit` to wrap the data up into an interactive, pretty little website!

See our code at [Github](https://github.com/paueguibarr/Hack_Beta_CodeAmigos):space_invader:

""")

st.divider()

st.title("Next Steps")
st.markdown("""
Where are we taking the project from here?

- Add automatic graph generation for custom date ranges selected by user
- Add forecasting and predictions using machine learning
- Add media bias and fake news detection
- Add support for other media platforms


""")
