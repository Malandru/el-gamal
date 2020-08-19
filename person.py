from keygen import Keygen
import random


class Person:
    def __init__(self, name):
        self.name = name
        keygen = Keygen()
        self.public_key = keygen.public_key
        self.private_key = keygen.private_key
        print(f"{name}'s keys generated.")

    def encrypt(self, msg, receptor_pk):
        p, g, y = receptor_pk  # Receiver public key
        k = random.randint(2, p)
        s = pow(y, k, p)  # Just one execution, belongs to c2 (y^k mod p)

        c1 = pow(g, k, p)  # en_msg argument -> C1 = g^k mod p
        c2 = [ord(char) * s for char in msg]  # encrypted msg -> C2 = PlainText * (y^k mod p)
        en_msg = ''.join(map(str, c2))
        print(f'{self.name} encrypted message: {c1}{en_msg}')
        return c1, c2

    def decrypt(self, en_msg):  # Plaintext = C2 × [C1 mod p] ^ (-x)
        x = self.private_key
        p, g, y = self.public_key
        c1, c2 = en_msg
        s = pow(c1, x, p)  # s = (C1 mod p) ^ x
        msg = ''.join([chr(int(value / s)) for value in c2])  # C2 * s^-1
        print(f'{self.name} decrypted message: {msg}')
        return msg
