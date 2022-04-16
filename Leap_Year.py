# a Leap year is divisible by 4 but not by 100 unless it is also divible by 400

print("Leap year program\n")
def main():
    print("Insert leap year: ")
    x = int(input())
    print("You insereted ", + x)

    div = x % 4

    if (div % 4 == 0) and (div % 100 == 0) or (div % 400 == 0):
        print("Yes, is Leap Year\n")
    else:
        print("No, not leap year\n")
main()
