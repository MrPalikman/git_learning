import traceback



# Это наш калькулятор
class Calculator:
    last_rez = None

    def sum(self, n1, n2):
        self.last_rez = n1 +n2
        return n1 + n2

    def min(self, n1, n2):
        self.last_rez = n1 - n2
        return n1 - n2

    def divide (self, n1, n2):
        try:
            res = n1 / n2
            self.last_rez = res
            return res
        except:
            traceback.print_exc()



    def myltiply(self, n1, n2):
        self.last_rez = n1 * n2
        return self.last_rez

    def print_last_rez(self):
        print(self.last_rez)