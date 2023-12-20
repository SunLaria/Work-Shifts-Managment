from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import time
from shift_manager.models import Worker,Shift


def home(request,week_num=datetime.datetime.now().isocalendar()[1]-1):
    today = datetime.date.today()
    startdate = time.asctime(time.strptime(f'{today.year} %d 0' % week_num, '%Y %W %w')) 
    startdate = datetime.datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')
    
    dates = [startdate.strftime('%d-%m-%Y')] 
    for i in range(1, 7): 
        day = startdate + datetime.timedelta(days=i)
        dates.append(day.strftime('%d-%m-%Y')) 
    return render(request, "shift_manager/index.html", 
                  {"week_dates":dates,
                   "week_num":week_num,
                   "workers_list":[{"Worker_ID":i.Worker_ID,"Full_Name":i.Full_Name} for i in Worker.objects.all() if len(i.shift_set.filter(Date__gte="-".join(dates[0].split("-")[::-1]), Date__lte="-".join(dates[-1].split("-")[::-1]))) < i.Work_Days]
                   })

def save(request):
    if request.method=="POST":
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
        return redirect("/")



def delete(request):
    if request.method=="POST":
        try:
            row_data_post = (list(zip(request.POST.getlist("Date"),request.POST.getlist("Shift"),request.POST.getlist("Worker"))))
            [[i.delete() for i in Shift.objects.filter(Date=x[0],Shift=x[1])] for x in row_data_post]
            return redirect("/")
        except:
            return redirect("/")
    else:
        return redirect("/")

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
            
        return redirect("workers")
    else:
        return redirect("workers")
            


def remove_worker(reuqest,worker_id):
    try:
        worker=Worker.objects.get(Worker_ID=worker_id)
        worker.delete()
        return redirect("workers")
    except:
        return redirect("workers")