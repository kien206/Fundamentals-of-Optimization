# Fundamentals-of-Optimization
This is my code for my IT3052E Fundamentals of Optimization mid-term project. 
Our problem can be described as follows:

There are N classes that need to be scheduled.
Each class i has:

t[i] is the number of lessons

g[i] is the teacher teaching class i

s[i] is the number of students in class i

There are M rooms 1,2,....,M and c[i] is the number of seats of the room i.

In a week, there are 5 days (from Monday to Friday), each day is divided into 12 shifts
(6 morning shifts and 6 afternoon shifts).

Create a schedule(assign day, shift and room) to each classes that satisfies:

a.Two classes that having the same teacher need to be scheduled separately.

b.The number of each class has to be smaller than the capacity of the room.

*Input:

- The first line: N and M

- The next N line, each line writes: t[i], g[i] and s[i]

- N+2 line: c(1),c(2),...., c(M)

*Output:

- Line 1: contains a positive integer Q
- Line q + 1 (q = 1, 2, . . ., Q): contains 3 positive integers i, u, and v in which class i is assigned to slot u and room u

I am responsible for the Greedy algorithm and Constraint Progamming using or-tools. Other algorithms that we used are Mixed Integer Programming, Local Search and Genetic algorithm.
