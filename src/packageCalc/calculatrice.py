class Calculatrice():

    def addition(self, a, b):
        res = a
        if b >= 0:
            while ( b - 1) >= 0:
                b -= 1
                res += 1
        elif b < 0:
            while ( b + 1) <= 0:
                b += 1
                res -= 1
        return res
