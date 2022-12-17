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

prompt = "I want you to act as an advertiser. You will create a campaign to promote a product or service of your choice. You will choose a target audience, develop key messages and slogans, select the media channels for promotion, and decide on any additional activities needed to reach your goals. My first suggestion request is"

def main():
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

    stats, dialog = st.columns([2, 1])
    with stats:
        with st.expander("Overview", expanded=True):
            tab1, tab2, tab3 = st.tabs(["Overview", "Posts", "Impressions"])
        
    with dialog:
        with st.expander("Suggestions", expanded=True):
            st.text("lorem ipsum ......")

            # for message_ in message_history:
            #     message(message_)   # display all the previous message

            # placeholder = st.empty()  # placeholder for latest message
            # input_ = st.text_input("you:")
            # message_history.append(input_)


            # with placeholder.container():
            #     message(message_history[-1]) # display the latest message

    with st.sidebar:
        with st.expander("Generate Post", expanded=True):
            input = st.text_area("What kind of post do you want me to generate?:")
            
            if st.button("Generate"):
                response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)

            st.text("AI:")
            placeholder = st.empty()
            with placeholder.container():
                if response.choices[0].text:
                    st.text(response.choices[0].text)
            

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