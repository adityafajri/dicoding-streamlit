# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
import plotly.graph_objects as go

order_payments_df = pd.read_csv('data/order_payments_dataset.csv')
new_order_payments_df = order_payments_df.drop(order_payments_df[order_payments_df['payment_type'] == 'not_defined'].index)


labels = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu']
values = [11960, 16196, 15963, 15552, 14761, 14122, 10887]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
st.plotly_chart(fig)


st.sidebar.success("Silahkan pilih salah satu menu diatas")
st.markdown(
    """
        ### Dalam satu minggu, pada hari apa para pelanggan cenderung untuk melakukan online shopping?
        - Customer cenderung melakukan transaksi pada hari senin
        - Hal ini cukup mengejutkan, mengingat traffic tertinggi adalah pada weekdays bukan pada weekend
    """
    )