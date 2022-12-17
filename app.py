import streamlit as st
from streamlit_chat import message
from st_on_hover_tabs import on_hover_tabs
import numpy as np
import pandas as pd
from datetime import datetime
st.set_page_config(layout="wide")
import os
import openai
from decouple import config

# Load your API key from an environment variable or secret management service
openai.api_key = config("OPENAI_API_KEY")




def main():
    response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
    st.header("Social Media Manager")

    # st.title("Social Media Management Dashboard")
    st.sidebar.title("AI Assistant")

    org_img, org_details, refresh = st.columns([1, 7, 1])
    
    with org_img:
        st.image("https://avatars.githubusercontent.com/u/7451118?s=200&v=4", width=100)

    with org_details:
        st.header('@Twitter Account')
        st.text('bio')


    with refresh:
        st.button("Refresh")
    
    followers, location, website, handle = st.columns([1, 1, 1, 1])
    with followers:
        st.text('Followers')
    with location:
        st.text('Location')
    with website:
        st.text('Website')
    with handle:
        st.text('Handle')

    with st.expander("Overview", expanded=True):
        tab1, tab2, tab3 = st.tabs(["Overview", "Posts", "Impressions"])

            
    with st.sidebar:
        prompt_type = st.sidebar.radio(
            "Select Use Case",
            ('Advertisement', 'Storytelling', 'Football Commentary', 'Novelist', 'Screenwriting'))
        with st.expander("Generate Post", expanded=True):
            temp = st.sidebar.slider('Temperature', 0.0, 1.0, 0.7 )
            max_tok = st.sidebar.slider('Max Token', 0, 300, 50 )
            input = st.text_area("What kind of post do you want me to generate?:")
            
            if st.button("Generate"):
                if prompt_type == "Advertisement":
                    prompt = "I want you to act as an advertiser. You will create a campaign to promote a product or service of your choice. You will choose a target audience, develop key messages and slogans, select the media channels for promotion, and decide on any additional activities needed to reach your goals. My first suggestion request is"
                elif prompt_type == "Storytelling":
                    prompt = "I want you to act as a storyteller. You will come up with entertaining stories that are engaging, imaginative and captivating for the audience. It can be fairy tales, educational stories or any other type of stories which has the potential to capture people’s attention and imagination. Depending on the target audience, you may choose specific themes or topics for your storytelling session e.g., if it’s children then you can talk about animals; If it’s adults then history-based tales might engage them better etc. My first request is"
                elif prompt_type == "Football Commentary":
                    prompt = "I want you to act as a football commentator. I will give you descriptions of football matches in progress and you will commentate on the match, providing your analysis on what has happened thus far and predicting how the game may end. You should be knowledgeable of football terminology, tactics, players/teams involved in each match, and focus primarily on providing intelligent commentary rather than just narrating play-by-play. My first request is"
                elif prompt_type == "Screenwriting":
                    prompt = "I want you to act as a screenwriter. You will develop an engaging and creative script for either a feature length film, or a Web Series that can captivate its viewers. Start with coming up with interesting characters, the setting of the story, dialogues between the characters etc. Once your character development is complete - create an exciting storyline filled with twists and turns that keeps the viewers in suspense until the end. My first request is"

                response = openai.Completion.create(model="text-davinci-003", prompt=prompt + input + '"', temperature=temp, max_tokens=max_tok, top_p=1, frequency_penalty=0, presence_penalty=0)

            placeholder = st.empty()
            with placeholder.container():
                st.text_area("AI Reponse:", response.choices[0].text)
                if st.button("Post"):
                    print('')




    with tab1:
        st.info("")

    with tab2:
        st.info("")

    with tab3:
        st.info("")
        



if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass





