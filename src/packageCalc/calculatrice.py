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
    
    def soustraction(self, a, b):
        res = a
        if b >= 0:
            while (b - 1) >= 0:
                b -= 1
                res -= 1
        elif b < 0:
            while (b + 1) <= 0:
                b += 1
                res += 1
        return res

    def multiplication(self, a, b):
        if b == 0 or a == 0:
            res = 0
        elif b < 0 and a < 0:
            res = abs(a)
            while (b + 1) < 0:
                b += 1
                res = abs(self.soustraction(a,res))
        elif b < 0 and a > 0:
            res = -a
            while (b + 1) < 0:
                b += 1
                res = self.soustraction(a,res)
        elif b > 0 and a < 0:
            res = -a
            while (b - 1) > 0:
                b -= 1
                res = self.soustraction(a,res)
        else:
            res = a
            while (b - 1) > 0:
                b -= 1
                res = self.addition(res,a)
        return res
