import streamlit as st
import os
import speech_recognition as sr 
from pydub import AudioSegment
from pydub.silence import split_on_silence
from scipy.io import wavfile
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from question_generator.questiongenerator import QuestionGenerator
from question_generator.questiongenerator import print_qa
import json
from question_generator.questiongenerator import QuestionGenerator
import numpy as np
import webbrowser

def app():
    st.title(" Revise Dashboard ")
    st.write(" This is the Revise dashboard made with Streamlit. Click the Drag and Drop featurn to select your audio file for your online class. The file must be a .wav file.")

    my_range = list(range(1,11))
    option=st.sidebar.select_slider("Choose number of Questions(Between 1 and 10):", options=my_range, value=10)

    r = sr.Recognizer()

    def get_large_audio_transcription(path):
        sound = AudioSegment.from_wav(path) 
        chunks = split_on_silence(sound,
            min_silence_len = 500,
            silence_thresh = sound.dBFS-14,
            keep_silence=500,
        )
        folder_name = "audio-chunks"
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        for i, audio_chunk in enumerate(chunks, start=1):
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    whole_text += text
        with open('data1.txt', 'w+') as f:
            f.write(whole_text)

        return whole_text
    def summarymaker(text):
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
        freqTable = dict() 
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        
        sentences = sent_tokenize(text)
        sentenceValue = dict()
        
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        
        # Average value of a sentence from the original text
        
        average = int(sumValues / len(sentenceValue))
        
        # Storing sentences into our summary.
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        out_file=open("summary_out.txt","w+")
        out_file.write(summary)
        return summary

    def Questions(summary,no):
        qg = QuestionGenerator()
        qa_list = qg.generate(
            summary, 
            num_questions=no, 
            answer_style='multiple_choice'
        )
        return qa_list

    qg = QuestionGenerator()

    def print_qs(qa_list,name,show_answers=True):
        st.subheader(f"Questions Based On {name} Topic:")
        for i in range(len(qa_list)):
            st.write(f"Q{i+1})"+qa_list[i]["question"])
            st.write("\n")

    uploaded_file = st.file_uploader("Choose a wav file")
    st.audio(uploaded_file, format='wav')

    try:
        with open(uploaded_file.name,"wb") as f:
            f.write(uploaded_file.getbuffer())
        text=get_large_audio_transcription(uploaded_file.name)
    except:
        st.error("Make sure to upload WAV file")
        url = 'https://forms.gle/6xUWXcJvKMtsUF5P7'
        if st.button('Feedback Form'):
            webbrowser.open_new_tab(url)
        st.stop()
    url = 'https://forms.gle/6xUWXcJvKMtsUF5P7'
    if st.button('Feedback Form'):
        webbrowser.open_new_tab(url)
    st.write("Summary:")

    #summary Generator

    summary1=summarymaker(text)
    st.write(summary1)

    #question generator

    questions=Questions(summary1,option)
    print_qs(questions,uploaded_file.name)




