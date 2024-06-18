menu = {
    "Espreso" : {
        "Water" : 50,
        "Coffe" : 18,
    },
    "cost" : 40,

    "Latte" : {
        "Water" : 200,
        "Coffe" : 24,
        "Milk" : 150,
    },
    "cost" : 60,
    "Cappuccino" :{
        "Water" : 250,
        "Coffe" : 24,
        "Milk" : 100
    },
    "Cost" : 80

}
profit = 0
resources = {
    "Water" : 300,
    "Milk"  : 200,
    "Coffe" : 100,
}
def is_resource_ready(order_ingridients):
    """To check if we have resources"""
    for item in order_ingridients:
        if order_ingridients> resources[item]:
            print(f"We are out off {item}")
            return False
    return True
machine_on = True
while machine_on:
    choice = input("Select your bevrage(Espreso/Latte/Cappuccino) : ").capitalize()
    if choice == 'Off': machine_on = False
    elif choice == 'Report' :
        print(f"Water : {resources['Water']} ml")
        print(f"Milk : {resources['Milk']} ml")
        print(f"Coffe : {resources['Coffe']} g")
        print(f"Money : {profit}")
    else :
        drink = menu[choice]
        print(drink)
        if is_resource_ready(drink["ingridients"]):
            pass

        
        
