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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Aditya Fajri Melinianto",
    )

    st.write("# Dicoding Submission: Proyek Analisis Data")

    st.sidebar.success("Silahkan pilih salah satu menu diatas")

    st.markdown(
        """
       Selamat datang kepada senior reviewer dicoding atau teman-teman sekalian. Streamlit ini dibuat sebagai syarat kelulusan 
       salah satu kelas di Dicoding, yaitu Proyek Analisis Data.
        **Dataset yang digunakan adalah: Brazilian E-Commerce Public Dataset by Olist**
        ### Dimana saya bisa menemukan dataset ini?
        - Anda bisa menemukan dataset yang saya gunakan [disini](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
        - Jika ada saran dan kritik, teman-teman bisa menghubungi saya [disini](https://github.com/adityafajri)
        - Website ini saya buat menggunakan platform [streamlit](https://streamlit.io)
        ### Terimakasih kepada
        - Tuhan Yang Maha Esa
        - Indosat IDCamp yang sudah menyelenggarakan program beasiswa ini
        - Semua instructor, content writer, reviewer, dan pihak lain yang tidak bisa disebut satu persatu dari Dicoding Indonesia untuk materi yang luar biasa
        - Diri saya sendiri karena sudah berusaha sampai sejauh ini
    """
    )


if __name__ == "__main__":
    run()
