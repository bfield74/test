# choices for problem solving

print("Practice to visualize problem (V)")
print("Practice working on Graphs for this problem (G)")
print("Practice calculations for this problem (C)")
print("Look for motivation for problem solving (M)")
print(" >>> ")
choice = input()
print(choice)

if choice == 'c' or 'C':
    print("going to calculations")
elif choice == 'v' or 'V':
    print("going to visualization")
elif choice == 'G' or 'g':
    print("going to graphing")
elif choice == 'M' or 'm':
    print("going to motivation")
else:
    print("invalid choice")


