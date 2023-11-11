import numpy as np

def prepare_input(text):
    matrix = []
    for char in text:
        if char.isalpha():
            matrix.append(ord(char) - ord('A') if char.isupper() else ord(char) - ord('a'))

    return np.array(matrix)

def hill_encrypt(plain_text, key_matrix):
    key_size = len(key_matrix)
    plain_matrix = prepare_input(plain_text)

    # Menambahkan padding dengan nilai 0 jika diperlukan
    while len(plain_matrix) % key_size != 0:
        plain_matrix = np.append(plain_matrix, [0])

    # Mengubah matriks teks menjadi matriks terenkripsi menggunakan kunci
    encrypted_matrix = np.dot(plain_matrix.reshape(-1, key_size), key_matrix) % 26

    # Mengembalikan teks terenkripsi
    return ''.join([chr(x % 26 + ord('A')) for x in encrypted_matrix.flatten()])

def main():
    plain_text = input("Masukkan teks yang akan dienkripsi: ")

    # Memasukkan kunci enkripsi sebagai matriks 3x3
    key_text = input("Masukkan kunci enkripsi (sebagai matriks 3x3, contoh: '2 4 7 9 6 15 1 8 12'): ")
    key_values = [int(x) for x in key_text.split()]

    # Validasi kunci
    if len(key_values) != 9:
        print("Error: Kunci harus berisi 9 nilai untuk matriks 3x3.")
        return

    key_matrix = np.array(key_values).reshape(3, 3)

    encrypted_text = hill_encrypt(plain_text, key_matrix)
    print("Teks terenkripsi:", encrypted_text)

if __name__ == "__main__":
    main()
