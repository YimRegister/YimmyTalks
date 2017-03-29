def main():
    print("I am the Mathemagician! I can magically guess any number inside of your head. Just think of a number between 0 and 100, and revel in my psychic abilities! Though I do require some audience participation. After each guess, indicate whether I am too high (H), too low (L), or correct (C).")
    low, high, guess_status = (0, 100, False)
    while guess_status ==False:
        guess=(high + low)//2
        answer = input("My guess is " + (str(guess)) + ". Is this too high (H), too low (L), or correct (C)?")
        if answer== (str("H")):high = guess
        elif answer== (str("L")): low = guess
        elif answer== (str("C")): guess_status= True
        elif answer != (str("H"))+ (str("L")) + (str("C")): print("Don't mess around with me, mortal. Answer with (H), (L), or (C).")
    print("You may now feel free to admire my magical powers. Have an extraordinary day!")
main()
