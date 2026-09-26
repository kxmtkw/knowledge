# Operating System

An operating system is a system softwate that manages computer hardware and software resources, and provides common services for computer programs.
## Responsiblities

An operating system is responsible for:
+ Detecting and managing hardware devices
+ Running software applications
+ Scheduling processes so multiple software applications can run at once
+ Managing networks
+ Providing security against malicious programs
+ Allow multiple users to use the same computer
+ Providing useful services to running programs
+ And much more...

> [!info] Timesharing systems and Real time systems
> A timesharing system allows multiple users to use the same machine at the same time.
> A real time system (RTOS) allows processing data with strict time constraints.
## OS Concepts
### Process

A process is an active instance of an executable that is currently being executed by the operating system, loaded into RAM with allocated system resources.

> [!note] Program vs Executable vs Process
>  A program is the conceptual set of logic that is written by a person, with the intention of perfoming some task.
>  An exectuable is a compiled binary of instructions stored in disk that can be executed.
>  A process is a live instance of an executable that is currently being ran by the operating system.

### Process Management

A process is managed by the OS for its whole lifecycle.
A process can be in one of many states during its lifecycle.

![Process Lifecycle|587](https://media.geeksforgeeks.org/wp-content/uploads/20250825180931532602/bb.webp)

1. `New` -> Process is just created
2. `Ready` -> Process is ready to be ran
3. `Running` -> Process is running
4. `Blocked/Waiting` -> Process is waiting for IO or for a system call.
5. `Exit` -> Program finishes execution.

A process maybe only enter the `New` and `Exit` stages once in its lifetime while it may interchange between the other three states many times.

> [!info] Running State
> Only one process can be in the running state at a given time. Unless the CPU has multiple cores which can execute multiple processes at the same time.
#### PCB

`Process Control Block` or the PCB is a data structure used by the OS to store information related to a process.

It stores information like:
+ Current PC
+ Values of all the registers
+ Page tables

Each state has its own PCB list that holds information about each process in that list.

### Memory Management

A process may see `Logical Memory Addresses` which get translated to `Physical Memory Addresses`.

This allows for:
+ More security (A process can not access another process' memory)
+ Flexible and non-continuous allocation (A process's memory space might be distributed in different regions of the RAM)
+ Paging and Virtualization (The OS can map logical addresses to disk memory instead of RAM in case of memory shortage)
+ The program logic does not have to care about the changing physical addresses.

An OS may manage memory as:
1. `Single Contiguous MM` has only the OS and one program being executed.
2. `Partition MM` has the OS and any number of programs being run.
	1. `Fixed` The memory is divided into fixed blocks.
	2. `Dynamic` The memory can be dynamically created to fit a program's needs.

The logical to physical address conversion is supported by the CPU itself. The CPU has a `Base Register` that holds the address of the starting of the current partition and a `Bounds Register` that holds the length of the current partition.

> [!info] Illegal Memory Access Check
> If the *Specified Address* is less than the one in the *Base Register* or is greater than the sum of *Base Register* and *Bounds Regiser* address, then a trap to OS is triggered. The CPU halts the current process and transfers control back to the OS, so it can handle the illegal memory access.

#### Allocating Partitions

There are three common ways to allocate partitions to programs.
1. `First Fit` Find the first partition capable of holding the program memory.
	+ Is the fastest but can be inefficient in terms of memory usage.
2. `Best Fit` Find the smallest partition capable of holding the program's memory.
	+ Is the most efficient in terms of memory usage but can lead to small unusable fragments that deter memory efficiency in the long run.
3. `Worst Fit` Find the largest partition capable of holding the program's memory.
	+ Can lead to less fragmentation but wastes memory in the long run. 

### CPU Scheduling

A CPU can only execute one instruction at a time so it is impossible for multiple programs to be ran at once. To solve this, the OS implements `Scheduling`.
Each process gets to use the CPU for a specified amount of time before another process can be executed.

Scheduling may be of two types:
1. `Non-Preemptive` The current process has to give control of CPU back to OS voluntarily.
2. `Preemptive` The OS decides which process can run by favoring one process and halting the execution of the current one.
#### Scheduling Metrics

The following time metrics are used in the domain of CPU scheduling.
+ `Arrival Time - AT` The time a process enters the ready state.
+ `Burst Time - BT` The time a process takes to execute.
+ `Current Time - CT` The current clock time
+ `Completion Time - CT` The clock time at which the process finishes execution
+ `Turnaround Time - TAT` The actual time a process took to execute. It is: $$ Completion \space Time - Arrival \space Time$$
+ `Waiting Time - WT` The time the process spent waiting for execution. It is: $$Turnaround \space Time - Burst \space Time$$
+ `Response Time - RT` The time it takes for the process to be executed for the first time since arrival. It is: $$First \space CPU \space Execution \space Time - Arrival \space Time$$
#### Scheduling Algorithms

Algorithms are used to schedule processes on the CPU.
Some algorithms include:

+ `First Come, First Served - FCFS` The process that enters the ready queue first is executed. The upcoming processes have to wait for their turns.
+ `Shortest Job Next - SJN` The process with the shortest estimated running time is executed first.
+ `Round Robin` Each process is only allowed to run for a fixed amount of time, referred to as the *Time Quantum*. A running process that hits the time quantum is halted and moved back to the ready queue where it has to wait for its turn again.

> [!info] Average TAT
> SJN gives the shortest average TAT while FCFS gives the longest average TAT.

#### Round Robin

Round Robin is a scheduling algorithm that focuses on fair sharing and usage of the CPU by each process. Each process is only allowed to execute for a fixed amount of time (`Time Quantum`) before it is halted and put back in the ready queue.

Consider the following set of processes.

| Process | Arrival time | Burst time |
| ------- | ------------ | ---------- |
| P0      | 0            | 250        |
| P1      | 50           | 170        |
| P2      | 130          | 75         |
| P3      | 190          | 100        |
| P4      | 210          | 130        |
| P5      | 350          | 50         |

A RR based scheduler will manage the processes as:

![629](https://upload.wikimedia.org/wikipedia/commons/5/50/RoundRobin.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original)