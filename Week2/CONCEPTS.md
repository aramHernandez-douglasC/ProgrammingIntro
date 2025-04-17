**Week 2**
-
**Conditionals and Loops**

**Objectives:** 
- Understand the way conditionals help us to make decisions
when taking into account different scenarios. 
- Know what is a loop and iterations, and the usage for handling logic
with large lists of items.

**Conditionals**
-

In programming, conditionals allow your code to make decisions. 
Just like in real life, you often make decisions based on conditions:

`If it’s raining, take an umbrella. Otherwise, enjoy the sunshine.`

In Python, we do the same using `if, elif, and else` respectively.

**Main keywords**

| Keyword | Meaning                                 |
|---------|-----------------------------------------|
| if      | Check if a condition is True            |
| elif    | Else if — check another condition       |
| else    | If none of the above conditions are met |


**Logical operators**

You can also combine conditions using:

`and` → both conditions must be true
`or` → at least one condition must be true
`not` → reverses the condition

Remember, this concept is tied and similar to what we saw on
the first session, the binary truth tables.
Think about the concept of the `and`, `or` & `not` the same as them since they work
in a similar fashion 

i.e 

`if (condition1 and condition2)`

is equivalent to

`1 && 1 = 1`

----

**Loops**
-

In programming, loops allow your code to repeat certain set of actions until
a certain condition is met in a linear manner (from start to beginning).
In real life, for instance, we often repeat actions:

- Brush your teeth every day.
- Stir the soup until it boils.
- Count from 1 to 10.

In Python, we use loops to repeat code automatically.

We have 2 types of loops in python:

| Loop Type  | When to use                                |
|------------|--------------------------------------------|
| for loop	  | When you know how many times to repeat     |
| while loop | When you repeat until a condition is false |

**For loop**

So let's break down the for loop in the ways you can use it:

1. When _iterating*_ over items and we want to get ONLY VALUES
```
for item in collection:
    # Do something with item
```
If you notice here we are only accessing one value at the time from the
collection.

2. When _iterating_ over a range of numbers (0 to infinity)
```
for number in range(1, 6):
    print(number)
```
Here we are looping and printing a number 5 times since we are starting from 1 and ending up at 6.

Now, you might notice something interesting here, even though we say range(1, 6), the loop only prints numbers up to 5, not 6.
That’s because in Python, the range() function includes the start number, but it stops right before the end number.
So range(1, 6) means:

`Start at 1, and keep going until you reach 6 — but don’t include 6.`

The loop checks each number before running the code. As soon as it sees that the next number is 6, it stops.

Think of it like walking up to a door, but not going through it.


**While loop**

The difference with the for loop is that here we will evaluate a custom conditionn
and run the subsequent code until that condition is no longer met.

```
while condition:
    # Keep running this block
```

i.e. 
```
count = 1

while count <= 5:
    print(count)
    count += 1
```

**Loop control statements**
-

Sometimes when writing our logic inside the loop we might want to
check skip an specific iteration if a condition is met or even break the loop
completely once we completed out objective

| Statement | Purpose                    |
|-----------|----------------------------|
| break     | Stop the loop completely   |
| continue  | Skip to the next iteration |

i.e.

```
for num in range(1, 10):
    if num == 5:
        break
    print(num)
```

Real World Analogy:

🌀 For loop = To-do list
📋 “For each item on my list, do it.”

🔁 While loop = Oven timer
⏱ “While the timer is running, keep checking the oven.”
