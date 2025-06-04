import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
dic={"+": add,"-":subtract,"*":multiply,"/":divide}
def calculator():
    print(art.logo)
    more_calc=True
    num1 = float(input("Enter number:"))
    while more_calc:
        num2=float(input("enter another number: "))
        for symbol in dic:
            print(symbol)
        op_symbol=input("pick an operation")
        ans=dic[op_symbol](num1,num2)
        print(f"{num1} {op_symbol} {num2} = {ans}")
        more=input("type y to continue or  n to restart").lower()
        if more=="y":
            num1=ans
        else:
            more_calc=False
            print("\n"*25)

calculator()

