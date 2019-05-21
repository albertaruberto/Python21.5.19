def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age


current_year = 2049
birth_year = 1993
calculate_age = current_year - birth_year

my_age = calculate_age


current_year = 2049
birth_year = 1953
calculate_age = current_year - birth_year

dads_age = calculate_age

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old ")