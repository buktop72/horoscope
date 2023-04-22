from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .data import SING_DICT, SING_DATES, SING_DICT_TYPE, PICS, SING_RUS


# Главная страница
def index(request):
    ls = list(SING_DICT)
    context = {
        'signs': ls,
        'signs_rus': SING_RUS,
    }
    return render(request, 'horoscope/index.html', context=context)


# Знаки по стихиям
def type_index(request):
    # ls = list(SING_DICT_TYPE)
    context = {
        'signs': SING_DICT_TYPE,
        'signs_rus': SING_RUS,
    }
    return render(request, 'horoscope/type.html', context=context)


def type_list(request, type):
    # ls = list(SING_DICT_TYPE)
    context = {
        'signs': SING_DICT_TYPE,
        'signs_rus': SING_RUS,
        'type': type,
    }
    return render(request, 'horoscope/type_list.html', context=context)


# Ваш знак по ДР
def your_sign(request):
    if request.method == 'POST':
        month = int(request.POST['month'])
        day = int(request.POST['day'])
        if month <= 12 and month > 0 and day <= 31 and day > 0:
            num = int((month - 1) * 30.4 + day)
            for key, value in SING_DATES.items():
                if num in value:
                    sign = key
            return HttpResponseRedirect(f'/{sign}')
        else:
            context = dict(day=day, month=month)
            return render(request, 'horoscope/404.html', context=context)

    return render(request, 'horoscope/your_sign.html')


# Описание знака зодиака
def signs(request, sign):
    context = {
        'sign': sign,
        'info': SING_DICT,
        'pic': PICS,
    }

    return render(request, 'horoscope/sign.html', context=context)
