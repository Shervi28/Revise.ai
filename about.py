import streamlit as st
import webbrowser

def app():
   

    url = 'https://forms.gle/6xUWXcJvKMtsUF5P7'
    if st.button('Feedback Form'):
        webbrowser.open_new_tab(url)
    
    st.title('A Word from the Creators')
    
    st.image('pika_cropped.png',width=250)
    st.markdown("""
    # Sqwatato
    (Jayden Lim)

    Hi my name is Jayden Lim, from US, and as of right now I am entering 9th grade. 
    I have experience with python and django and worked on the Frontend/UI for Revise.
    I think this project will be helpful for students having trouble with school and for student who are too lazy to watch lectures.
    Contact: sqwatato@gmail.com
    """)

    st.image('polandball.png')
    st.markdown("""
    # ConstantChaos28
    
    Hi my name is Shervin Antony and I am entering 8th grade. 
    I helped with the design of our app and I helped with proccessing the audio and made the AI Models with Varun.
    This app can help anyone with school on a day to day basis. You can use this app for understanding your school content as well as understanding youtube tutorials.
    Any questions or problems or wanna talk about this product? Contact Me : shervinantony28@gmail.com
    (Shervin Antony)
    """)

    st.image('discordlogored.png')
    st.markdown("""
    # Varun
 

    Hi my name is Varun Sampath Kumar Currently in Sophomore year at PSG College Of Technology, India.
    I helped my team formulate the idea and also with the audio processing, question generation.
    I think I have contributed to the betterness of the student community by enriching their study experience.
    Would love to collaborate and meet new people. So feel free to dm me @ Varunkavin5@gmail.com
    """)

    st.image('oumamimaLogo.png')
    st.markdown("""
    # Oimaima
    Hi I'm oimaima and I helped design the website and some logos!

    """)


    st.write('# About the Revise project')
    st.markdown("""
    ## Inspiration
We have all struggled in class, whether the teacher was unclear, or you're having trouble understanding a topic. If you don't understand the material, it will lead to failed exams and unnecessary stress. But now with our product, Revise, you can change that.

## What it does
All you need to do is upload the audio recording of your class(.wav file), and our AI models will give you a summary of what you have learned in class and it will give you a few questions to test your understanding.

## How we built it
We used streamlit to built the website for our app and we used NLTK, pytorch, transformers and numpy for our AI Models. In addition, we used pydub to process our audio files and speech recognition to convert the audio files to text.

## Challenges we ran into
One of our team members left right before the hackathon and we had to find a new member which proved a very hard task. We also had trouble processing large audio files as we could not install one of the necessary libraries. To add on, we had trouble communicating between different time zones. Originally we used Django to make our python app but we ran into issues deploying our AI models to the website. So we had to abandon our Django app, and start all over again with streamlit as our webapp framework.

## Accomplishments that we're proud of
We were proud to learn new technologies to make this this web app! We learned multiple new technologies like Natural Language Processing and StreamLit and we are also proud of the end result of our app! Seeing all the hard work put in being paid off is an amazing experience! We were proud that we were able to still manage to finish our app despite us switching web dev frameworks in the middle and starting all over again. 

## What we learned
We learned new technologies like NLP and Streamlit and many more. This entire hackathon was a great learning experience for all of us! We learned soooo many new things and we also improved our communication skills as they were essential for success.

## What's next for Revise
We need to implement a recording feature so you can record your meetings/classes and upload them directly to our AI. We also wanted to make our AI models and our entire website more efficient and faster as well as more accurate with answers in the future.
    """)
