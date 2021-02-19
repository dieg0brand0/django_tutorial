from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "input.html")


def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    num3 = request.POST['num3']
    num4 = request.POST['num4']

    if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit():
        a = int(num1) #vol1
        b = int(num2) #price1
        c = 1000
        d = int(num3) #vol2
        e = int(num4) #price2
        p1 = c*b/a
        p2 = c*e/d
        #res = c*b/a
        if p1 < p2:
            res = "El producto 1 es más barato con un precio de ${} pesos por Litro contra ${} del segundo producto".format(p1, p2)
        else:
            res = "El producto 2 es más barato con un precio de ${} pesos por Litro contra ${} del primer producto".format(p2, p1)
        
        return render(request, "result.html", {"result": res})
    else:
        res = "Ingresa solo números por favor"
        return render(request, "result.html", {"result": res})


def subtraction(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    num3 = request.POST['num3']
    num4 = request.POST['num4']


    if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit():
        a = int(num1) #mass1
        b = int(num2) #price1
        c = 1000
        d = int(num3) #mass2
        e = int(num4) #price2
        p1 = c*b/a
        p2 = c*e/d
        #res = c*b/a
        if p1 < p2:
            res = "El producto 1 es más barato con un precio de ${} pesos por kilo contra ${} del segundo producto".format(p1, p2)
        else:
            res = "El producto 2 es más barato con un precio de ${} pesos por kilo contra ${} del primer producto".format(p2, p1)
        
        return render(request, "result.html", {"result": res})
    else:
        res = "Ingresa solo números por favor"
        return render(request, "result.html", {"result": res})


def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a * b

        return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})



def division(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    
    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)

        if b == 0:
            res = "Zero divide error"
            return render(request, "result.html", {"result": res})
        else:
            res = a / b
            return render(request, "result.html", {"result": res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result": res})
        
