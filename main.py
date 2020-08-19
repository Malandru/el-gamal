from person import Person

if __name__ == '__main__':
    bob = Person('Bob')
    alice = Person('Alice')
    msg = input("Bob's message: ")
    en_msg = bob.encrypt(msg, alice.public_key)
    alice.decrypt(en_msg)
