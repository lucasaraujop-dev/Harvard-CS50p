def einstein(mass):
    Energy = ((int(mass))*(300000000**2))
    return Energy

def main():
    mass = input("m: ")
    Result = einstein(mass)
    print(Result)

main()
