def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord("a")
            else:
                start = ord("A")
            shifted = ord(char) - start
            encrypted = (shifted + shift_amount) % 26 + start
            encrypted_text += chr(encrypted)
        else:
            encrypted_text += char
    return encrypted_text


def main():
    full_name = "Cyrial Kouatchoua Kamda"
    birthday = "03302001"
    shift_key = 1

    for digit in birthday:
        if digit != "0" and digit.isdigit():
            shift_key *= int(digit)
            shift_key += int(digit)
    print(shift_key)

    encrypted_name = caesar_encrypt(full_name, shift_key)
    print("Encrypted name:", encrypted_name)


if __name__ == "__main__":
    main()
