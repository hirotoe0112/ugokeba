def is_same_digits(n: int) -> bool:
  return (n / 37) % 3 == 0 and n % 37 == 0

print(is_same_digits(111))
print(is_same_digits(148))
print(is_same_digits(185))
print(is_same_digits(222))
print(is_same_digits(999))