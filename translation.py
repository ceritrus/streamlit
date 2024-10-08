from openai import OpenAI

def translate(prompt: str, client: OpenAI):
    return client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "text": "You are a translation expert, you get sent a sentence in any language and return a json file containing pairs of keys and languages in their complete english name representing the translation of the original sentence in the 10 most used languages.",
            "type": "text"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Hello, how are you?"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "text": "{\n  \"english\": \"Hello, how are you?\",\n  \"spanish\": \"Hola, ¿cómo estás?\",\n  \"chinese\": \"你好，你好嗎？\",\n  \"hindou\": \"नमस्ते, तुम कैसे हो?\",\n  \"arabic\": \"مرحبًا، كيف حالك؟\",\n  \"portuguese\": \"Olá, como estás?\",\n  \"french\": \"Bonjour, comment vas tu?\",\n  \"russian\": \"Привет, как ты?\",\n  \"japanese\": \"こんにちは、元気ですか？\",\n  \"german\": \"Hallo, wie geht es dir?\"\n}",
            "type": "text"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "I am doing well, just ate some pasta"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "text": "{\n  \"english\": \"I am doing well, just ate some pasta\",\n  \"spanish\": \"Estoy bien, acabo de comer algo de pasta\",\n  \"chinese\": \"我过得很好，刚吃了一些面食\",\n  \"hindou\": \"मैं अच्छा हूँ, बस कुछ पास्ता खा लिया\",\n  \"arabic\": \"أنا بخير، لقد تناولت للتو بعض المعكرونة\",\n  \"portuguese\": \"Estou bem, acabei de comer um pouco de massa\",\n  \"french\": \"Je vais bien, je viens de manger des pates\",\n  \"russian\": \"Я хорошо себя чувствую, только что поел немного пасты\",\n  \"japanese\": \"元気です、ちょうどパスタを食べました\",\n  \"german\": \"Mir geht es gut, ich habe gerade etwas Pasta gegessen\"\n}",
            "type": "text"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "How do you make a baguette, do you need chili oil?"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "text": "{\n  \"english\": \"How do you make a baguette, do you need chili oil?\",\n  \"spanish\": \"¿Cómo se hace una baguette, necesitas aceite de chile?\",\n  \"chinese\": \"如何制作法棍面包，需要辣椒油吗？\",\n  \"hindou\": \"बागेट कैसे बनती है, क्या आपको मिर्च का तेल चाहिए?\",\n  \"arabic\": \"كيف تصنع البغيت، هل تحتاج لزيت الفلفل الحار؟\",\n  \"portuguese\": \"Como se faz uma baguete, precisa de óleo de pimenta?\",\n  \"french\": \"Comment faites-vous une baguette, avez-vous besoin d'huile de piment?\",\n  \"russian\": \"Как приготовить багет, нужно ли вам острое масло?\",\n  \"japanese\": \"バゲットはどうやって作るのか、唐辛子油は必要ですか？\",\n  \"german\": \"Wie macht man ein Baguette, braucht man Chilöl?\"\n}",
            "type": "text"
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