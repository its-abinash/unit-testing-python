class demo_class:
    def GCD(self, a, b):
        return (a == 0) and b or self.GCD(b % a, a)