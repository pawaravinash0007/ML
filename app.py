import streamlit as st

# Page Title and Header
st.title("Explore Machine Learning Projects")


# Project Links and Descriptions
projects = {
    "This project demonstrates classification algorithms.",
    "Random forest is a popular ensemble learning algorithm.",
    "Linear regression is a fundamental algorithm for regression tasks.",
    "Logistic regression is widely used for binary classification problems."
}

# Displaying Projects with Descriptions and Links
for project, description in projects.items():
    st.header(project)
    st.markdown(description)
    st.markdown(f"[Click here to explore {project}](https://avinashc.streamlit.app)")

# Footer
st.markdown("Discover various machine learning projects developed by Avinash Pawar at NIELIT Daman")
st.markdown("Feel free to explore these projects and learn more about machine learning techniques!")
st.markdown("Contact Avinash Pawar: 8329063970")
