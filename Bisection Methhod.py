# Defining Function
def f(x):
    return 4*(x**3) - 6 * (x**2) +7*x-2.3



# Implementing Bisection Method
def bisection(x0, x1, e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    x2 = 0
    error = x0 - x1
    condition = True

    while condition:
        c = x2

        x2 = (x0 + x1) / 2
        print("===========================================")
        print('Iteration = %d,\nRoot  = %0.6f \nEstimated Error = %0.6f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        error=(c-x2)/x2
        step = step + 1
        condition = abs(error) > e



    print("---------------------------------------------------")
    print("======================Finally======================")
    print('Iteration = %d,\nRoot  = %0.6f \nEstimated Error = %0.6f' % (step-1, x2, f(x2)))





x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('True Error: '))


# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0, x1, e)