import openai

def generate_text(prompt):
    completions = openai.Completion.create(
		engine='text-davinci-002',
		prompt=prompt,
		max_tokens=2048,
		n=1, stop=None,
		temperature=0.5,
		api_key='')

    message = completions.choices[0].text

    return message.strip()

