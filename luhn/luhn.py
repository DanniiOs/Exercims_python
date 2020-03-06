class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        lis = []
        suma = 0
        divisibe = 10
        for i in range(0, len(self.card_num)):
            if lis == self.card_num:
                if lis[i] != 0:
                    lis[i+1] = 2*lis[i]
                    suma += lis[i]
                    divisibe /= suma
                    return True
                else:
                    return False
