import chardet

class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        print(self.key)
        print(self.alphabet)

    def encode(self, text):
        print(text)
        print(len(text))
        print(type(text))
        str = ""
        long_key = self.key * (len(text) // len(self.key)) + self.key[:len(text) % len(self.key)]
        for i in range(len(text)):
            print(text[i])
            if text[i] not in self.alphabet:
                str += text[i]
            else:
                index_t = self.alphabet.find(text[i])
                index_k = self.alphabet.find(long_key[i])
                str += self.alphabet[(index_k + index_t) % len(self.alphabet)]
        return str

    def decode(self, text):
        print(text)
        str = ""
        long_key = self.key * (len(text) // len(self.key)) + self.key[:len(text) % len(self.key)]
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                str += text[i]
            else:
                index_t = self.alphabet.find(text[i])
                index_k = self.alphabet.find(long_key[i])
                str += self.alphabet[(index_t - index_k) % len(self.alphabet)]
        return str

if __name__ == "__main__":
    abc = "アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー"
    key = "カタカナ"
    c = VigenereCipher(key, abc)
    print(c.encode('カタカナ'))
    print(c.decode("タモタワ"))