from openai import OpenAI

client = OpenAI(api_key='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')
we = []
for i in range(3):
    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    we.append(response.data[0].url)
    print(we)
# #
# # import re

# # text = "1.Ваш исходный текст 2. weqwe"
# #
# # # Используем регулярное выражение для разделения текста по номерам с последующим текстом
# # text_parts = re.findall(r'(\d+\.\s*.+?)(?=\s*\d+\.\s*|$)', text)
# #
# # print(text_parts)
# text = '''Пост 1:
# Тема: "5 простых упражнений для укрепления мышц спины"
# 1. Планка: удерживайте позу как можно дольше, активируя мышцы спины и корсета.
# 2. Вертикальная тяга: подтягивайтесь к горизонтальной перекладине, работая среднюю часть спины.
# 3. Гиперэкстензия: лёжа на животе, поднимайте корпус, напрягая мышцы спины.
# 4. Разведение рук в стороны: стойте прямо, разведите руки в стороны, удерживая некоторое время.
# 5. Вращения гантелей: с гантелями в руках, делайте вращения, укрепляя мышцы спины и плеч.
#
# Пост 2:
# Тема: "Польза бега для здоровья"
# 1. Улучшает сердечно-сосудистую систему.
# 2. Снижает риск развития болезней сердца и сосудов.
# 3. Стимулирует процессы обмена веществ и способствует сжиганию жира.
# 4. Улучшает настроение и помогает бороться со стрессом.
# 5. Повышает выносливость и укрепляет мышцы ног.'''
#
# posts_list = []
#
# # print(text.split('\n\n'))
# for post in text.split('\n\n'):
#     # Найти номер и текст поста
#     for j in range(1, 3):
#         post_parts = post.split(f"Пост {j}")
#         if len(post_parts) == 2:  # Проверяем, что удалось разделить на две части
#             post_number, post_text = post_parts
#             posts_list.append((post_number.strip(), post_text.strip()))
#
#
# for i in posts_list:
#     print(i)
b = {}
for i in range(1, 10):
    b['2'] = [i for i in range(10)]
print(b)
