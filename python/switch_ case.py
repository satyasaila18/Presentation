marks=int(input("Enter Marks.."))
match marks:
    case m if marks>=91:
        print("A+")
    case m if marks>=81:
        print("A")
    case m if marks>=71:
        print("B")
    case m if marks>=61:
        print("C")
    case m if marks>=51:
        print("D")
    case m if marks>=41:
        print("E")
    case _:
        print("Fail")

