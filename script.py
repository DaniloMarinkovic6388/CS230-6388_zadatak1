def multiply_a_b_(a, b):
    return a * b


def povrsina_pravougaonika(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Stranice moraju biti pozitivni brojevi.")
    return multiply_a_b_(a, b)


try:
    a = float(input("Unesite stranicu a: "))
    b = float(input("Unesite stranicu b: "))

    rezultat = povrsina_pravougaonika(a, b)
    print("Povrsina pravougaonika je:", rezultat)

except ValueError as greska:
    print("Greska:", greska)