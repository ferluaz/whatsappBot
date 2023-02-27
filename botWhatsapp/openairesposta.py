import openai
import unicodedata

openai.api_key = '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'

model_engine = 'text-davinci-003'

def ai_response(whats_input):
    #oppen ai test
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = whats_input,
        max_tokens = 1024,
        temperature = 0.5,
    )
    resposta = completion.choices[0].text
    respostaAc = unicodedata.normalize("NFD", resposta)
    respostaAc = respostaAc.encode("ascii", "ignore")
    respostaAc = respostaAc.decode("utf-8")
    return respostaAc