# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import openai

async def ai(query):
    openai.api_key = "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" #Your openai api key
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"{response}")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
