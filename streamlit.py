from typing import Dict

import streamlit as st
from plagiarism_checker_template import PlagiarismChecker

import seaborn as sns
import matplotlib.pyplot as plt

plagiarism_checker = PlagiarismChecker()

header_html = '''<h1 style="color: #5e9ca0;">Plagiarism checker</h1>
<h2 style="color: #2e6c80;">Do not try to cheat! ...At least a lot :)</h2>'''

how_to = "Just upload your .txt files below. We'll do everything else for you!"


@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}


def main():
    """Run this function to run the app"""
    static_store = get_static_store()
    st.markdown(
        header_html, unsafe_allow_html=True,
    )
    st.info(how_to)
    result = st.file_uploader("Upload", type="txt")
    if result:
        #Process you file here
        value = result.getvalue()

        #And add it to the static_store if not already in
        static_store[result.name] = value.decode("utf-8")

    if st.button("Clear file list"):
        static_store.clear()

    if st.checkbox("Show file list?", True):
        st.write(f"Uploaded files:")
        for filename in static_store.keys():
            st.write(filename)

    if st.checkbox("Show content  of files?"):
        for name, value in static_store.items():
            st.write(name)
            st.code(value)

    if st.button('Check for plagiarism'):
        results = plagiarism_checker.check_plagiarism(static_store)
        fig, ax = plt.subplots()
        sns.heatmap(results, annot=True, ax=ax)
        st.write(fig)


main()