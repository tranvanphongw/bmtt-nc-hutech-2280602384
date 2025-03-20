import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_cols = key
        num_rows = math.ceil(len(text) / key)
        num_full_cols = len(text) % key  

        decrypted_text = [''] * num_rows
        row, col = 0, 0  

        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            
            if row == num_rows or (row == num_rows - 1 and col >= num_full_cols):
                row = 0
                col += 1

        return ''.join(decrypted_text)
