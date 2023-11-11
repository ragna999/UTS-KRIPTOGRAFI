def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plain_text, a, b):
    result = ""
    m = 26  # Jumlah huruf dalam alfabet

    for char in plain_text:
        if char.isalpha():
            if char.islower():
                result += chr((a * (ord(char) - ord('a')) + b) % m + ord('a'))
            else:
                result += chr((a * (ord(char) - ord('A')) + b) % m + ord('A'))
        else:
            result += char

    return result

def affine_decrypt(encrypted_text, a, b):
    result = ""
    m = 26  # Jumlah huruf dalam alfabet
    a_inv = mod_inverse(a, m)

    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                result += chr((a_inv * (ord(char) - ord('a') - b)) % m + ord('a'))
            else:
                result += chr((a_inv * (ord(char) - ord('A') - b)) % m + ord('A'))
        else:
            result += char

    return result

def main():
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    a = int(input("Masukkan nilai a (bilangan bulat relatif prima dengan 26): "))
    b = int(input("Masukkan nilai b (bilangan bulat): "))

    if gcd(a, 26) != 1:
        print("Error: a harus relatif prima dengan 26.")
        return

    encrypted_text = affine_encrypt(plain_text, a, b)
    print("Teks terenkripsi:", encrypted_text)

    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print("Teks terdekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
