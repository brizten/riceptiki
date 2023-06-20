import easyocr 

def tex_recognition(file_path, text_file_name = 'resulst.txt'):
    reader = easyocr.Reader(['en', 'ru'])
    result = reader.readtext(file_path, detail= 0, paragraph = True)

    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f'{line}\n\n')

    return f'result wrote into {text_file_name}'

def main():
    file_path = input('Enter file path: ')
    result = tex_recognition(file_path)
    print(result)

if __name__ == '__main__':
    main()
