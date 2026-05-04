import streamlit as st
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🌸 Background
st.markdown("""
<style>
.stApp {
    background-color: #fff0f5;
}
</style>
""", unsafe_allow_html=True)

# 🤖 Title
st.markdown("""
<h1 style='text-align:center; font-family:Times New Roman;'>
🤖 FAQ Chatbot
</h1>
<hr>
""", unsafe_allow_html=True)

# ✅ STEP 1: FAQ DATA (REQUIRED)
questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Python?",
    "What is a chatbot?",
    "What is NLP?"
]

answers = [
    "Artificial Intelligence is the simulation of human intelligence in machines.",
    "Machine Learning is a subset of AI that learns from data.",
    "Python is a popular programming language.",
    "A chatbot is a program that interacts with users.",
    "NLP helps computers understand human language."
]

# ✅ STEP 2: NLP PREPROCESSING (REQUIRED)
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)

    # remove punctuation
    tokens = [w for w in tokens if w not in string.punctuation]

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]

    return " ".join(tokens)

# preprocess FAQ questions
processed_questions = [preprocess(q) for q in questions]

# vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

# UI input
user_input = st.text_input("Ask your question:")

# button
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question")
    else:
        processed_input = preprocess(user_input)

        user_vec = vectorizer.transform([processed_input])
        similarity = cosine_similarity(user_vec, X)

        index = similarity.argmax()
        response = answers[index]

        st.success(f"🤖 {response}")
