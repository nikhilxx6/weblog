import streamlit as st

# User inputs
name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father's name:")
Adr = st.text_area("Enter your address:")
classdata = st.selectbox("Enter your class:", (1, 2, 3, 4, 5, 6, 7, 8, 9))

# Custom CSS to style the button
st.markdown("""
    <style>
        .blue-button > button {
            background-color: #007bff; /* Blue color */
            color: white; /* Text color white */
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Display the button inside a div with a class
with st.container():
    st.markdown('<div class="blue-button">', unsafe_allow_html=True)
    button = st.button("DONE")
    st.markdown('</div>', unsafe_allow_html=True)

if button:
    # Displaying the information
    st.markdown(f"""
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Father's Name:</strong> {fname}</p>
        <p><strong>Address:</strong> {Adr}</p>
        <p><strong>Class:</strong> {classdata}</p>
    """, unsafe_allow_html=True)
