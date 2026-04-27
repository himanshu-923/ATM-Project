from utils import statement


def show_statement():
    print("\nMini Statement")
    print("\nAccount holder: Himanshu kumar")
    print("\nAccount Number: 0000 XXXX 0000")
    if len(statement) == 0:
        print("No transaction found")
    else:
        for item in statement:
            print(item)
