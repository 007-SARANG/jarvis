import streamlit as st

def userData():
  st.title("📦 User Data")
  key = st.text_input("Enter the Super Admin key", type="password")
  if st.button("Show Data") and key == st.secrets["SUPER_ADMIN_KEY"]:
    from database.mongodb import show_data
    data = show_data()
    st.dataframe(data)
  else:
    st.info("Provide the correct key to view the data", icon="ℹ️")

userData()
