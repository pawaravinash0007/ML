import streamlit as st

# Page Title and Header
st.title("Explore Machine Learning Projects NIELIT Daman")

# Project Links and Descriptions
projects = {
    "Classification Machine Learning Project": {
        "description": "This project demonstrates classification algorithms.",
        "link": "https://avinashc.streamlit.app"
    },
    "Random Forest Machine Learning Project": {
        "description": "Random forest is a popular ensemble learning algorithm.",
        "link": "https://avinashrf.streamlit.app"
    },
    "Linear Regression Machine Learning Project": {
        "description": "Linear regression is a fundamental algorithm for regression tasks.",
        "link": "https://avinashli.streamlit.app"
    },
    "Logistic Regression Machine Learning Project": {
        "description": "Logistic regression is widely used for binary classification problems.",
        "link": "https://avinashlr.streamlit.app"
    }
}

# Displaying Projects with Descriptions and Links
for project, details in projects.items():
    st.header(project)
    st.markdown(details["description"])
    st.markdown(f"Click here to explore {project}")

# Footer
st.markdown("Discover various machine learning projects developed by Avinash Pawar at NIELIT Daman")
st.markdown("Feel free to Contact Avinash: 8329063970 for Machine Learning Project ")
