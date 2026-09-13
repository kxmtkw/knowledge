# Number Systems

`A number system is a mathematical framework for representing numbers using a set of symbols (digits) where each digit's value depends on its position relative to the base.`

- Binary (2) [0, 1]
- Decimal (10) [0 - 9]
- Octal (8) [0 - 7]
- Hexadecimal (16) [0 - 9, A - F]

## Conversions between Number Systems

### `From Decimal`

##### To Binary
By Long Division with divider as 2

##### To Octal
By Long Division with divider as 8

##### To Hexadecimal
By Long Division with divider as 16.

### `From Binary`

##### To Decimal
Compute the decimal number by iterating over the binary digits from the right.
```python
binary = "1110"
decimal = (1 * 0) + (2 * 1) + (4 * 1) + (8 * 1)

digits = list(reversed(binary))
decimal = sum([(2 ** i) * int(digits[i]) for i in range(len(digits))])
```

##### To Octal
Divide the binary number into sets of 3 digits and convert each group to decimal and place them together.
- 3 binary digits can hold 8 values.

##### To Hexadecimal
Divide the binary number into sets of 4 digits and convert each group to decimal and place them together. Map 10-15 to A-F.
- 4 binary digits can hold 16 values.

### `From Octal`

##### To Binary
Write the binary representation of each octal digit and simply write them together.

##### To Decimal
Same as Binary to Decimal. Compute value of each digit and add but this time each digit is multiplied by $8^n$.

##### To Hexadecimal
Too complicated to do manually, use binary as proxy.

### `From Hexadecimal`

##### To Binary
Write the binary representation of each hexadecimal digit and simply write them together.

##### To Octal
Use binary as proxy.

##### To Decimal
Same as Binary to Decimal. Compute value of each digit and add but this time each digit is multiplied by $16^n$.


## Conversion Matrix

| From \ To       | **Decimal**                                                       | **Binary**                                                       | **Octal**                                                                       | **Hexadecimal**                                                                    |
| --------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Decimal**     | —                                                                 | Successive division by 2; collect remainders in reverse order.   | Successive division by 8; collect remainders in reverse order.                  | Successive division by 16; collect remainders in reverse order (map 10–15 to A–F). |
| **Binary**      | Positional expansion: $\sum (d_i \cdot 2^i)$ from right to left.  | —                                                                | Group bits into sets of 3 from right to left; map each group to 0–7.            | Group bits into sets of 4 from right to left; map each group to 0–9, A–F.          |
| **Octal**       | Positional expansion: $\sum (d_i \cdot 8^i)$ from right to left.  | Expand each octal digit into its equivalent 3-bit binary string. | —                                                                               | Convert to Binary (3-bit groups) first, then regroup into 4-bit sets for Hex.      |
| **Hexadecimal** | Positional expansion: $\sum (d_i \cdot 16^i)$ from right to left. | Expand each hex digit into its equivalent 4-bit binary string.   | Convert to Binary (4-bit groups) first, then regroup into 3-bit sets for Octal. | —                                                                                  |
|                 |                                                                   |                                                                  |                                                                                 |                                                                                    |


> [!info]
>  Number of values a binary number can represent = 2 ^ n where n is the number of digits.
>  Remember the additional hexadecimal digits as: A10, B11, C12, D13, E14, F15