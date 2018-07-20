# Scalability-and-markovian-testing

Phase 1
Two functions have been created. Because of the way that the Markovian function has been coded the maximum number of companies could be greatly increased. However it was decided that the maximum array size would be 10 because of the rounding used in calculating the ownership of each company being to one decimal point, the smallest element of ownership is 0.1. 
When significantly larger arrays are used, because of the number of reductions that typically need to occur to reduce the total ownership to 1 and the minimum unit of reduction being 0.1, the array tends towards no companies having dominant control over any others. If a smaller unit of measurement was utilised to denote ownership one could generate a much larger meaningful participation matrix.  

participation _matrix(a)
The first function generates a participation matrix of length a. a is a random number between 2 and 10. 
    The matrix assigns random values between 0 and 1 in each of a[i][j] and then subsequently changes all values where i and j are equal to 0 to indicate that no company owns itself.

make_markovian (blist)
    This function looks at the array of all the companies ownerships (blist) and on a company by company basis sums all ownership values for that company to assess whether this is greater or less than 1, which would indicate that more than 100% of the company is owned. 

E.g.    a[i][j] + a[i+1][j] ... a[maxi][j] = sum of ownership

If the ownership is greater than 1 the function will randomly pick a specific instance of ownership and do one of three things depending on the value of the ownership:
If the value is greater than 0.5 if will reduce this value by 0.1. This is to try and minimise the effects on majority ownership whilst still allowing us to reduce the overall total
For values between and including 0.2 and 0.5 the function will remove half of the value and round the result
If the value is less than 0.2 it will set the ownership at 0. This allows us to quickly remove small minority stakes.

If the ownership is less than 1 the function will randomly pick a specific instance of ownership and add half of its value, then round this new figure. It will then recalculate the total ownership of the company and see whether the total ownership is now 1.

The weightings between the changes to different levels of ownership could be changed based on preference, however using those set out above tends to produce a an array where once the seed has been set there will likely be companies with both direct and indirect ownership.

Phase 2
    A function named corp_control was created with two input variables the seed and the companies array from the previous phase.
    The function does not return a value, rather printing out two strings. One is the list of any companies that are directly controlled by the seed, the other is a list of any companies subsequently indirectly controlled.

Firstly the function creates and prints a list of any companies where the ownership is greater than or equal to 0.5.

Secondly the function creates and prints a list of all companies where the combined ownership of the seed company and all companies directly owned is greater than 0.5. This list will not include any companies that are directly owned or the seed company.

The result is correct on all small instances.

Phase 3
    Due to the length of time it takes to run the program with values of k in excess of 4, exponent values of 2,3, and 4 were chosen (k = [2,3,4]).
10 random instances of k were created and the solution run with n=10**k producing an array of n length. The time it took to to compute each iteration of k was measured.


Increasing the array size by a factor of 10 significantly increases the time it takes for the whole solution to solve. On average when K = 2 the solution is solved in 0.015 s, when k = 3 it takes 1.5 s and when k = 4 it takes anything from 200 to 350 seconds to solve. There appears to be significantly higher variation in larger arrays. However based on this we could hypothesise that solving for higher values of k would also take exponentially longer. 

If the matrix is altered to become Markovian the amount of time required to solve greatly increases, to such a level that even solving for k = 3 takes a very large amount of time. Code has been created that shows how one would test the markovian time however a powerful computer would be required to undertake this test. A better method may be using a number of smaller values of k (e.g. 0.5, 1, 1.5, 2) and then using logistic regression to hypothesise the length of time required for higher values of k.
