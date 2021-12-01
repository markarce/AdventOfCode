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
"""

def evaluate_homework(filename, is_test_data):
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


def process_pemdas(expression):
    # parentheses, exponents, multiplication / division, addition / subtraction
    if len(expression) == 1:
        return expression
    elif ")" in expression:
        for r_char in range(len(expression)):
            if expression[r_char] == ")":
                for l_char in range(r_char - 1, -1, -1):
                    if expression[l_char] == "(":
                        return process_pemdas(expression[:l_char] + process_pemdas(expression[l_char + 1:r_char]) + expression[r_char + 1:])
    else:
        evaluated = 0
        for char in range(len(expression)):
            if expression[char] == "*" or expression[char] == "+":
                operation = expression[char]
                a = int(expression[char - 1])
                b = int(expression[char + 1])
                if expression[char] == "*":
                    evaluated = a * b
                elif expression[char] == "+":
                    evaluated = a + b
                del expression[char - 1:char + 2]
                return process_pemdas([evaluated] + expression)
                break