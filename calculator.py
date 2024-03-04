import traceback


class Calculator:
    last_rez = None

    def sum(self, n1, n2):
        self.last_rez = n1 +n2
        return n1 + n2

    def divide (self, n1, n2):
        try:
            res = n1 / n2
            self.last_rez = res
            return res
        except:
            traceback.print_exc()

    def print_last_rez(self):
        print(self.last_rez)