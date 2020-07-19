print('python program that tells a user their Birth date based on their last birthday and how old they are')

# import date class from the datetime module.
from datetime import date

# Get current year 
current_year = date.today().year

# Get birth_year of user
birth_year = int(input('Which year were you born? '))

# Get last_birthday_month of user
last_birthday_month = int(input('Enter your last birthday month: '))

# Get last_birthday_day of user
last_birthday_day = int(input('On which day of your birthday month did you celebrate your birthday? '))

# Calculate current_age of user
current_age = current_year - birth_year

print(f"You were born on {last_birthday_day}/{last_birthday_month}/{birth_year} and you're {current_age} years old")

