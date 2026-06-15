def repeat_message():
    message = input("Enter your message that you want to repeat: \n> ")
    add_newline = message + "\n"
    repeat_time = int(input("Enter the repeat time you want to repeat: \n> "))
    repeat_msg = add_newline * repeat_time
    print(repeat_msg)

continue_working = True
while continue_working:
    def my_main():
        global continue_working
        repeat_message()
        choice = input("Do you want to continue (yes/no) | (y/n) \n> ").lower()
        if choice == "yes" or choice == "y":
            print("\n" * 20)
            repeat_message()
        elif choice == "no" or choice == "n":
            print("\nThank you for using my program. ")
            print("Written by Morn Chanthoung. \n")
            continue_working = False
        else:
            print("Your are enter the wrong output!")
            my_main()
    my_main()

            