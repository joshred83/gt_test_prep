# New Questions for Prob/Stats/Simulation

## Question 1
**TRUE or FALSE?**  
Discrete-event simulations are not suitable for modeling systems with time-continuous variables like temperature fluctuations in a room.

---

## Question 2
A single-server queue simulation has i.i.d. exponential interarrivals and i.i.d. exponential service times. The service discipline is FIFO, with an arrival rate of 3 customers per minute and a service rate of 5 customers per minute.  
1. What is the long-term utilization of the server?  
2. What is the expected number of customers in the system?

---

## Question 3
**TRUE or FALSE?**  
If the correlation coefficient between $X$ and $Y$ is zero, then $X$ and $Y$ must be independent.

---

## Question 4
A planet has 150-day years. If there are 6 residents in a room, what is the probability that at least two of them share the same birthday?  
(Assume all days are equally likely.)

---

## Question 5
Suppose a coffee shop receives customers according to a Poisson process with a rate of 10 per hour.  
1. What is the probability of receiving exactly 5 customers in a 30-minute interval?  
2. What is the expected time until the next customer arrives?

---

## Question 6
If $X \sim \text{Bern}(0.3)$, find $\mathbb{E}\left[5 - 2e^{X}\right]$.

---

## Question 7
If $X$ has a mean of 10 and a variance of 6, find $\text{Var}(15 - 3X)$.

---

## Question 8
Suppose $X$ is a continuous random variable with p.d.f. $f(x) = 4x^3$ for $0 < x < 1$.  
1. Find the expected value of $X$.  
2. Find $P(X > 0.5)$.

---

## Question 9
Suppose $X$ and $Y$ are i.i.d. random variables with a mean of 8, a variance of 5, and $\text{Cov}(X, Y) = 3$.  
1. Find $\text{Var}(X + Y)$.  
2. Find $\text{Corr}(X, Y)$.

---

## Question 10
Two random variables $X$ and $Y$ have joint p.d.f.  
$$
f(x, y) = \frac{k}{(1 + x^2 + y^2)^2}, \quad 0 \leq x \leq 2, \, 0 \leq y \leq 2,
$$
where $k$ is a normalization constant.  
1. Determine $k$.  
2. Are $X$ and $Y$ independent?

---

## Question 11
Consider the integral:
$$
I = \int_0^1 e^{-x^2} \, dx.
$$
Use the Monte Carlo method with $n = 5$ samples from $\text{Unif}(0,1)$ random numbers: $0.12, 0.45, 0.63, 0.78, 0.95$.  
1. Compute a Monte Carlo estimate of $I$.  
2. Calculate the standard error of your estimate.

---

## Question 12
Toss 10,000 darts uniformly into a unit square. Use the proportion of darts that land within a circle of radius $0.4$ inscribed in the square to estimate $\pi$.  
If 5,020 darts land inside the circle, what is the estimate for $\pi$?

---

## Question 13
Suppose $U \sim \text{Unif}(0,1)$. Use $U$ to simulate the outcome of rolling a 20-sided die.  
1. What formula should be applied?  
2. Simulate the result if $U = 0.67$.

---

## Question 14
Consider the discrete random variable $X$ with:
$$
P(X = x) =
\begin{cases}
0.3 & \text{if } x = -5, \\
0.4 & \text{if } x = 1, \\
0.3 & \text{if } x = 3, \\
0 & \text{otherwise.}
\end{cases}
$$
Use the Inverse Transform method and the $\text{Unif}(0,1)$ random number $U = 0.27$ to generate one observation of $X$.

---

## Question 15
Consider the linear congruential generator:
$$
X_{i+1} = (5X_i + 3) \mod 16.
$$
1. If $X_0 = 7$, calculate the next two pseudo-random numbers.  
2. What is the period of this generator?

---

## Question 16
Suppose $X$ and $Y$ are i.i.d. $\text{Exp}(\lambda)$ random variables. Use simulation to approximate $P(X + Y > 3)$ with $n = 1000$ samples.  
1. Provide the simulation procedure.  
2. Calculate the estimate if $n = 10$ samples give 7 successes.

---

## Question 17
Consider a FIFO single-server queue where customers arrive according to a Poisson process with a rate of 4 per hour, and service times are exponential with a mean of 15 minutes.  
1. What is the average number of customers in the system?  
2. What is the probability that the server is idle?

---

## Question 18
**TRUE or FALSE?**  
In Arena, modules such as GENERATE, ASSIGN, and DISPOSE are used to create, modify, and remove entities, respectively.

---

## Question 19
Which Arena module allows you to decide between different entity routes based on conditions or probabilities?

1. DECIDE  
2. ASSIGN  
3. CREATE  
4. PROCESS  
5. DISPOSE  

---

## Question 20
**TRUE or FALSE?**  
The $\text{Unif}(0,1)$ random numbers generated in a computer simulation are always independent.

---

Let me know if you'd like additional questions or modifications to these!


# Additional New Questions for Prob/Stats/Simulation

## Question 1
A hospital has two emergency rooms. Patients arrive at each emergency room according to independent Poisson processes, with rates of 6 patients per hour for Room A and 8 patients per hour for Room B.  
1. What is the probability that exactly 3 patients arrive at Room A in the next 30 minutes?  
2. What is the probability that no patients arrive at either room in the next 10 minutes?

