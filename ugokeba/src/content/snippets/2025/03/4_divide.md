---
pubDate: 2025-03-13
title: 割り切れるかどうか
index: 4
slug: 4-divide
---

## Instructions
割り切れるかどうかを返します。

## Implementation
```python: divide.py
def divide(numerator: int, denominator: int) -> boolean:
  if numerator >= denominator:
    divide(numerator, numerator - denominator)
  return numerator == 0
```

## How to Run
```bash
$ python divide.py
```

## Test Cases
```python
```

## Notes
なし

## Environments
Python 3.13.2