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

import time
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code

customers_df = pd.read_csv("https://raw.githubusercontent.com/adityafajri/dicoding-streamlit/main/data/customers_dataset.csv")
persebaran = customers_df["customer_state"].value_counts()

fig = go.Figure()

fig.add_trace(go.Bar(
        x=persebaran.values,
        y=persebaran.index,
        orientation='h',
        marker=dict(
            color=["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3"
                   ,"#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3"],
        )
    ))

fig.update_layout(
        title='Persebaran customer berdasarkan negara bagiannya',
        xaxis=dict(
            title='customer Count',
            tickfont=dict(
                size=12,
            ),
        ),
        yaxis=dict(
            tickfont=dict(
                size=12,
            ),
            automargin=True,
        ),
        width=1000,
        height=700,
    )

st.plotly_chart(fig)
st.sidebar.success("Silahkan pilih salah satu menu diatas")
st.markdown(
    """
        ### Bagaimana persebaran customer untuk setiap negara bagian?
        - Sebagian besar pelanggan berasal dari Sao Paulo (SP)
        - Diikuti oleh Rio de Janeiro (R) sebagai urutan kedua terbanyak
        - Untuk urutan selanjurnya silahkan melihat pada visualisasi diatas
    """
    )