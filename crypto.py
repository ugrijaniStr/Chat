import random
import requests

class Crypto():
    prefix_list = [
        "FS5ffEseptxmDmP1giC2CKIz0IH2juzzEpLhWokx",
        "Gzfv3byEZHsdIGybGwL5BrxT72mWWvXlN2Ga5G3c",
        "XJ2ePH6MEsedFkHNJlhQlVwKGgCYSszsZv2cjEGI",
        "DDYWZvq0m8VocPSDiTbjAySgiMczmtmBoRW0gcer",
        "cjs3QxADv8ogzvk8gubK4YNL88TUyT9wuewcjg7m",
        "kspYBmcVyltca74uxTVVwnmkcglfsaKPJXClq4Qn",
        "Xlblzej15ygMzUSIYX5R4ZIAJ9z4m2fmnQx0ZNq5",
        "bdowD6kEyYTfSNu2J5wVs6dIyVSFIfZ8Yp41PYLE",
        "dPiZr2tDoZOpyTsRk5NsfKotwcztVd9X4Y9esPif",
        "6o8Y2C7xsBgwGBjrUE25f9tjwPH1py43b4KaJhcU",
        "OrxoV76t6eDZqQSfSykn5TznGJj0Uuy8xTB13ASW",
        "gihvDPCox92u7IzK5I6HTCweTFFTwjRfoYvMeACW",
        "5WVAFQQdhGJDvFdmuaDyCKvBCsVmDcRIa0KEBqEK",
        "MIWcrZmo1ORf0iAxvqlm0IGHvHtjESZ52QYdtvm7",
        "RZa8jci02cNMWEZBxpWHZWbnyXuV45X0Dudxh5T5",
        "LNFeLh1h2EW2vC3ELP7LzwvyOVMWEvgviOfhkgro",
        "WcOgxNSOMDqCKp44bKexgW6ydTubygf5SIuSwWZB",
        "71MXRNSHIZWphLb2bJAzGscjJhJRkb4YvQCKMQmF",
        "EVkLQ8hrwpvd7OV1YVNVAD74tBVzf9R9XxDwbRVN",
        "6T7KHuoOhev2bpo6hJYDjTn2KMwPbihY4GenGQpZ",
    ]

    sufix_list = [
        "PU#X1Z<(5kW^i}ARA3Kd!|IVx5;I4Fr<?v3ej.0&",
        "M_%%hMj}9JPwq\\Yc.,xaa*/Mm|_61F6;bsYnAG=<",
        "L6?iv\\&2yX^4a[nq&L@>8Ou,zQh!;i0d@{`+I|`*",
        ",)4Hh_=hyn'({gPE8fYq2r->&?petlc:C>Ie%!%a",
        "^rmgU(C%:th@:wzWe#7CLK`4O#iWah~$m(W(VU`&",
        "mk=#QvnO^5hLCXOZ7[OQC-r-L=mz`7}N7<e2e7r'",
        ":|@TTp}L@>?[8O:a(&PTG7|1[1g!)`{AjV82K^6Y",
        "He-hSfaf?9@5cf~cF;YGb~4Ngk%Nr1.(G3P{DSnB",
        ".[I}$8![4B4p}q{Ffi&iZ;y_,xZ)ZZ:+!eYN),wX",
        "@Ysa7_D7iMwl}fAw>l1o[a;gQc)hnB6[gLGve6Y{",
        "}$mH,p4]k~f%{~R_P;i2R0LzQ<7)jRuvFTk]k}@_",
        "$V}4w56pP-nruxdQ?g=cmiKLjM5,BPMlc.4c>]e4",
        "JJ2}T)9*<El=H/q'<%`b?S[]U;/A^.4Ur{-WVu'H",
        "V!dTl1;T<QA*:md#vF|4'R#l1t^]iUa-<9cOnvVO",
        "x]>y)fG4>NkPwIf.z*i9b'l&lnG8{ebLxphuET:k",
        "3HgP_2Q)Xk'*g65dT^`tIjvf,7+fmx}!:sKjzSLH",
        "7k-0+qja+<=Rbn@_LvOXt$G2i7hYk+fRm;7=r_J|",
        ":f!in*S#S.KVYUS+8}z%E2@n@<mH'e(uf+I2L9d_",
        "N[s=c8\\ZSvLMqzhcEp,iws.PC]k>)6X2E'bUr6Wx",
        "=yE9Nr(F2)#24Gtxw2V=0^j(Glf3&J?T_hrHt,>j",
    ]

    crypto_word_list = [
        'A', '154', 'g', '371', 'S', 'l', 'u', '520', '655', '286',
        'v', '515', 'L', '92', '876', 'p', 'Q', 'R', 'q', 'c',
        'U', 'e', 'o', 'z', 'Z', 'n', '_'
    ]

    @staticmethod
    def encode_message_to_crypto_word(message):
        result = ""
        for char in message:
            if char == " ":
                result += "_"
            elif char.isalpha():
                index = ord(char.lower()) - ord('a')
                if 0 <= index < 26:
                    result += Crypto.crypto_word_list[index]
        return result

    @staticmethod
    def crypto_sys(prefix_message, sufix_message, message):
        encoded = Crypto.encode_message_to_crypto_word(message)
        return prefix_message + encoded + sufix_message


class Decrypto():
    @staticmethod
    def decrypto_sys(crypto_message):
        prefix_ = crypto_message[:40]
        sufix_ = crypto_message[-40:]

        if (prefix_ in Crypto.prefix_list) and (sufix_ in Crypto.sufix_list):
            msg = crypto_message[40:-40]
            decrypted = Decrypto.decode_crypto_to_message(msg)
            print(decrypted)
        else:
            print("Invalid crypto message")

    @staticmethod
    def decode_crypto_to_message(crypto_word_message):
        result = ""
        i = 0
        crypto_map = {word: chr(97 + idx) for idx, word in enumerate(Crypto.crypto_word_list[:-1])}
        crypto_map["_"] = " "

        while i < len(crypto_word_message):
            matched = False
            for word in sorted(Crypto.crypto_word_list, key=lambda x: -len(x)):
                if crypto_word_message[i:i+len(word)] == word:
                    result += crypto_map[word]
                    i += len(word)
                    matched = True
                    break
            if not matched:
                i += 1
        return result


class Main():
    @staticmethod
    def main():
        print("1. Crypto")
        print("2. Decrypto\n")
        choice = input("Number: ")

        if choice == "1":
            Main.main_crypto()
        elif choice == "2":
            Main.main_decrypto()
        else:
            print("Invalid option.")

    @staticmethod
    def main_crypto():
        prefix = random.choice(Crypto.prefix_list)
        sufix = random.choice(Crypto.sufix_list)

        url = "http://141.227.140.54:9583/send"

        while True:
            message = str(input("Enter message: "))
            if(message == "!break"):
                print("End...")
                break
            else:
                crypted = Crypto.crypto_sys(prefix, sufix, message)
                requests.post(f'{url}', json = {'message': f'{crypted}'})

    @staticmethod
    def main_decrypto():
        encrypted_message = input("Decrypto: ")
        Decrypto.decrypto_sys(encrypted_message)


if __name__ == "__main__":
    Main.main()