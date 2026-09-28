# 1. Python Basics

## Data Types

A data type tells Python **what kind of value** something is.

| Type    | Meaning                    | Example              |
| ------- | -------------------------- | -------------------- |
| `int`   | Whole number               | `10`                 |
| `float` | Decimal number             | `3.14`               |
| `bool`  | True/False                 | `True`               |
| `str`   | Text                       | `"Hello"`            |
| `list`  | Collection, changeable     | `[1, 2, 3]`          |
| `tuple` | Collection, not changeable | `(1, 2, 3)`          |
| `set`   | Unique values              | `{1, 2, 3}`          |
| `dict`  | Key-value pairs            | `{"name": "Shaafi"}` |

### Data operations

**Create → Store → Read → Change → Remove**

### Custom Data Types

Created using classes.

```python
class SuperCar:
    pass
```

### Specialized Data Types

Extra data types provided by external libraries/modules.

### `None`

Means **no value / absence of value**.

```python
x = None
```

`None` ≠ `0`

### 3 Categories

* **Fundamental** → Built into Python
* **Custom** → Created using classes
* **Specialized** → From external modules/libraries

---

# 1.1 Integers and Floats

### `int`

Whole numbers:

```python
3, 4, 0, -2, 100
```

### `float`

Decimal numbers:

```python
0.5, 5.0001, 9.9
```

```python
5    # int
5.0  # float
```

Same numerical value, different data type.

## Operators

| Operator | Meaning        | Example  | Result |
| -------- | -------------- | -------- | ------ |
| `+`      | Add            | `2 + 4`  | `6`    |
| `-`      | Subtract       | `2 - 4`  | `-2`   |
| `*`      | Multiply       | `2 * 4`  | `8`    |
| `/`      | Divide         | `2 / 4`  | `0.5`  |
| `**`     | Power          | `2 ** 3` | `8`    |
| `//`     | Floor division | `5 // 4` | `1`    |
| `%`      | Remainder      | `5 % 4`  | `1`    |

### `type()`

Returns the data type.

```python
type(5)     # int
type(5.0)   # float
type(2 + 4) # int
```

### Important Rules

**`/` always returns a float:**

```python
10 / 2
# 5.0
```

**int + float → float:**

```python
20 + 1.1
# 21.1
```

### `//` Floor Division

Returns the floor result.

```python
5 // 4
# 1
```

### `%` Modulo

Returns the remainder.

```python
5 % 4
# 1
```

For `5 / 4`:

```text
// → 1  → full times it fits
%  → 1  → remainder
```

### Quick Cheat Sheet

```python
2 + 4      # 6
2 - 4      # -2
2 * 4      # 8
2 / 4      # 0.5
2 ** 3     # 8
5 // 4     # 1
5 % 4      # 1

type(5)    # int
type(5.0)  # float
```

### Memory Trick

```text
int    → whole number
float  → decimal
/      → division
//     → floor division
%      → remainder
**     → power
type() → data type
```

---

# 1.2 Math Functions

### Function

A function is a reusable **action/tool**.

Examples:

```python
print()
type()
```

### `round()`

Rounds a number.

```python
round(3.1)  # 3
round(3.9)  # 4
round(2.5)  # 2
round(3.5)  # 4
```

Python uses **banker's rounding** for `.5` cases.

### `abs()`

Returns the absolute value.

```python
abs(-20)  # 20
abs(20)   # 20
abs(-5.5) # 5.5
```

### Nested Functions

One function can be inside another.

```python
print(round(3.9))
```

Execution:

```text
round(3.9) → 4
print(4)   → 4

```

### Function Cheat Sheet

| Function  | Use             |
| --------- | --------------- |
| `print()` | Display output  |
| `type()`  | Check data type |
| `round()` | Round number    |
| `abs()`   | Absolute value  |

---

# 1.3 Operator Precedence

Operator precedence = **which operation Python performs first**.

### Order

1. `()` → Parentheses
2. `**` → Power
3. `*`, `/`, `//`, `%` → Multiplication/Division
4. `+`, `-` → Addition/Subtraction

### Memory Trick

**Brackets → Power → Multiply/Divide → Add/Subtract**

### Example

```python
20 + 3 * 4
```

First:

```python
3 * 4 = 12
```

Then:

```python
20 + 12 = 32
```

Result:

```python
32
```

### Another Example

```python
(20 - 3) + 2 ** 2
```

```text
(20 - 3) → 17
2 ** 2   → 4
17 + 4   → 21
```

Result:

```python
21
```

### Remember

Python follows a **fixed order of operations**. Use `()` when you want to control the order clearly.
