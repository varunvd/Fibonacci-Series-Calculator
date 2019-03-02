from django.shortcuts import render
from django.http import HttpResponse
import time


def index(request):
    if request.method == 'POST':
        number = request.POST['number']
        start = time.time()
        result = calculate_fib(int(number))
        end = time.time()
        return render(request, "base.html", {"result" : result, "time" : (end-start)*(10**9)})
    return render(request, "base.html")

def calculate_fib(number):
    n1 = 0
    n2 = 1
    if number <= 0:
        return 'Please provide input greater than 0'
    if number == 1:
        return n1
    for num in range(number-1):
        ans = n1 + n2
        n1=n2
        n2=ans
    return ans
