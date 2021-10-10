from django.urls import path

from . import views
from .views import *

app_name = 'questionapp'

urlpatterns = [
    path('', init, name=''),
    path('q01', q01, name='q01'),
    path('q02', q02, name='q02'),
    path('q03', q03, name='q03'),
    path('q04', q04, name='q04'),
    path('q05', q05, name='q05'),
    path('q06', q06, name='q06'),
    path('q07', q07, name='q07'),
    path('q08', q08, name='q08'),
    path('q09', q09, name='q09'),
    path('q10', q10, name='q10'),
    path('q11', q11, name='q11'),
    path('q12', q12, name='q12'),
    path('r01', r01, name='r01'),
    path('r02', r02, name='r02'),
    path('r03', r03, name='r03'),
    path('r04', r04, name='r04'),
    path('r05', r05, name='r05'),
    path('r06', r06, name='r06'),
    path('r07', r07, name='r07'),
    path('r08', r08, name='r08'),
    path('r09', r09, name='r09'),
    path('r10', r10, name='r10'),
    path('r11', r11, name='r11'),
    path('r12', r12, name='r12'),
    path('r13', r13, name='r13'),
    path('r14', r14, name='r14'),
    path('r15', r15, name='r15'),
    path('r16', r16, name='r16'),
    path('load', load, name='load'),
    path('result', result, name='result'),
]