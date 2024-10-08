import streamlit as st
import json
import openai
from translation import translate
from generation import generate
from code import code
from summary import summary

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