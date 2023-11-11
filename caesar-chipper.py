def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if 0 <= ord(char) <= 255:
            shifted_index = (ord(char) + shift) % 256

            result += chr(shifted_index)
        else:
            result += char

    return result


while True:
    print("Pilihah tindakan anda:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    choice = input("Masukkan pilihan anda (1/2/3): ")

    if choice == "1":
        text = input("Masukkan teks yang ingin Anda enkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (contoh: 3): "))
        encrypted_text = caesar_cipher(text, shift)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == "2":
        text = input("Masukkan teks yang ingin Anda dekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (contoh: 3): "))
        decrypted_text = caesar_cipher(text, -shift)
        print("Teks terdekripsi:", decrypted_text)
    elif choice == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
