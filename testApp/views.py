from django.shortcuts import render
import datetime

def dateinfo(request):
    date = datetime.datetime.now()
    name = 'Rajesh'
    msg=''
    h = int(date.strftime('%H'))
    if h<12:
        msg='Good Morning'
    elif h<16:
        msg='Good Afternoon'
    elif h<22:
        mag='Good Evening'
    else:
        msg='Good Night'
    my_dict ={'date':date, 'guest':name, 'msg':msg}
    return render(request, 'testApp/test.html', context=my_dict)
