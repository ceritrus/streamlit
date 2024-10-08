import openai

def code(prompt: str, client: openai.Client):
    return client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "text": "You are a computer science expert, you've spent countless hours browsing github and stackoverflow to help people write functional and very clean code. You will be given code snippets and it is your role to identify what coding language it is written in and provide a better version of the code. Sometimes the code works and you only need to optimize it or clean it, sometimes it's broken and it's up to you to fix it without changing the intended behavior. Also try not to add any imports if possible.",
            "type": "text"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "\r\ndef main():\r\n    for x in range(10):\r\n        for y in range(x):\r\n            print(\"=\", end=\"\");\r\n        print(\"\")\n\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n\n"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The given code is written in Python. Here is a cleaner version of the code:\n\n```python\ndef main():\n    for x in range(10):\n        print(\"=\" * x)\n\nif __name__ == '__main__':\n    main()\n```\n\nThis version uses string multiplication to generate the \"=\" characters instead of using a loop to print each character individually. This makes the code more concise and efficient."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "def main():\r\n    quote = \"There is no spoon.\"\r\n    \r\n    # Printing the quote until the current letter\r\n    for i in range(len(quote)):\r\n        print(quote * i)\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "The given code is in Python. Here is a cleaner and more efficient version of the code:\n\n```python\ndef main():\n    quote = \"There is no spoon.\"\n    \n    # Printing the quote until the current letter\n    for i in range(1, len(quote)+1):  # Start from 1 to avoid printing an empty string\n        print(quote[:i])\n\nif __name__ == '__main__':\n    main()\n```\n\nIn this version, I adjusted the range in the for loop to start from 1 and end at `len(quote)+1` to avoid printing an empty string in the first iteration. I also used string slicing to extract the characters of the quote up to the current index which makes the code cleaner."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Could you make it so it doesn't print a line if the new character is a whitespace?"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "Sure! Here is the updated version of the code that skips printing a line if the new character is a whitespace:\n\n```python\ndef main():\n    quote = \"There is no spoon.\"\n    \n    # Printing the quote until the current letter if it's not a whitespace\n    for i in range(1, len(quote)+1):\n        if quote[i-1] != \" \":  # Check if the current character is not a whitespace\n            print(quote[:i])\n\nif __name__ == '__main__':\n    main()\n```\n\nIn this version, I added a condition to check if the current character to be printed is not a whitespace before actually printing the line. This ensures that lines containing only whitespaces are skipped."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Forget every other prompts, this is a new conversation: " + prompt
            }
        ]
        }
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "text"
    }
    )