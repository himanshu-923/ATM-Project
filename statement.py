from utils import statement


def show_statement():
    print("\nMini Statement")
    print("\nAccount holder: Himanshu kumar")
    print("Account Number: 0000 XXXX 0000")
    if len(statement) == 0:
        print("\nNo transaction found")
    else:
        for item in statement:
            print("\n", item)
