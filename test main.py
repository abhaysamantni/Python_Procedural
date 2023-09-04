def main():
    print("Hello World (in main)")
    askAndPrintName()
    print("Back in main")

def askAndPrintName():
    name = input("What is your name?")
    print("Welcome ", name)

main()