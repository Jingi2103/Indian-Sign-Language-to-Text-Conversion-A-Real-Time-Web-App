import streamlit as st

st.markdown(
   """<style>
body {
background-image: url('C:/Users/jino mathew/Desktop/streamlitenv/format-arw-PXjQaGxi4JA-unsplash.jpg');
background-size: cover;
}
</style>""",    unsafe_allow_html=True,
)

# Title of the web app
st.title("Hand sign recognition using Deep Learning models")

# Define a function for the signup page
def signup():
    st.title("Signup Page")
    
    # Create input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Create a signup button
    if st.button("Signup"):
        # Store the username and password (for demonstration purposes)
        st.session_state.signup_username = username
        st.session_state.signup_password = password
        # Redirect to the login page
        st.experimental_rerun()
        

# Define a function for the login page
def login():
    st.title("Login Page")
    
    # Check if signup information is available
    if "signup_username" in st.session_state and "signup_password" in st.session_state:
        st.write("Signup successful! You can now login.")
        
        # Create input fields for username and password
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # Create a login button
        if st.button("Login"):
            # Check if the entered username and password match the signup information
            if (username == st.session_state.signup_username) and (password == st.session_state.signup_password):
                st.success("Login successful!")
            else:
                st.error("Login failed. Please check your credentials.")
    else:
        st.write("You need to sign up first. Please go to the signup page.")

# Create a navigation sidebar to switch between pages
page = st.sidebar.selectbox("Choose a page", ("Signup", "Login"))

# Display the selected page
if page == "Signup":
    signup()
elif page == "Login":
    login()



    
