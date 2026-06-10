def validacija(funkcija):
    def wrapper(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return "Greska: argumenti moraju biti brojevi"

        if a < 1 or a > 100 or b < 1 or b > 100:
            return "Greska: brojevi moraju biti od 1 do 100"

        return funkcija(a, b)

    return wrapper


@validacija
def saberi(a, b):
    return a + b


print(saberi(10, 20))
print(saberi(150, 20))