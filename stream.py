import streamlit as st
import json
import openai
from translation import translate
from generation import generate
from code import code
from summary import summary
import io
import requests
import base64
from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="OpenAI Assistant", page_icon="🤖", layout="centered")

client : openai.Client

def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True
	
def main():
	api_key = st.text_input("API Key", type="password")
	if (api_key != ""):
		if (not check_openai_api_key(api_key)):
			st.write(":red[API Key is invalid]")
		else:
			client = openai.Client(api_key=api_key)
			audio_bytes = audio_recorder(pause_threshold=10.0)
			# translate = st.toggle("Translate")
			if audio_bytes:
				# if translate:
				# 	print("Translating")
				# 	buffer = io.BytesIO(audio_bytes)
				# 	buffer.name = "recorded.mp3"
				# 	translation = client.audio.translations.create(
				# 		model="whisper-1",
				# 		file=buffer
				# 	)
				# 	st.markdown(f"{translation.text}")
				# else:
				buffer = io.BytesIO(audio_bytes)
				buffer.name = "segment.mp3"
				transcript = client.audio.transcriptions.create(
					model="whisper-1",
					file=buffer
				)
				st.markdown(f"{transcript.text}")
			col1, col2 = st.columns([3, 1], gap="large")
			with col2:
				st.radio("Mode", options=["Translation", "Generation", "Code", "Summary"], key="mode")
			with col1:
				prompt = st.text_area("Your prompt", "")
				if (prompt != ""):
					match st.session_state.mode:
						case "Translation":
							json_content = json.loads(translate(prompt, client).choices[0].message.content)
							for key, value in json_content.items():
								st.write(f"<b>{key.capitalize()}</b>:\n{value}", unsafe_allow_html=True)
						case "Generation":
							st.write(generate(prompt, client).choices[0].message.content)
						case "Code":
							st.write(code(prompt, client).choices[0].message.content)
						case "Summary":
							st.write(summary(prompt, client).choices[0].message.content)
				else:
					st.write("Please enter a prompt")
		
if __name__ == '__main__':
	main()