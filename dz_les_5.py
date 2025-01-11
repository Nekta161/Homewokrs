text = input("Введите текст: ")

while True:
    shift_input = input("Введите сдвиг (может быть отрицательным): ")
    if shift_input.lstrip('-').isdigit(): 
        shift = int(shift_input)
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

encrypted_text = ""
for char in text:
    if char == ' ':
        encrypted_text += char
    else:
        char_code = ord(char)
        new_char_code = char_code + shift
        new_char = chr(new_char_code)
        encrypted_text += new_char

print(f"Зашифрованный текст: {encrypted_text}")

while True:
    decrypt_input = input("Хотите дешифровать текст? (да/нет): ").lower()
    if decrypt_input in ['да', 'нет']:
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")

if decrypt_input == 'да':
    decrypted_text = ""
    for char in encrypted_text:
        if char == ' ':
            decrypted_text += char
        else:
            char_code = ord(char)
            new_char_code = char_code - shift
            new_char = chr(new_char_code)
            decrypted_text += new_char

    print(f"Дешифрованный текст: {decrypted_text}")
else:
    print("Программа завершена.")
