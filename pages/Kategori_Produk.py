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

product_df = pd.read_csv("https://raw.githubusercontent.com/adityafajri/dicoding-streamlit/main/data/products_dataset.csv")
top_product = product_df["product_category_name"].value_counts().sort_values(ascending=False)[:10]

fig = go.Figure()

fig.add_trace(go.Bar(
        x=top_product.values,
        y=top_product.index,
        orientation='h',
        marker=dict(
            color=["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3"
                   ,"#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3","#D3D3D3"],
        )
    ))

fig.update_layout(
        title='Produk yang memiliki kategori terbanyak',
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
        ### Produk apa saja yang memiliki jenis / kategori paling banyak pada olist e-commerce?
        - cama_mesa_baho atau dalam bahasa indonesia diartikan sebagai kamar mandi meja tempat tidur
        - esporte_lazer atau dalam bahasa indonesia diartikan sebagai rekreasi olahraga
        - moveis_decoraco atau dalam bahasa indonesia diartikan sebagai furnitur dekorasi
        - beleza_saude atau dalam bahasa indonesia diartikan sebagai kecantikan 
        - utilidades_domesticas atau dalam bahasa indonesia diartikan sebagai utilitas domestik
        - automotivo atau dalam bahasa indonesia diartikan sebagai otomotif
        - informatica_acessorios atau dalam bahasa indonesia diartikan sebagai aksesoris komputer
        - brinquedos atau dalam bahasa indonesia diartikan sebagai mainan
        - relogios_presentes atau dalam bahasa indonesia diartikan sebagai jam tangan hadiah
        - telefonia atau dalam bahasa indonesia diartikan sebagai telepon
    """
    )