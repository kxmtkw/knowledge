# Introduction

Programming is the art or skill of instructing a computer to do something.
Computers are programmed/instructed using languages.

This is the basic introduction of programming languages and computers in general.


## Computer Organization

A computer consists of several parts that work together. By functionality, a computer can be divided into three kinds of parts:

- IO devices for input and output of data.
- Storage devices for storing data.
- Processing devices for processing data.


### IO

Input devices take in input data for the computer. For example, mouse, keyboard, camera, touchpad, mic etc.
Output devices are used to show data. For example, screens, speakers, LEDs etc.


### Storage

Storage devices are used to store data. For example, SSDs and HDDs.


### Processing

The main processing device in any computer is the CPU.
CPU, standing for **Central Processing Unit**, is the heart of a computer.
It is the main component doing all calulations.
It also has several sub components:

- Control Unit manages the whole CPU, executing instructions an routing data.
- ALU, **Arithmetic Logic Unit**, does calculations and performs operations.


## A computer's language

Computers only understand binary. This is because:

- Computers work using transistors and currents which can either be on or off.
- Binary is easier to work with when you are already dealing with something as difficult as CPU designing.

Computers (specifically CPUs) execute instructions in a standard three step pipeline:
```
Fetch -> Decode -> Execute
```
- **Fetch**, get the instruction to execute.
- **Decode**, find out what that instruction is.
- **Execute**, run that instruction.

This is simplified explanation. In real CPUs, each step of the cycle is further divided into many steps.
For example, during **Fetch**, a CPU might need to first tell the RAM what address in the memory it needs to get, the RAM will then send the data at that address to the CPU.


## Binary Data


### Bit
The smallest possible piece of information that can be provided in binary is whether something is on or off. One and Zero.

`A bit is defined as a single binary digit which can hold only 2 values, either 1 or 0.`

$$
bit = 1 \ or \  0
$$

A bit is the most basic form of information possible.

Bits by themselves are kind of useless, what are you gonna do with a single digit? Computers also do NOT work on individual bits.

### Bytes and Nibbles

Computers work on bytes!

`A byte is a group of 8 bits.`

A single byte is composed of 8 binary digits and is the smallest unit on which a computer can work. A bit allowed you to store 2 numbers: 0 and 1. While a byte allows you to store 256 numbers starting from 0 all the way up to 255.

```
0000 0000 -> 0
0000 0001 -> 1
0000 0010 -> 2
0000 0011 -> 3
...
1111 1101 -> 253
1111 1110 -> 254
1111 1111 -> 255
```

There also exists a nibble. `A nibble is a group of 4 bytes`. It can store numbers 0 to 15 (so 16 numbers). A byte consists of two nibbles, called as the high and low nibble respectively.

> Generally, a group of bits is called as a bit array, bit string or a one-dimensional bit vector. A bit array with 4 bits is a nibble an a bit array with 8 bits is a byte.

> Bits are not really that useless. They are actually crucial in cybersecurity (cryptography) and low level programming (operating system masks and flags)


### Chars (short for Characters)

`A char in computer science is a mapping of a natural language characters (like the ABCs, digits etc) along with control characters to binary data.`

Chars are formed by assigning a value to each symbol needed. These assigned values are called code points.

The most famous mapping is ASCII, which stands for **American Standard Code for Information Interchange**. ASCII maps characters to a single byte. Since a single byte can store upto 256 numbers, 256 characters can be represented using the ASCII system. In reality, ASCII maps only 128 characters from 0 to 127, (So only 7 bytes are used.) Out of these 128 characters, only 95 are actually printable, the rest are control characters.

Here is the ASCII table for reference: [ASCII Table](/cs/general/ascii-table.md)

> Control Characters can be thought of as "commands" to the printer. In the early ages, these were used to trigger the printer to do something special. Most of these are obsolete now.