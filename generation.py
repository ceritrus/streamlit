import openai

def generate(prompt: str, client: openai.Client):
    return client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "text": "Your are an awarded writer for an online blog, your job is to write catchy articles under 500 words around themes given by the user. Since this is for a blog, your text should be easily understandable and interesting to please the search engine optimisation algorithms.",
          "type": "text"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Theme: The neverending cycle of work/sleep"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Title: The Work-Sleep Cycle: Breaking Free from the Grind\n\nDo you ever feel like you're trapped in a never-ending cycle of work and sleep? You're not alone. In today's fast-paced world, it's easy to get caught up in the daily grind of job responsibilities and the need for rest, creating a cycle that can be hard to break.\n\nOur society often glorifies the hustle and encourages working long hours, leaving little time for relaxation and self-care. This constant cycle of work and sleep can lead to burnout, stress, and a decrease in overall well-being.\n\nBreaking free from this cycle is vital for maintaining a healthy work-life balance. Here are a few tips to help you escape the endless loop:\n\n1. Prioritize self-care: Make time for activities that bring you joy and relaxation. Whether it's reading a book, taking a walk in nature, or practicing mindfulness, self-care is essential for recharging your batteries.\n\n2. Set boundaries: Learn to say no to extra work hours and commitments that can interfere with your personal time. Establishing boundaries between work and leisure is crucial for preventing burnout.\n\n3. Create a bedtime routine: Establishing a consistent sleep schedule can improve the quality of your rest. Engage in calming activities before bed, such as reading or meditating, to signal to your body that it's time to wind down.\n\n4. Incorporate movement: Regular exercise can boost your energy levels and improve the quality of your sleep. Find a physical activity that you enjoy, whether it's yoga, running, or dancing, and make it a part of your weekly routine.\n\n5. Seek support: Don't be afraid to reach out for help if you're feeling overwhelmed. Whether it's talking to a friend, a therapist, or a support group, finding a support system can offer new perspectives and coping strategies.\n\nRemember, breaking the work-sleep cycle is a gradual process that requires patience and self-compassion. By prioritizing self-care, setting boundaries, establishing healthy routines, and seeking support, you can take the necessary steps to reclaim your time and well-being.\n\nIt's time to break free from the never-ending cycle of work and sleep and create a life that prioritizes your health and happiness. You deserve it."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Theme: The rise and fall of sliced bread in the european culture"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Title: From Revolution to Staple: The Fascinating Journey of Sliced Bread in European Culture\n\nSliced bread, considered a convenience in modern times, has a captivating history that mirrors the evolution of European culture. From its revolutionary debut to becoming a household staple, the ascent and descent of sliced bread provide insights into changing consumer preferences and societal trends.\n\nThe invention of sliced bread in Europe dates back to the early 20th century, with the first automatic bread-slicing machine introduced in 1928 by Otto Frederick Rohwedder in Germany. This innovation revolutionized the way bread was packaged, sold, and consumed, saving time and effort for households across the continent.\n\nThe convenience of pre-sliced bread quickly gained popularity, becoming a symbol of modernity and efficiency. During World War II, sliced bread became a crucial staple in many European countries, providing a readily available and rationed food source for civilians amid challenging times.\n\nIn the post-war era, sliced bread continued to rise in prominence as industrialization and urbanization led to changes in consumer behaviors. The widespread adoption of packaged, sliced bread reflected the shift towards convenience and mass production in European society.\n\nHowever, as European culture began embracing artisanal and traditional food practices in recent years, the popularity of sliced bread has experienced a decline. Consumers are increasingly seeking out handmade, locally sourced bread with natural ingredients, eschewing the uniformity and preservatives often found in sliced bread.\n\nDespite this shift, sliced bread remains a staple in many European households, valued for its convenience, affordability, and versatility. Whether enjoyed as toast for breakfast, sandwiches for lunch, or breadcrumbs for cooking, sliced bread continues to hold a significant place in European culinary traditions.\n\nAs European culture undergoes further changes in response to sustainability concerns and health-conscious trends, the future of sliced bread remains intriguing. Will it continue to adapt to evolving consumer preferences, or will it be surpassed by new innovations in the baking industry?\n\nThe rise and fall of sliced bread in European culture narrate a compelling story of innovation, tradition, and changing tastes. As we toast our next sandwich or savor a slice of toast, let's reflect on the journey of this humble yet iconic staple in our culinary heritage."
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
    },
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