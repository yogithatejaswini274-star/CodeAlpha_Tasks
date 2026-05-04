import streamlit as st
from deep_translator import GoogleTranslator

# 🌸 Rose pink background + report style
st.markdown("""
<style>
.stApp {
    background-color: #fff0f5;
}
</style>
""", unsafe_allow_html=True)

# 🌍 Report-style title
st.markdown("""
<h1 style='
    text-align: center;
    font-family: "Times New Roman", serif;
    font-size: 36px;
    font-weight: bold;
    color: black;
'>
🌍 Language Translator 🌍
</h1>

<hr style='border: 1px solid #ccc; width: 70%; margin: auto;'>
""", unsafe_allow_html=True)

languages = {
    "Hindi": "hi", "English": "en", "Telugu": "te", "Tamil": "ta",
    "Kannada": "kn", "Malayalam": "ml", "Bengali": "bn", "Gujarati": "gu",
    "Marathi": "mr", "Punjabi": "pa", "Urdu": "ur", "Odia": "or",
    "Spanish": "es", "French": "fr", "German": "de", "Chinese": "zh-CN",
    "Japanese": "ja", "Korean": "ko", "Arabic": "ar", "Russian": "ru",
    "Portuguese": "pt", "Italian": "it", "Turkish": "tr", "Dutch": "nl",
    "Thai": "th"
}

# Session state
if "source" not in st.session_state:
    st.session_state.source = "English"
if "target" not in st.session_state:
    st.session_state.target = "Hindi"
if "translated" not in st.session_state:
    st.session_state.translated = ""

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "From",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.source)
    )
    text = st.text_area("Enter text")

with col2:
    target = st.selectbox(
        "To",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.target)
    )

# Swap
if st.button("🔄 Swap Languages"):
    st.session_state.source, st.session_state.target = (
        st.session_state.target,
        st.session_state.source,
    )
    st.rerun()

# Translate
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            with st.spinner("Translating..."):
                translated = GoogleTranslator(
                    source=languages[source],
                    target=languages[target]
                ).translate(text)

                st.session_state.translated = translated
        except Exception as e:
            st.error(f"Error: {e}")

# Output
if st.session_state.translated:
    st.text_area("Translation", value=st.session_state.translated, height=200)

    st.download_button(
        "📋 Download",
        st.session_state.translated,
        file_name="translation.txt"
    )