from functools import reduce
def main():

    #Filter - filtra si la condicion es True, caso contrario reduce el string
    myList = [1,4,5,7,9,13,19,21]

    odd = list(filter(lambda x: x % 2 != 0, myList))
    print(odd)

    #Map - actua sobre el string devolviendo uno del mismo largo
    myList2 = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, myList2))
    print(squares)

    #Reduce - toma los 2 primeros elementos y luego los sigue iterando
    myList3 = [2, 2, 2, 2, 2]
    
    allMultiplied = reduce(lambda a, b: a * b, myList3)
    print(allMultiplied)

if __name__ == '__main__':
    main()