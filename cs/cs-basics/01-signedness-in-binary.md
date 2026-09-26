## Unsigned numbers

- Cannot represent negative values.
- For a binary number of $n$ digits, it can hold numbers ranging between:
$$
[0, 2^{n}-1]
$$

## Signed numbers

Signed numbers cannot be represented by simply using a $-$ sign, because it does not exist in computer binary. 

There are three techniques for this:
### Signed magnitude

- Left-most digit or the MSB is the sign bit.
	- 0 -> positive
	- 1 -> negative

```
1000 0001

1 -> sign bit (-ve)
000 0001 -> magnitude = 1

value -> -1
```

Range:
$$
[-(2^{n-1}-1),(2^{n-1}-1)]
$$
For a byte: $[-127, 127]$

Downsides:
- Requires more complex circuitry for arithmetic.
- Two zeros (0, -0)

### One's complement

- To get negative numbers in this technique, simply invert the bit pattern of the positive variant.

```
0010 -> 2
1101 -> -2
```

- MSB still indicates that this is a negative number.

Range:
$$
[-(2^{n-1}-1),(2^{n-1}-1)]
$$
For a byte: $[-127, 127]$

Upsides:
- Arithmetic now easier due to same circuits for add/sub.

Downsides:
- Still two zeros.

### Two's complement

Obtained by taking the bitwise inverted digit and adding one.
```
0010 -> 2
1101 # bitwise inverted 2
1110 # added 1
1110 -> -2
```
- MSB still indicates that it is a negative number.

Range:
$$
[-(2^{n-1}),(2^{n-1}-1)]
$$
For a byte: $[-128, 127]$

Upsides:
- Arithmetic even more easier because wrap around.
```
0000 - 0001 = 1111
# 0 - 1 = -1
```
- Only one zero now.

## Converting

Just solve logically. Here is some tips:
- For signed magnitude, just find the magnitude of the n-1 bits.
- 2's complement is just 1's complement + 1
- To go back to 1's complement from 2's complement, either:
	- -1 and invert
	- invert and +s1