---

## Question 2
A single-server queue operates with i.i.d. exponential interarrival times (mean 2 minutes) and i.i.d. exponential service times (mean 1 minute).  
1. What is the utilization of the server?  
2. What is the expected waiting time in the queue for a customer?

---

## Question 3
Suppose $X$ and $Y$ are random variables such that $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$, and $\text{Cov}(X, Y) = 6$.  
1. Find $\text{Var}(2X + 3Y)$.  
2. Compute the correlation coefficient between $X$ and $Y$.

---

## Question 4
Suppose $X \sim \text{Unif}(0,1)$. Using $X$, simulate the result of flipping a biased coin where $P(\text{Heads}) = 0.3$ and $P(\text{Tails}) = 0.7$.  
What value of $X$ would simulate a heads? Explain.

---

## Question 5
The daily demand for a product follows a normal distribution with a mean of 100 units and a standard deviation of 15 units.  
1. What is the probability that demand exceeds 120 units on a given day?  
2. What level of demand corresponds to the 95th percentile?

---

## Question 6
A company observes that failures in its machinery follow a Poisson process with a rate of 2 failures per week.  
1. What is the expected time until the next failure?  
2. What is the probability of at least 3 failures in the next 2 weeks?

---

## Question 7
Suppose $X \sim \text{Exp}(\lambda = 2)$ and $Y \sim \text{Exp}(\lambda = 3)$ are independent.  
1. Find $P(X < Y)$.  
2. Simulate 5 samples from the maximum of $X$ and $Y$ using random $\text{Unif}(0,1)$ values: $0.15, 0.33, 0.56, 0.78, 0.92$.

---

## Question 8
Suppose $X$ is a continuous random variable with p.d.f. $f(x) = 2x$ for $0 < x < 1$.  
1. Find the expected value of $X^2$.  
2. Compute $P(0.25 < X^2 < 0.5)$.

---

## Question 9
Consider a queue where customers arrive at a rate of 2 per minute and service times are exponential with a mean of 1 minute.  
1. What is the average number of customers in the queue?  
2. What is the probability that the server is busy?

---

## Question 10
**TRUE or FALSE?**  
The Central Limit Theorem applies even if the underlying distribution of the data is not normal, provided the sample size is sufficiently large.

---

## Question 11
A factory produces widgets, and the lifetime of a widget follows an exponential distribution with a mean of 100 hours.  
1. What is the probability that a widget lasts more than 150 hours?  
2. If 3 widgets are used independently, what is the probability that at least one of them lasts more than 150 hours?

---

## Question 12
Suppose $U \sim \text{Unif}(0,1)$. Use $U$ to simulate the outcome of rolling a fair 6-sided die and a biased 6-sided die where $P(1) = 0.4$, $P(2) = 0.2$, and $P(3) = P(4) = P(5) = P(6) = 0.1$.  
1. What formula would you use for the fair die?  
2. Simulate outcomes for both dice if $U = 0.25$.

---

## Question 13
Suppose a discrete random variable $X$ has the following distribution:
$$
P(X = x) =
\begin{cases}
0.2 & \text{if } x = -1, \\
0.5 & \text{if } x = 2, \\
0.3 & \text{if } x = 4, \\
0 & \text{otherwise.}
\end{cases}
$$
Use the Inverse Transform method and a $\text{Unif}(0,1)$ random number $U = 0.62$ to generate one observation of $X$.

---

## Question 14
Suppose $X$ and $Y$ are independent $\text{Exp}(\lambda = 1)$ random variables. Find the probability that $X + Y > 3$.

---

## Question 15
A continuous random variable $X$ has p.d.f. $f(x) = \frac{1}{x^2}$ for $x \geq 1$.  
1. Verify that this is a valid p.d.f.  
2. Compute the expected value of $X$.

---

## Question 16
In a single-server queue, customers arrive according to a Poisson process with rate 10 per hour, and service times are exponential with a mean of 4 minutes.  
1. What is the average time a customer spends in the system?  
2. What is the average length of the queue?

---

## Question 17
**TRUE or FALSE?**  
In discrete-event simulation, the simulation clock only advances when an event occurs.

---

## Question 18
Suppose $U_1$ and $U_2$ are i.i.d. $\text{Unif}(0,1)$ random variables. What is the distribution of  
$$
X = \sqrt{-2 \ln(U_1)} \sin(2\pi U_2)?
$$

---

## Question 19
A factory uses a linear congruential generator defined by:  
$$
X_{i+1} = (7X_i + 3) \mod 11.
$$
1. If $X_0 = 4$, generate the next 3 pseudo-random numbers.  
2. Determine the period of the generator.

---

## Question 20
Suppose you want to approximate the integral
$$
I = \int_0^1 e^{x^2} \, dx
$$
using Monte Carlo simulation.  
1. Describe the simulation procedure.  
2. Compute the estimate if $\text{Unif}(0,1)$ random numbers are $0.1, 0.3, 0.5, 0.7, 0.9$.

---

Let me know if you'd like even more questions or tweaks to these!
