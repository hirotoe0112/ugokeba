---
pubDate: 2025-03-11
title: 1から指定した数までの合計を計算する
index: 1
slug: 1-sum
---

## Instructions
1から指定した数までを合計する関数を作成すること。

## Implementation
```python: sum.py
def sum(n: int) -> int:
  list = [1] * n
  index = 0
  total = 0
  for n in list:
    total += n * (index + 1)
    index += 1
  return total
```

## How to Run
```bash
$ python sum.py
```

## Test Cases
```python
print(sum(10)) # 55
print(sum(100)) # 5050
print(sum(1)) # 1
```

## Notes
なし

## Environments
Python 3.13.2