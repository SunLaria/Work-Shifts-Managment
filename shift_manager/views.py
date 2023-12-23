from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import datetime
import time
from shift_manager.models import Worker,Shift
from .functions import weeks_for_year


def home(request,year=datetime.date.today().year,week_num=datetime.datetime.now().isocalendar()[1]-1):
    week_num=int(week_num)
    if week_num==0:
        week_num=weeks_for_year(year)
        year=year-1
    try:
        startdate = time.asctime(time.strptime(f'{year} %d 0' % week_num, '%Y %W %w')) 
    except:
        week_num=1
        year=year+1
        startdate = time.asctime(time.strptime(f'{year} %d 0' % week_num, '%Y %W %w')) 

    startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')
    dates = [startdate.strftime('%d-%m-%Y')] 
    for i in range(1, 7): 
        day = startdate + datetime.timedelta(days=i)
        dates.append(day.strftime('%d-%m-%Y')) 
    messages
    return render(request, "shift_manager/index.html", 
                  {"week_dates":dates,
                   "week_num":week_num,
                   "year":year,
                   "workers_list":[{"Worker_ID":i.Worker_ID,"Full_Name":i.Full_Name,"Work_Days_Left":i.Work_Days-len(i.shift_set.filter(Date__gte="-".join(dates[0].split("-")[::-1]), Date__lte="-".join(dates[-1].split("-")[::-1])))} for i in Worker.objects.all()],
                   "available_workers_list":[{"Worker_ID":i.Worker_ID,"Full_Name":i.Full_Name} for i in Worker.objects.all() if len(i.shift_set.filter(Date__gte="-".join(dates[0].split("-")[::-1]), Date__lte="-".join(dates[-1].split("-")[::-1]))) < i.Work_Days]
                   })

def save(request):
    if request.method=="POST":
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            is_ajax = True
        else:
            is_ajax = False
        row_data_post = (list(zip(request.POST.getlist("Date"),request.POST.getlist("Shift"),request.POST.getlist("Worker"))))
        for data_cell in row_data_post:
            try:
                temp_shift=Shift.objects.get(Date=data_cell[0],Shift=data_cell[1])
                if data_cell[2]!='empty':
                    temp_shift.Worker=Worker.objects.get(Worker_ID=int(data_cell[2]))
                    temp_shift.clean_fields()
                    temp_shift.save()
                else:
                    temp_shift.delete()
            except:
                if data_cell[2]!="empty" and len(Worker.objects.get(Worker_ID=int(data_cell[2])).shift_set.filter(Date__gte=row_data_post[0][0], Date__lte=row_data_post[-1][0])) < Worker.objects.get(Worker_ID=int(data_cell[2])).Work_Days:
                    Shift.objects.create(Date=data_cell[0],Shift=data_cell[1],Worker=Worker.objects.get(Worker_ID=int(data_cell[2])))
        messages.success(request, "Shifts Updated!.")
        return redirect(request.META.get('HTTP_REFERER'))



def delete(request):
    if request.method=="POST":
        try:
            row_data_post = (list(zip(request.POST.getlist("Date"),request.POST.getlist("Shift"),request.POST.getlist("Worker"))))
            [[i.delete() for i in Shift.objects.filter(Date=x[0],Shift=x[1])] for x in row_data_post]
            messages.success(request, "Shifts Deleted!.")
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(redirect("/"))

def workers(request):
    return render(request, "shift_manager/worker.html", {"workers":[i for i in Worker.objects.all()]})


def save_worker(request):
    if request.method=="POST":
        try:
            worker=Worker.objects.get(Worker_ID=request.POST["worker_id"])
            worker.Full_Name=request.POST["full_name"]
            worker.Work_Days=request.POST["work_days"]
            worker.clean_fields()
            worker.save()
        except:
            worker=Worker(Worker_ID=request.POST["worker_id"],Full_Name=request.POST["full_name"],Work_Days=request.POST["work_days"])
            try:
                worker.clean_fields()
                worker.save()
            except:
                pass
        messages.success(request, "Worker Saved!.")
        return redirect("workers")
    else:
        return redirect("workers")
            


def remove_worker(request,worker_id):
    try:
        worker=Worker.objects.get(Worker_ID=worker_id)
        worker.delete()
        messages.success(request, "Worker Removed!.")
        return redirect("workers")
    except:
        return redirect("workers")