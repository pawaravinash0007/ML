import streamlit as st

# Page Title and Header
st.title("Explore Machine Learning Projects NIELIT Daman")


# Project Links and Descriptions
projects = {
    "Classification Machine Learning Project": "This project demonstrates classification algorithms.",
    st.markdown(f"[Click here to explore {project}](https://avinashc.streamlit.app)")
    "Random Forest Machine Learning Project": "Random forest is a popular ensemble learning algorithm.",
    st.markdown(f"[Click here to explore {project}](https://avinashrf.streamlit.app)")
    "Linear Regression Machine Learning Project": "Linear regression is a fundamental algorithm for regression tasks.",
    st.markdown(f"[Click here to explore {project}](https://avinashli.streamlit.app)")
    "Logistic Regression Machine Learning Project": "Logistic regression is widely used for binary classification problems."
    st.markdown(f"[Click here to explore {project}](https://avinashlr.streamlit.app)")
}

# Displaying Projects with Descriptions and Links
for project, description in projects.items():
    st.header(project)
    st.markdown(description)
    st.markdown(f"[Click here to explore {project}](https://avinashc.streamlit.app)")

# Footer
st.markdown("Discover various machine learning projects developed by Avinash Pawar at NIELIT Daman")
st.markdown("Feel free to Contact Avinash: 8329063970 for Machine Learning Project ")

