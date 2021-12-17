def run():
#    list_sqrt = [i**2 for i in range(1,101) if i%3!=0]
#    print (list_sqrt)

    lst = [i for i in range (1,100_000) if i%36==0]
#    print (lst)
    print (len(lst)) 

if __name__ == '__main__':
    run()