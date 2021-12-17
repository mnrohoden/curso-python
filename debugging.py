def divisors(num):
    divisors = [i for i in range(1,num+1) if num % i == 0]
    return divisors


def run():
    try:
        num = int(input('Ingresa un numero: '))
        if num < 1:
            raise Exception('Debes ingresar un numero mayor a 0 (cero)')
        print(divisors(num))
        print('Termino mi programa')
    except ValueError:
        print("Debes ingresar un numero oe")
    except Exception as inst:
        print(inst)


if __name__ == '__main__':
    run()