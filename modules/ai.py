from g4f.client import Client

client = Client()
# question = input("Введите свой вопрос")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "У тебя есть доступ в интернет?"}],

)
print(response.choices[0].message.content)

# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI

# llm = OpenAI(temperature=0.9, model_name="text-davinci-003")
# prompt = PromptTemplate(
#     input_variables=["question"],
#     template="What is the answer to: {question}?",
# )
# chain = LLMChain(llm=llm, prompt=prompt)

# result = chain.run("Какая температура в Париже сейчас?")
# print(result)