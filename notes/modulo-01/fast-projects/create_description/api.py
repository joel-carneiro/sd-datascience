import openai

def generate_text(prompt):
    completions = openai.Completion.create(
		engine='text-davinci-002',
		prompt=prompt,
		max_tokens=2048,
		n=1, stop=None,
		temperature=0.5,
		api_key='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')

    message = completions.choices[0].text

    return message.strip()


def describe(title):
    generate_text(f'A partir desse título, gere um descrição para o youtube, com 15 linhas: {title}')


def hashtags(describe):
    generate_text(f'A partir dessa descrição, gere 10 hashtags para o youtube: {describe}')


if __name__ == '__main__':
    title = input('Insira aqui o título do vídeo: ')

    describe_text = describe(title)
    print(describe_text)
    hashtags_text = hashtags(describe_text)
    print(hashtags_text)

    print('# ', title)
    print('> ', describe_text)
    print('* ', hashtags_text)

