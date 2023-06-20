import os
import easyocr
import openai

def tex_recognition(file_path, text_file_name='results.txt'):
    reader = easyocr.Reader(['en', 'ru'])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    return result

def generate_recipes(prompt):
    openai.api_key = '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'
    model_engine = 'text-davinci-003'

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    generated_recipe = completion.choices[0].text.strip()
    return generated_recipe

def main():
    file_path = input('Enter file path: ')

    if not os.path.exists(file_path):
        print("Invalid file path. Please provide a valid file path.")
        return

    try:
        ocr_result = tex_recognition(file_path)
        prompt = 'дай несколько рецептов из того что есть в чеке ' + str(ocr_result)
        generated_recipe = generate_recipes(prompt)
        print(generated_recipe)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    main()
