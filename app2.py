import streamlit as st
import pandas as pd
import numpy as np
import os

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)



# Initialize connection.
conn = st.connection('mysql', type='sql', username='davis2024irwan', password='wh451n9m@ch1n3', host='kubela.id', database='aw')
# conn = st.connection(**st.secrets.db_credentials)
# conn = st.connection("mydb", type="sql", autocommit=True)

# Perform query.
df = conn.query('SELECT EnglishPromotionName, StartDate, EndDate, MaxQty from dimpromotion limit 10;', ttl=600)

st.table(df)
# Print results.
# for row in df.itertuples():
#     st.write(f"{row.EnglishPromotionName} , {row.MaxQty} ")
