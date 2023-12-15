from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import time
from shift_manager.models import Worker,Shift

def home(request,week_num=datetime.datetime.now().isocalendar()[1]-1):
    
    startdate = time.asctime(time.strptime('2023 %d 0' % week_num, '%Y %W %w')) 
    startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y') 
    dates = [startdate.strftime('%d-%m-%Y')] 
    for i in range(1, 7): 
        day = startdate + datetime.timedelta(days=i)
        dates.append(day.strftime('%d-%m-%Y')) 
    return render(request, "shift_manager/index.html", {"week_dates":dates,"week_num":week_num,"workers_list":[{"Worker_ID":i.Worker_ID,"Full_Name":i.Full_Name} for i in Worker.objects.all()]})

def save(request):
    if request.method=="POST":
        row_data_post = (list(zip(request.POST.getlist("Date"),request.POST.getlist("Shift"),request.POST.getlist("Worker"))))
        [Shift.objects.create(Date=x,Shift=y,Worker=Worker.objects.get(Worker_ID=int(z))) for x,y,z in row_data_post if z != "empty"]
        return redirect("/")
    else:
        return redirect("/")

def workers(request):
    return render(request, "shift_manager/worker.html")
