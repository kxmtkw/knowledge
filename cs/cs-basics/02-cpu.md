# CPU

CPU -> Central Processing Unit
It is the "brain" of the computer, responsible for performing the actual computations.
## Operation
### Instruction

Computers execute instructions. Each instruction contains an **opcode**, which is a numerical value associated with that instruction and tells the computer which operation is the be executed.
### Instruction Set & ISA

Instruction Set is the set of instructions that a CPU can execute. 

> [!info] Unknown Instruction
> The instruction set is hardwired into the CPU circuitry so a CPU cannot execute a instruction it does not know. As for what happens when a CPU encounters an unknown instruction, it halts the execution of the program and transfers control to the Host OS.

ISA -> Instruction Set Architecture
The ISA defines how a CPU interprets instructions and which instructions it can execute.

Main ISAs used in the real world include:
1. x86-64
2. ARM
3. RISC-V

> [!note] Computer Architecture
>  `Instruction Set Architecture` is different from `Micro-Architecture`. The former is an abstract set of operations that the CPU can execute while the latter is the way those instructions are implemented in the actual hardware. 
>  `Computer Architecture` might refer to both at the same time.
>  *Two computers with different micro architectures can have the same instruction set architecture.*

### Instruction Cycle

All CPUs follow the same instruction cycle.
Fetch -> Decode -> Execute.

1. Instructions are fetched from memory.
2. Fetched instructions are decoded so the CPU can figure out which operation to execute.
3. Execute the decoded operation.

The instruction cycle is triggered by an electric clock in the CPU. Every time the clock sends and electrical signal, the instruction cycle starts. Some instructions can take multiple clock cycles (like division).
#### Fetch

The memory location from which the next instruction will be fetched is determined by the `program counter`. After an instruction is fetched, the program counter is incremented, so when the next cycle runs, the next instruction can be fetched.
#### Decode

The instructions are decoded by a `binary decoder` component which turns the opcode into electrical signals.
#### Execute

The decoded instruction is then executed.


The cycle also contains data related steps, so the full cycle may be:
1. *IF*: Instruction Fetch
2. *ID*: Instruction  Decode
3. *DF*: Data Fetch
4. *IE*: Instruction Execute
5. *RR*: Return Result

## Components

A CPU consists of several components that work together to execute an operation.
### Control Unit

Control Unit (__CU__) is a component of the CPU that directs the operation. It tells the other components and devices how to respond to instructions. It directs the operation of other units with timing and control signals. It also controls the data flow between components.
### Arithmetic Logic Unit

Arithmetic Logic Unit (**ALU**) is responsible for performing arithmetic and logical computations in the CPU. It takes input registers, performs the specified operations and returns an output.
### Registers

Registers are small and extremely fast memory locations built directly into the CPU itself. They are used by the different components of the CPU to perform computations and other tasks.

1. *General Purpose Registers* store temporary data related to computations. 
2. *Special Purpose Registers* store special information.
	1. *Program Counter - PC* stores the memory location of the current instruction.
	2. *Instruction Register - IR* stores the current instruction to be decoded.
	3. *Flags or Condition Code Registers* store status bits set by arithmetic operations like zero flag `ZF`, sign flag `SF`, carry flag `CF` and overflow flag `OF`.
## Von Neumann Architecture

Von Neumann Architecture defines a theoretical computer architecture in which the instructions and data associated with those instructions are stored in the same memory unit. The entire program is stored together. Almost all modern CPUs are based off of this architecture. 

The components of this architecture include:
1. CPU
	1. CU
	2. ALU
	3. Registers
2. Shared Memory Unit
3. I/O Devices
4. Buses *Responsible for moving data between the computer components*
	1. Data Bus *Transfers data*
	2. Address Bus *Carries the address of data*
	3. Control Bus *Carries control commands from the CPU*

#### `References`

Computer Architecture:

![Computer Architecture](https://www.youtube.com/watch?v=eNtADpJ2EC4&t=16s)