# Introduction Algebra

## Sets

### You know what a set is

A set is `collection` of **distinct** objects. These objects are called the elements or members of the set. A set is defined as a list of these elements encaptulated with this symbols `{ your elemts }` and every elemnt is seperated with a `,` so the set of the numbers $3$ and $4$ is written in the roster notation as follows $\{3, 4\}$. 

If you have a big set that folows a clear pattern you can use `...` to symbolise that the set continous. Consider for example a set with all the positiv interes, you can say this set contains the numbers 1, 2, 3 and so on. To convert this into an mathematil expression you just have to substitute `and so on` for `...`. Following this you would end up with a set that looks like this $\{1, 2, 3, ...\}$. You can also do this in the other direction like for example $\{..., -2, -1, 0, 1, 2, ...\}$ this set would represent every integer.

There also exists an `empty set` that can be written as $\{\}$ or $\emptyset$.

### You know the operations that you can perform on sets

Every of the following examples has two sets $A = \{2, 4, 6, 10\}$ and $B = \{2, 5, 10, 20\}$ 

- An `union` between to sets is all of thier elements combined into one set and can be written like this $A \cup B$, pronounced as `A-cup-B`. With the example definition above this would equal $\{2, 4, 5, 6, 10, 20\}$.

- Computing the `intersection` of two sets results in a set containg elemts that both sets have in common and can be writte like this $A \cap B$, pronounced as `A-cap-B`. With the example definition above this would equal $\{2, 10\}$.

- The `difference` between thwo sets results in one set that contains every element of the first set that is not in the second one. This can be written as $A \setminus B$, pronounced as `A-minus-B`. This results with the example definition above in the following set $\{4, 6\}$. 

- Sets can also be multyplied with the `cartesion product` and can seem on the first glance a little strange. It is written as $A \times B$. This is besed exmplained on a table where the first column is the set $A$ now beeing $\{1, 2\}$ for simplisity and is the first row $B$ now only beeing $\{3, 4\}$
  
  |     | 3      | 4      |
  | --- | ------ | ------ |
  | 1   | (1, 3) | (1, 4) |
  | 2   | (2, 3) | (2, 4) |
  
  The resulting of this multiplication is therefore equal to $\{(1, 3), (1, 4), (2, 3), (2, 4)\}$

### Sets of numbers

- The `natrual` $\N$ numbers are all bigger or equal to $0$ and are integers

- The `integers` $\Z$ numbers are all the integers

- The `rational` $\mathbb{Q}$ numbers are all numbers that can be described by a fraction like $\frac{a}{b}$ where $a$ and $b$ are positive and $b$ is not equal to $0$

- The `real` $\R$ contain all the remaining *conventional* numbers.

- The `complex` numbers are a special set of numbers. That extend the number line into the y-axis. Complex numbers are written as $a+bi$ where $a$ and $b$ are real numbers. The $a$ factor can be compared to the x-cordinates of a point and the $b$ factor to the y-cordinates of a point on a graph.
  
  $i$ is a sepcial number in methematics that is defined as the $\sqrt{-1}$ which can not exist because $-1² = 1$. So $i$ is just like the *unit* on the y-axis

Pease be aware that evey number set contains all of its previous number sets like for example the rational numbers contains also the inters and natural numbers.

## Positional notation of numbers

### Binary into Decimal

You can convert Binary numbers into decimal number with these simple steps

- Only to do at the baggining: Take the first binary digit

- Double your number and add the next binary digit

- Continue like this

This can be shown in a table going from left to right. In the first row we write all the digits of the binary number and in the bottom row we will keep track of the current result of our computations.

| binary  | 1   | 1   | 0   | 1   |
| ------- | --- | --- | --- | --- |
| decimal | 1   | 3   | 6   | 13  |

The bottom right cell is now your result. If you don't completely unterstand the prcedure this is what is caulcualted:

- Take the first digit, in this case $1$

- Double it add add the next digit, in this cae also $1$ and write down the tmporary result $3$

- Take $3$ double it add the next digit and you result in $6$

- Then double it again and add the last digit, leaving you with $13$

### Decimal into Binary

This can be solved very similary to the last problem by just going backword.

- Only to do at the beginning: Take your decimal number and write it in the bottom right cell

- If it is uneven write down $1$ in the binary row and subtract $1$, if it is even write a $0$

- Devide it by $2$ and write it left from your last number

- Do this until your number becomes $0$

The same example as in the table above can be explained with these steps

- Take $13$ and wirte it down, because it is uneven wirte a $1$ and subtract $1$ then devide by two. The result $6$ can ten be written down left from the $13$

- $6$ is even so can write down a $0$  for the binary row and just devide $6$ by $2$ and you can write $3$ left from it

- $3$ is uneven so you can wirte down $1$ and subtract $1$, then you can devide by two leaving you with the decimal number $1$ to write down left from the previous result.

- $1$ is uneven so write down a $1$ and subtract a $1$. Your result of this operation is $0$ so your done but there is no need to write it down.

### Scientific notation

Every number can be represented with the scientific notation that goes as follows

$$
a * 10^b
$$

