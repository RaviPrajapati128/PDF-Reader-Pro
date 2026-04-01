import streamlit as st
#import pyttsx3                   
from PyPDF2 import PdfReader  
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.title("📘 PDF Reader Pro")

file = st.file_uploader(" ",["pdf"])
st.divider()

def con(file):
    st.sidebar.title("⚙️ Control Panel")

    reader = PdfReader(file)   
    pages = reader.pages                    

    n_page = len(reader.pages) - 1
    
    i = st.sidebar.number_input("📄 Enter Page Number:",min_value=0, max_value=n_page, step=1)
    st.sidebar.info("Note:- Here page number starts from 0")
    st.write("You are on Page:",i+1)
    #melo = pyttsx3.init()     
    page = reader.pages[i]    
    text = page.extract_text()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Text")
        st.info(text)

    with col2:
        st.subheader("Translated Text")
        target = st.sidebar.selectbox("Choose target language:",["English","Hindi","Gujarati","Marathi","Bengali"])
        if target == "Hindi":
            translated = GoogleTranslator(source='en', target='hi').translate(text)
            st.success(translated)
        if target == "Marathi":
            translated = GoogleTranslator(source='en', target='mr').translate(text)
            st.success(translated)
        if target == "Gujarati":
            translated = GoogleTranslator(source='en', target='gu').translate(text)
            st.success(translated)
        if target == "English":
            translated = GoogleTranslator(source='en', target='en').translate(text)
            st.success(translated)
        if target == "Bengali":
            translated = GoogleTranslator(source='en', target='bn').translate(text)
            st.success(translated)
        
    if st.sidebar.button("🔊 Create audio file",use_container_width=True):
        if target == "Hindi":
            tts = gTTS(text=translated, lang="hi")
            tts.save("audio(hindi).mp3")
            os.system("start audio(hindi).mp3")
    
        elif target == "Gujarati":
            tts = gTTS(text=translated, lang="gu")
            tts.save("audio(gujarati).mp3")
            os.system("start audio(gujarati).mp3")

        elif target == "Marathi":
            tts = gTTS(text=translated, lang="mr")
            tts.save("audio(marathi).mp3")
            os.system("start audio(marathi).mp3")

        elif target == "Bengali":
            tts = gTTS(text=translated, lang="be")
            tts.save("audio(bengali).mp3")
            os.system("start audio(bengali).mp3")

        elif target == "English":
            tts = gTTS(text=translated, lang="en")
            tts.save("audio(english).mp3")
            os.system("start audio(english).mp3")

    st.sidebar.download_button(
    label="📥 Download Translated Text",
    data=translated,
    file_name="translated.txt",
    mime="text/plain",
    use_container_width = True
)

if file is not None:
    con(file)

st.write("📝 Description")
st.write("""
PDF Reader Pro is a smart, multilingual document assistant designed to help you read, translate, and interact with PDF content effortlessly. With a sleek interface and intuitive controls, it allows you to:
- 📄 Upload PDF files up to 200MB.
- 🔢 Select specific pages for focused reading.
- 🌍 Choose target languages for instant translation.
- 🔊 Play translated text aloud using built-in audio controls.
- 🔇 Stop playback anytime.
- 🧠 Compare original and translated text side-by-side for clarity and learning.
- 📥 Download translated text as a file for study or sharing.""")

st.markdown("---")
st.markdown("Developed by Ravi Prajapati using Streamlit & Python")


