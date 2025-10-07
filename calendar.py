def leap(y): return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def days_in(m, y):
    return 29 if m == 2 and leap(y) else [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m-1]

def first_day(m, y):
    if m < 3: m += 12; y -= 1
    return ((1 + (13*(m+1))//5 + y%100 + (y%100)//4 + y//400 + (5*(y//100))) % 7 + 6) % 7

def show_month(m, y):
    names = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    print(f"\n   {names[m-1]} {y}\nSu Mo Tu We Th Fr Sa")
    f, d = first_day(m, y), days_in(m, y)
    print("   " * f, end="")
    for day in range(1, d+1):
        print(f"{day:2}", end=" ")
        if (f + day) % 7 == 0: print()
    print()

def show_year(y):
    print(f"\n===== CALENDAR {y} =====")
    for m in range(1, 13): show_month(m, y)
    print("========================\n")

while True:
    y = int(input("Enter year: "))
    show_year(y)
    if input("Another year? (yes/no): ").lower() != "yes":
        print("Goodbye 👋")
