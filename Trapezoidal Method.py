def f(x):
    return 4*(x**2)-2*x+4


def trapizoidal(lower,upper,intarval):
    h=(upper - lower)/intarval   #calculate step number
    integration = f(upper)+f(lower)   #calculate sum

    for i in range(1,intarval):
        k=lower+i*h
        integration=integration+2*f(k)

    integration=integration*h/2
    return integration





lower=float(input("Enter lower limit of integration : "))
upper=float(input("Enter upper limit of integration : "))
intarval=int(input("Enter the number of sub interval : "))

result=trapizoidal(lower,upper,intarval)
print("\nIntegration result by Trapezoidal method is : %0.6f" % result)
