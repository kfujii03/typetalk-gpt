# import openai
import settings as env

# openai.api_key = env.OPENAI_API_KEY

# def get_chatgpt_response(msg='こんにちは'):
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = [
#             { "role": "system", "content" : "あなたは、日本語から英語に翻訳してくれる優秀なアシスタントです。" },
#             { "role": "user", "content" : msg },
#         ]
#     )
#     return response["choices"][0]["message"]["content"]

def get_test():
    return 'こんにちは'