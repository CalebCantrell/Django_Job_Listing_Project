from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Job
from .forms import JobForm, JobApplicationForm, JobSearchForm

# Create your views here.
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to the job listings page
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})

def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to the job listings page after editing

    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('job_list')  # Redirect to the job listings page after deletion

    return render(request, 'jobs/delete_job.html', {'job': job})

def job_list(request):
    job_list = Job.objects.all()

    # Number of jobs per page
    jobs_per_page = request.GET.get('jobs_per_page', 10)

    # Get the search query and category from the request
    search_query = request.GET.get('search_query', '')
    search_category = request.GET.get('search_category', 'title')

    # Filter jobs based on search query and category
    if search_query:
        if search_category == 'title':
            job_list = job_list.filter(title__icontains=search_query)
        elif search_category == 'company_name':
            job_list = job_list.filter(company_name__icontains=search_query)
        elif search_category == 'location':
            job_list = job_list.filter(location__icontains=search_query)

    paginator = Paginator(job_list, jobs_per_page)
    page = request.GET.get('page')

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'search_query': search_query, 'search_category': search_category, 'jobs_per_page': int(jobs_per_page)})

def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def application(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the form data (save to database, send email, etc.)
            # For now, you can print the form data to the console
            print(form.cleaned_data)
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/application.html', {'job': job, 'form': form})