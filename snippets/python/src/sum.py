def sum(n: int) -> int:
  list = [1] * n
  index = 0
  total = 0
  for n in list:
    total += n * (index + 1)
    index += 1
  return total

print(sum(10))
print(sum(100))
print(sum(1))