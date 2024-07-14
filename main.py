# Imports
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from utils import get_video_segments, format_transcript, get_gpt3_response
from openai import OpenAI
from constants import OPENAI_API_KEY, PROMPT_CONTEXT


# Streamlit page set up
st.title("Input Comprehension")

url = st.text_input("YouTube URL", "https://www.youtube.com/watch?v=BC6Wa27VVz0")
video_id = url.split("watch?v=")[1]

# Collect transcript
video_transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr'])
formatted_transcript = format_transcript(video_transcript)

# Play the video
st.video(url)

# Send transcript to gpt
client = OpenAI(api_key=OPENAI_API_KEY)
response = get_gpt3_response(client, PROMPT_CONTEXT, formatted_transcript)

# Display questions and transcript
with st.expander("See Questions"):
    st.markdown(response)

with st.expander("See Transcript"):
    st.markdown(formatted_transcript)