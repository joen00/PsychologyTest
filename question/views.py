from django.shortcuts import render
from .forms import *

def q01(request):
    num1 = request.GET.get('num1')
    context = {
        'num1': num1,
    }
    return render(request, 'q01.html', context)


def q02(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    context = {
        'num1': num1,
        'num2': num2
    }
    return render(request, 'q02.html', context)


def q03(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3
    }
    return render(request, 'q03.html', context)


def q04(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4
    }
    return render(request, 'q04.html', context)


def q05(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
    }
    return render(request, 'q05.html', context)


def q06(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
    }
    return render(request, 'q06.html', context)


def q07(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
    }
    return render(request, 'q07.html', context)


def q08(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
        'num8': num8,
    }
    return render(request, 'q08.html', context)


def q09(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    num9 = request.GET.get('num9')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
        'num8': num8,
        'num9': num9,
    }
    return render(request, 'q09.html', context)


def q10(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    num9 = request.GET.get('num9')
    num10 = request.GET.get('num10')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
        'num8': num8,
        'num9': num9,
        'num10': num10,
    }
    return render(request, 'q10.html', context)


def q11(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    num9 = request.GET.get('num9')
    num10 = request.GET.get('num10')
    num11 = request.GET.get('num11')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
        'num8': num8,
        'num9': num9,
        'num10': num10,
        'num11': num11,
    }
    return render(request, 'q11.html', context)


def q12(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    num9 = request.GET.get('num9')
    num10 = request.GET.get('num10')
    num11 = request.GET.get('num11')
    num12 = request.GET.get('num12')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
        'num8': num8,
        'num9': num9,
        'num10': num10,
        'num11': num11,
        'num12': num12,
    }
    return render(request, 'q12.html', context)


def result(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    num9 = request.GET.get('num9')
    num10 = request.GET.get('num10')
    num11 = request.GET.get('num11')
    num12 = request.GET.get('num12')

    arr1 = [num1, num2, num3]
    arr2 = [num4, num5, num6]
    arr3 = [num7, num8, num9]
    arr4 = [num10, num11, num12]
    m1 = 0
    m2 = 0
    b1 = 0
    b2 = 0
    t1 = 0
    t2 = 0
    i1 = 0
    i2 = 0
    for i in arr1:
        if i == "01":
            m1 = m1 + 1
        else:
            m2 = m2 + 1

    for i in arr2:
        if i == "01":
            b1 = b1 + 1
        else:
            b2 = b2 + 1

    for i in arr3:
        if i == "01":
            t1 = t1 + 1
        else:
            t2 = t2 + 1

    for i in arr4:
        if i == "01":
            i1 = i1 + 1
        else:
            i2 = i2 + 1

    if m1 > m2 and b1 > b2 and t1 > t2 and i1 > i2:
        return render(request, 'r01.html', {})
    elif m1 > m2 and b1 > b2 and t1 > t2 and i1 < i2:
        return render(request, 'r02.html', {})
    elif m1 > m2 and b1 > b2 and t1 < t2 and i1 > i2:
        return render(request, 'r03.html', {})
    elif m1 > m2 and b1 > b2 and t1 < t2 and i1 < i2:
        return render(request, 'r04.html', {})
    elif m1 > m2 and b1 < b2 and t1 > t2 and i1 > i2:
        return render(request, 'r05.html', {})
    elif m1 > m2 and b1 < b2 and t1 > t2 and i1 < i2:
        return render(request, 'r06.html', {})
    elif m1 > m2 and b1 < b2 and t1 < t2 and i1 > i2:
        return render(request, 'r07.html', {})
    elif m1 > m2 and b1 < b2 and t1 < t2 and i1 < i2:
        return render(request, 'r08.html', {})
    elif m1 < m2 and b1 > b2 and t1 > t2 and i1 > i2:
        return render(request, 'r09.html', {})
    elif m1 < m2 and b1 > b2 and t1 > t2 and i1 < i2:
        return render(request, 'r10.html', {})
    elif m1 < m2 and b1 > b2 and t1 < t2 and i1 > i2:
        return render(request, 'r11.html', {})
    elif m1 < m2 and b1 > b2 and t1 < t2 and i1 < i2:
        return render(request, 'r12.html', {})
    elif m1 < m2 and b1 < b2 and t1 > t2 and i1 > i2:
        return render(request, 'r13.html', {})
    elif m1 < m2 and b1 < b2 and t1 > t2 and i1 < i2:
        return render(request, 'r14.html', {})
    elif m1 < m2 and b1 < b2 and t1 < t2 and i1 > i2:
        return render(request, 'r15.html', {})
    elif m1 < m2 and b1 < b2 and t1 < t2 and i1 < i2:
        return render(request, 'r16.html', {})




def r01(request):
    return render(request, 'r01.html', {})


def r02(request):
    return render(request, 'r02.html', {})


def r03(request):
    return render(request, 'r03.html', {})


def r04(request):
    return render(request, 'r04.html', {})


def r05(request):
    return render(request, 'r05.html', {})


def r06(request):
    return render(request, 'r06.html', {})


def r07(request):
    return render(request, 'r07.html', {})


def r08(request):
    return render(request, 'r08.html', {})


def r09(request):
    return render(request, 'r09.html', {})


def r10(request):
    return render(request, 'r10.html', {})


def r11(request):
    return render(request, 'r11.html', {})


def r12(request):
    return render(request, 'r12.html', {})


def r13(request):
    return render(request, 'r13.html', {})


def r14(request):
    return render(request, 'r14.html', {})


def r15(request):
    return render(request, 'r15.html', {})


def r16(request):
    return render(request, 'r16.html', {})

def load(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')
    num4 = request.GET.get('num4')
    num5 = request.GET.get('num5')
    num6 = request.GET.get('num6')
    num7 = request.GET.get('num7')
    num8 = request.GET.get('num8')
    num9 = request.GET.get('num9')
    num10 = request.GET.get('num10')
    num11 = request.GET.get('num11')
    num12 = request.GET.get('num12')
    context = {
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
        'num5': num5,
        'num6': num6,
        'num7': num7,
        'num8': num8,
        'num9': num9,
        'num10': num10,
        'num11': num11,
        'num12': num12,
    }
    return render(request, 'load.html', context)

def init(request):
    return render(request, 'init.html', {})