class FibUtil:
    @classmethod
    def fibs(cls):
        print("fibs called")
        a, b = 1, 1
        yield a
        yield b
        while True:
            print("while true in fibs")
            a, b = b, a + b
            yield b