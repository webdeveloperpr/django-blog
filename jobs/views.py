from django.shortcuts import render
import datetime
from .models import Job

# Create your views here.
def home(req):
  jobs = Job.objects.all()
  context = {
    'year': datetime.datetime.now().year,
    'jobs': jobs,
  }
  return render(req, 'jobs/home.html', context)
