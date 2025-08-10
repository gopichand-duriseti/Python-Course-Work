while True:
    print("Select a Program:")
    print("0.Exit")
    print("1. Reverse Every Word in a Sentence")
    print("2. Print Emoji Right Angle Triangle")
    print("3. Convert Decimal to Binary (without bin())")
    print("4. Number of Days Between Two Dates")
    print("5. Python Program to Find Largest element in an Array")
    print("6. Count the Number of Matching Characters in a Pair of Strings")
    print("7. Generate a Table of Squares")
    print("8. Check if Binary Representations of Two Numbers are Anagram")
    print("9. Sort a List of Tuples by Second Item")
    print("10. Printing Alphabet 'D' Star Pattern with Integer Input as Rows Length")
    print()
    ch= int(input("Enter your choice: "))
    if ch==0:
        break

    elif ch == 1:
        from my_programs_4 import reverse_wrd
        reverse_wrd()

    elif ch == 2:
        from my_programs_4 import emoji
        emoji()

    elif ch == 3:
        from my_programs_4 import dec_bin
        dec_bin()

    elif ch == 4:
        from my_programs_4 import date_diff
        date_diff()

    elif ch == 5:
        from my_programs_4 import large_ele
        large_ele()

    elif ch == 6:
        from my_programs_4 import count_matches
        count_matches()

    elif ch == 7:
        from my_programs_4 import sqrs
        sqrs()

    elif ch == 8:
        from my_programs_4 import bin_anagram
        bin_anagram()

    elif ch == 9:
        from my_programs_4 import sort_tuple
        sort_tuple()

    elif ch == 10:
        from my_programs_4 import pattern
        pattern()

    else:
        print("Invalid choice. Please select from 1–10.")


