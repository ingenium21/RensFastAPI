firstname = input("please input your first name: ")
days = input("please input how many days until your birthday")

weeks = round(int(days)/7)
remaining_days = (int(days) % 7)

print(f"Hi, {firstname}, there are {weeks} weeks and {remaining_days} days left until your birthday")