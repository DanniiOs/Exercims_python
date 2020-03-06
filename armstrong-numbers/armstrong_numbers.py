def is_armstrong_number(number):
    acumulador = 0

    while number >= 0:
        tem = str(number)
        cantidad = len(tem)
        for i in tem:
            acumulador += int(i) ** cantidad
        if acumulador == number:
            return True
        else:
            return False
