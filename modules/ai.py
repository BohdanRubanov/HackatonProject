from g4f.client import Client

client = Client()
# question = input("Введите свой вопрос")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Проверь, есть ли у этого текста признаки автоматической генерации? Мавпа – це ссавець, найбільш близька тварина за будовою до людини, відноситься до загону примати. Сучасна класифікація виділяє понад 400 видів мавп або вищих приматів. В основному вони живуть в Африці, Південній Америці. Деякі мавпочки живуть в зоопарках, виступають в цирках, а у когось це домашня тварина. Мавпочки, як і люди, спілкуються між собою. Спілкування мавп відбувається за допомогою міміки і звуків. Особливо гучними і балакучими вважаються капуцини.Опис мавп Представники загону приматів мають різну вагу і зріст."}],

)
print(response.choices[0].message.content)