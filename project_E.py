import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# 1. Setup Database Connection (Using localhost for now)
import urllib.parse
from sqlalchemy import create_engine

# 1. Define your password
password = 'Shivaprasad@0'

# 2. Encode the password (this turns @ into %40)
safe_password = urllib.parse.quote_plus(password)

# 3. Use an f-string to insert the safe_password into the URL
# Note the 'f' before the opening quote and {safe_password} inside
engine = create_engine(f'mysql+pymysql://root:{safe_password}@localhost:3306/ecommerce')

st.title("Team Data Entry Portal")

# 2. Load Data from the 'records' table
try:
    df = pd.read_sql('SELECT * FROM records', engine)
    
    # 3. The Editor
    st.write("Edit the table below:")
    edited_df = st.data_editor(df, num_rows="dynamic", key="data_editor")

    # 4. Save Button (Saving back to 'records' so it persists)
    if st.button("Commit Changes"):
        edited_df.to_sql('records', engine, if_exists='replace', index=False)
        st.success("Database Updated Successfully!")
        
except Exception as e:
    st.error(f"Connection Error: {e}")