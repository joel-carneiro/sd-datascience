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


def script():

    describe_p = 'Faça uma descrição de 30 linhas para meu vídeo do youtube, a qual tem o título: '

    title = input('Insira o título do vídeo: ')
    describe = generate_text(describe_p + title)
    hashtags = generate_text('Escolha 10 hashtags para um vídeo do youtube com essa descrição: ' + describe)
    print('# ', title, '\n')
    print('> ', describe, '\n')
    print('* ', hashtags, '\n')


if __name__ == '__main__':
    script()