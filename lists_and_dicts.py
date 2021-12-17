def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname":"Facundo","lastname":"Garcia"}

    super_list = [
        {"firstname":"Facu","lastname":"Garcia"},
        {"firstname":"Max","lastname":"Rohoden"},
        {"firstname":"Pepe","lastname":"Torres"},
        {"firstname":"Jose","lastname":"Garcia"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

    for i in super_list:
        print(i["firstname"],i['lastname'])


if __name__ == '__main__':
    run()