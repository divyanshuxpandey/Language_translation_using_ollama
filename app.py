import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.llms import Ollama

# Initialize the model
model = Ollama(model="llama3.1:8b")

# Define prompt template
generic_template = "Translate the following into {language}: {text}"
prompt = ChatPromptTemplate.from_messages(
    [("system", generic_template)]
)

# Set up the output parser
parser = StrOutputParser()

# Chain the prompt, model, and parser
chain = prompt | model | parser

# Streamlit app
st.title("Language Translator Project using Ollama")

# Input fields
input_text = st.text_input("Type the word or sentence", "Hello")
input_language = st.text_input("Translation Language", "Swedish")

# Button to trigger translation
if st.button("Translate"):
    try:
        translated_output = chain.invoke({"language": input_language, "text": input_text})
        st.write("**Translated Output:**", translated_output)
    except Exception as e:
        st.error(f"Error During Translation: {e}")
