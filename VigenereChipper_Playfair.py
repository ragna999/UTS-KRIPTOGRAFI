def generatePlayfairMatrix(key):
    key = key.replace(" ", "").upper()
    key = "".join(dict.fromkeys(key))  # Remove duplicate letters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i : i + 5] for i in range(0, 25, 5)]
    return playfair_matrix


def findChar(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)


def encrypt(plaintext, key):
    playfair_matrix = generatePlayfairMatrix(key)
    plaintext = plaintext.replace(" ", "").upper()
    encrypted = []

    if len(plaintext) % 2 != 0:
        plaintext += "X"

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]
        row1, col1 = findChar(playfair_matrix, char1)
        row2, col2 = findChar(playfair_matrix, char2)

        if row1 == row2:
            encrypted.append(playfair_matrix[row1][(col1 + 1) % 5])
            encrypted.append(playfair_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted.append(playfair_matrix[(row1 + 1) % 5][col1])
            encrypted.append(playfair_matrix[(row2 + 1) % 5][col2])
        else:
            encrypted.append(playfair_matrix[row1][col2])
            encrypted.append(playfair_matrix[row2][col1])

    return "".join(encrypted)


def decrypt(ciphertext, key):
    playfair_matrix = generatePlayfairMatrix(key)
    decrypted = []

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = findChar(playfair_matrix, char1)
        row2, col2 = findChar(playfair_matrix, char2)

        if row1 == row2:
            decrypted.append(playfair_matrix[row1][(col1 - 1) % 5])
            decrypted.append(playfair_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted.append(playfair_matrix[(row1 - 1) % 5][col1])
            decrypted.append(playfair_matrix[(row2 - 1) % 5][col2])
        else:
            decrypted.append(playfair_matrix[row1][col2])
            decrypted.append(playfair_matrix[row2][col1])

    return "".join(decrypted)


def main():
    key = input("Masukkan kunci: ").upper()
    plaintext = input("Masukkan teks plaintext: ")

    playfair_matrix = generatePlayfairMatrix(key)
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext:")
    print(plaintext)
    print("Encrypted:")
    print(encrypted)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    main()
