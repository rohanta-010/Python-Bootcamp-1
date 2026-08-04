# Number Conversion & Rounding in Python

## 1. int() - Remove Decimal (Truncate) : Default Conversion

# - Removes the decimal part.
# - Truncates **towards 0**.
# - Does NOT round.

print("int() - Remove Decimal (Truncate) : Default Conversion")
print(int(3.99))     # 3
print(int(3.14))     # 3
print(int(-3.99))    # -3


## 2. math.floor() - Round Down

# - Always rounds down to the nearest smaller integer.
# - Requires `import math`.

import math
print("\nmath.floor() - Round Down")
print(math.floor(3.99))    # 3
print(math.floor(3.14))    # 3
print(math.floor(-3.14))   # -4


## 3. math.ceil() - Round Up

# - Always rounds up to the nearest larger integer.
# - Requires `import math`.

import math
print("\nmath.ceil() - Round Up")
print(math.ceil(3.14))     # 4
print(math.ceil(3.99))     # 4
print(math.ceil(-3.14))    # -3


## 4. round() - Nearest Integer

# - Rounds to the nearest integer.
# - Python uses **Banker's Rounding** for `.5` values (round half to even).

print("\nround() - Nearest Integer")
print(round(3.2))    # 3
print(round(3.8))    # 4 
print(round(2.5))    # 2 (rounds to nearest even)
print(round(3.5))    # 4 (rounds to nearest even)


# Round to decimal places:

# round(x) → integer
# round(x, 0) → float with .0

# General Rule
# Suppose you want to keep N decimal places:

# Keep the first N digits after the decimal.
# Look at the (N+1)th digit.
# If it is:
# 0–4 → Leave the last kept digit unchanged.
# 5–9 → Increase the last kept digit by 1.

print("\nround() - Round to Decimal Places")
print(round(3.14159, 0))   # 3.0
print(round(3.14159, 2))   # 3.14 (1<5, so 4 remains unchanged)
print(round(3.14159, 3))   # 3.142 (5≥5, so 1 becomes 2)


## 5. math.trunc() - Truncate

# - Removes the decimal part.
# - Requires `import math`.
# - Same behavior as `int()` for floats.

import math
print("\nmath.trunc() - Truncate")
print(math.trunc(3.99))    # 3
print(math.trunc(-3.99))   # -3


## Quick Comparison

# | Function | 3.14 | 3.99 | -3.14 |           Rule             |
# |----------|------|------|-------|----------------------------|
# | int()    | 3    | 3    | -3    | Remove decimal (towards 0) |
# | floor()  | 3    | 3    | -4    | Always down                |
# | ceil()   | 4    | 4    | -3    | Always up                  |
# | round()  | 3    | 4    | -3    | Nearest integer            |
# | trunc()  | 3    | 3    | -3    | Remove decimal (towards 0) |



## Remember

# - **int()** → Just remove decimal.
# - **floor()** → Go to the smaller integer.
# - **ceil()** → Go to the larger integer.
# - **round()** → Go to the nearest integer.
# - **trunc()** → Same as `int()` for float values.

### Easy Memory Trick

# int()   → Ignore decimal
# floor() → Go Down ⬇️
# ceil()  → Go Up ⬆️
# round() → Go Nearest 🎯
# trunc() → Cut decimal ✂️
