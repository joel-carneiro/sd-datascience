import telebot
import openai

def generate_text(prompt):
    completions = openai.Completion.create(
		engine='text-davinci-002',
		prompt=prompt,
		max_tokens=2048,
		n=1, stop=None,
		temperature=1,
		api_key='')

    message = completions.choices[0].text

    return message.strip()

# Criando o bot

API_KEY = '6019897583:AAFrZ4Thi9xL1Yl18WzQOGhgX1sIoC0Unsc'
bot = telebot.TeleBot(API_KEY)

PARAMETERS = ' (Voce)'


@bot.message_handler()
def response(message):
    
    print(message.text)
    
    text_response = generate_text(message.text + PARAMETERS)
    
    bot.reply_to(message, text_response)
    
bot.polling()
