import streamlit as st

# Page Title and Header
st.title("Explore Machine Learning Projects")


# Project Links and Descriptions
projects = {
    "Classification Machine Learning Project": "Explore a classification machine learning project by Avinash Pawar. This project demonstrates classification algorithms.",
    "Random Forest Machine Learning Project": "Discover a random forest machine learning project developed by Avinash Pawar. Random forest is a popular ensemble learning algorithm.",
    "Linear Regression Machine Learning Project": "Check out a linear regression machine learning project by Avinash Pawar. Linear regression is a fundamental algorithm for regression tasks.",
    "Logistic Regression Machine Learning Project": "Explore a logistic regression machine learning project developed by Avinash Pawar. Logistic regression is widely used for binary classification problems."
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