Where $a$ is any number equal or bigger then 1 but smaller then 10. $b$ can be any negative or positive integer. I you want to write the number $0.000000005234$ in scientific notation. You have to move the decimal point until the new number satisfiies the condition for a. In this case you have to move it $9$ times to the right resulting in $5.234$, this number becomes your a. This results in

$$
5.234 * 10^{-9}
$$

The exponent ($b$) has a minus here because when we moved the decimal point to the right. When we wan't to write a very big number in scientific notation then we move the decimal point to the left and $b$ becomes positive.

### Multiplication with scientific notation

Suppose we have two numbers in scientific notation

$$
a * 10^b, \space c * 10^d 
$$

The the we can multiply the like this

$$
(a * 10^b) * (c * 10^d) = a * c * 10^{b + d} 
$$

Lets do an example

$$
(2.3 * 10⁵) * (3.5 * 10²) = 2.3 * 3.5 * 10^{5 + 2} = 8.05 * 10⁷
$$

If the result of $a * c$ becomes grater then $10$ then you have to move your decimal point again until you get a valid number in scientific notation as described above. 

### Divison with scientifc notation

Suppose we have two numbers in scientific notation

$$
a * 10^b, \space c * 10^d 
$$

The we can devide them like this

$$
\frac{a * 10^b}{c * 10^d} = \frac{a}{c} * 10^{b - d}
$$

Lets do an example

$$
\frac{8.4 * 10^3}{2.4 * 10⁵} = \frac{8.4}{2.4} * 10^{3-5} = 3.4*10^{-2}
$$

Rememper if the result of $\frac{a}{c}$ becomes smaller then $1$ you have to adjust your number again until it meets the constranints for a number in scientific notation.

## Basic arithemetic with some help of gemoetry

### Addition and subtraktion

Let's imagine a point on the number line that represents the number $3$ now if we want to add the number $+2$ to it we draw an arrow from $3$ pointing to the right with the lenght of $2$. Now the addition can be representing as schifting the entire number line from the origin of or arrow to its end. Please not that we are just schifting the line with our number $3$ on it, our scale stays where she is. So if we shift **just** the line by two then $3$ ends up on $5$. 

Subtraktig would be the same operation just with our arrow pointing left.

### Multiplication

Let's imagine the number $4$ as a point on the number line and we want to multiple it with the number $2$. Tho achichieve this we can stretch the number line by a factor of $2$  in both direction from the origin with our point representing the $4$ on it but the the position of all ther numbers on our number line are left where they are only the line with the point is streached. So when we strech the number line with a factor of $2$ the point that befor represend $4$ now ends up on $8$.

Multiplication with a negative number can be simplified into two operation. First we hav eto flip the number line around it origin, this opearation accounts for the $-$ sign and then we can stretch it. So multilpying a number with $-1$ and then again with $-1$ will give us a positive number because we flip the number line twice.

## Inequalities

Inequalities can be solved like every equasion just by keeping this rules in mind.

Let $a$ and $b$ be any real number

- If you multiply or devide both sides of an inequality with an negative number then you have to flip the inequality sign. Take this as an example
  
  $$
  a < b \space \space \space \space \space \space \space | * (-5) \\
-5a > -5b \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space
  $$

## Linear equations with two variables

A linear equasion can be defined with this `slope-intercept` formula

$$
y = ax + b
$$

Where $x$ and $y$ are variables. The factor $a$ is the slope and $b$ is the Y-intercept.

### Slope

The slope of a linear equation defines by how much does the the values change between that are $1$ unit away from each other on the x-axis.

Lets define two points $P = (4, 4)$ and $Q = (8, 2)$

Then the slope can be computed as the y-difference between this points devided by the x-difference.

$$
a = \frac{\Delta y}{\Delta x} = \frac{y_p - y_q}{x_p - x_q} = \frac{4 - 2}{4-8}=-0.5
$$

 Please note that it doesnt matter if you subtract $Q$ from $P$ or $P$ from $Q$.

### Y-intercept

The y-intercept $b$ is added to every point is jut an offest. The y-intercept can be directly determinated when we are given a point where $x = 0$ otherwise you can take any point and calculate it with this formula

$$
b = y - ax
$$

### Point-slope of a line

If you don't want to calculate the Y-intercept you can express a linear equasion by just using the slope and two points.

If we take the two points $P$ and $Q$ from the slope example above an the calculated slope $a = -0.5$ 

Then we can write the equasion as

$$
y-y_0=a(x-x_0)=y-4=-0.5(x-4)
$$

You can use any point for $y_0$ and $x_0$ it just has to be the same for both the x and y cordinates.

### Standart Form

Imagine we have a vertical line at $x=2$ how could we represent this with the standart-form equation ($y=ax+b$)? To achieve this $a$ would have to be infinite so the slope doesn't make any sense. So to express such a linear equasion we can just write $x = 2$ because $y$ can be any value.

So for such cases we can use the standart form, written like this

$$
ax+by=c
$$

Plese note theat $a, b, c$ in the stnadart form are not the same as in the point-intercept from. This equsion will even hold true for a vertical line because then we can just say that $a=1$, $b=0$ and $c$ is euqal to the x cordinates where our vertical line. Let's assume $2$. So the whole formula would be

$$
1*x+0*y=2
$$

Which we can simplify to

$$
x = 2
$$


