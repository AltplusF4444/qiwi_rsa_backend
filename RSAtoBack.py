import random


class Rsa:
    N = 0
    closedExponent = 0
    openedExponent = 0

    def CreateKeys(self, minNum, maxNum):
        firstPrimirive = self.CreatePrimeNumber(minNum, maxNum)
        secondPrimirive = self.CreatePrimeNumber(minNum, maxNum)
        self.N = firstPrimirive * secondPrimirive
        phi = (firstPrimirive - 1) * (secondPrimirive - 1)
        self.closedExponent = self.CreateCoprime(phi)
        self.openedExponent = self.CreateReciprocal(phi, self.closedExponent)

    def CreatePrimeNumber(self, minNum, maxNum):
        num = random.randint(minNum, maxNum)
        all_numbers = []

        for i in range(0, num + 1):
            all_numbers.append(i)

        all_numbers[1] = 0

        for i in range(2, num + 1):
            j = 2 * i
            while j <= num:
                all_numbers[j] = 0
                j += i

        return max(all_numbers)

    def CreateCoprime(self, phi):
        a = 0
        b = 0
        i = phi - 2
        while a != 1:
            a = i
            b = phi
            while b != 0:
                a %= b
                c = a
                a = b
                b = c
            if a == 1:
                return i
            i -= 1
        return 0

    def CreateReciprocal(self, phi, closedExponent):
        for i in range(1, phi-1):
            if ((closedExponent * i) % phi) == 1:
                return i
        return 0

    def Encryption(self, messeg, openedExponent, N):
        encryptedMesseg = ""

        for i in range (0, len(messeg)):
            num = self.FuncMod(ord(messeg[i]), openedExponent, N)
            encryptedMesseg += str(num) + 'O'
        encryptedMesseg = encryptedMesseg[:-1]

        return encryptedMesseg

    def Decryption(self, encryptedMesseg, closedExponent, N):
        promString = ""
        decryptedMesseg = ""

        numList = []

        encryptedMesseg += 'O'

        for i in range (0, len(encryptedMesseg)):
            if(encryptedMesseg[i] == 'O'):
                numList.append(int(promString))
                promString = ""
            else:
                promString += encryptedMesseg[i]

        for i in range (0, len(numList)):
            decryptedMesseg += chr(self.FuncMod(numList[i], closedExponent, N))

        return decryptedMesseg

    def FuncMod(self, x, y, z):
        rezult = 1
        for i in range(0, y):
            rezult = (x * rezult) % z
        return rezult

def ShRSA(mess):
    keys = Rsa()
    user = Rsa()
    seller = Rsa()

    keys.CreateKeys(2024, 4048)

    s = user.Encryption(mess, keys.openedExponent, keys.N)

    print(s)
    print("\n")

    s = seller.Decryption(s, keys.closedExponent, keys.N)

    print(s)



ShRSA("8y982-bhsdf3347-hu234")










