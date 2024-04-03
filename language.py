
def main():
    question = str(input("What language do you want to play in?(English, Russian): "))

    if question == "English":
        import main_english
    elif question == "Russian":
        import main
    else:
        print("Invalid")
        exit()
main()