# Defining Function
import math
def f(x):
    return 2*(x**3)-3*x-6

# Defining derivative of function
def g(x):
    return 6*(x**2)-3


# Implementing Newton Raphson Method

def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero is error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print("==============================================================")
        print('Iteration : %d\nRoot Obtained : %0.6f \nEstimated Error : %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print("-------------------------------------------------")
        print("===============Finally===========================")
        print('\tIteration : %d\n\tRoot Obtained : %0.6f \n\tEstimated Error : %0.6f' % (step-1, x1, f(x1)))
        print("=================================================")
    else:
        print("===============Finally===========================")
        print('II --------------Not Convergent.---------------II')
        print("=================================================")



# Input Section
x0 =float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))


# Starting Newton Raphson Method
newtonRaphson(x0, e, N)