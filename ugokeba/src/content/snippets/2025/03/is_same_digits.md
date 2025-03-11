---
pubDate: 2025-03-12
title: 3桁の数がゾロ目かどうか判定する
slug: 2025-03-12-is-same-digits
---

## Instructions
3桁の数値を引数として取り、その数値がゾロ目かどうかを判定する関数を作成すること。

## Implementation
```python: is_same_digits.py
def is_same_digits(n: int) -> bool:
  return (n / 37) % 3 == 0 and n % 37 == 0

print(is_same_digits(111))
```

## How to Run
```bash
$ python sum.py
```

## Test Cases
```python
print(is_same_digits(111)) # True
print(is_same_digits(148)) # False
print(is_same_digits(185)) # False
print(is_same_digits(222)) # True
print(is_same_digits(999)) # True
```

## Notes
なし

## Environments
Python 3.13.2