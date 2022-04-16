# a Leap year is divisible by 4 but not by 100 unless it is also divible by 400

print("Leap year program\n")
def main():
    print("Insert leap year: ")
    x = int(input())
    print("You insereted ", + x)

    div = x % 4

    if (div == 0) and (x / 100) and (x / 400):
        print("is zero, is Leap Year\n")
    else:
        print("Not Leap Year\n")
main()
