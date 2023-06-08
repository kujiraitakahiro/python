import os
import sys
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_answer(question):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
      ]
    )
    return response.choices[0].message.content

if len(sys.argv) > 1:
    question = sys.argv[1]
    answer = get_answer(question)
    print("Answer:", answer)
else:
    print("Please provide a question as a command line argument.")

