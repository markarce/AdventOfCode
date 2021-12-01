"""
--- Day 18: Operation Order ---
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

Your puzzle answer was 15285807527593.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?
"""

def evaluate_homework(filename, is_test_data):
    """
    input: string path to a file containing the data set (is_test_data = False),
    or the data set in string format directly (is_test_data = True)
    """

    def process_pemdas(expression):
        # parentheses, exponents, multiplication / division, addition / subtraction
        # one number (base case) means this expression is solved
        if len(expression) == 1:
            # returned as a single item list so it can be used during list addition in recursion
            return expression
        # check for parentheses first and then process the sub-expression in parentheses
        elif ")" in expression:
            for r_char in range(len(expression)):
                if expression[r_char] == ")":
                    for l_char in range(r_char - 1, -1, -1):
                        if expression[l_char] == "(":
                            return process_pemdas(expression[:l_char] + process_pemdas(expression[l_char + 1:r_char]) + expression[r_char + 1:])
        # process addition next and return the sum of two numbers before and after a "+"
        elif "+" in expression:
            evaluated = 0
            for char in range(len(expression)):
                if expression[char] == "+":
                    a = int(expression[char - 1])
                    b = int(expression[char + 1])
                    evaluated = a + b
                    return process_pemdas(expression[:char - 1] + [evaluated] + expression[char + 2:])
                    break
        # process multiplication last and return the product of two numbers before and after a "*"
        else:
            evaluated = 0
            for char in range(len(expression)):
                if expression[char] == "*":
                    a = int(expression[char - 1])
                    b = int(expression[char + 1])
                    evaluated = a * b
                    return process_pemdas(expression[:char - 1] + [evaluated] + expression[char + 2:])
                    break
    # read in a string of expressions separated on newlines as test data or from a file from disk
    data = []
    if not is_test_data:
        with open(filename) as f:
           expressions = f.read().split("\n")
    else:
        expressions = filename.split("\n")
    for expression in expressions:
        data.append(list("".join(expression.split())))

    running_total = 0
    for line in data:
        answer = process_pemdas(line)
        running_total += answer[0]
    return running_total