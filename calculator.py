
class Calculator:
    last_rez = None

    def sum(self, n1, n2):
        self.last_rez = n1 +n2
        return n1 + n2

    def print_last_rez(self):
        print(self.last_rez)