from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewpostForm,NewProfileForm,VoteForm
from  .models import Profile,Project
from django.http import JsonResponse
# Create your views here.
from django.http  import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from django.db.models import Max,F

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()
    return render(request,'welcome.html',{ "projects":projects})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewpostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            
            project.save()
        return redirect('welcome')

    else:
        form = NewpostForm()
    return render(request, 'new_post.html', {"form": form})
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-file/search.html',{"message":message,"projects":searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-file/search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def addprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            
            profile.save()
        return redirect('viewprofile')

    else:
        form = NewProfileForm
    return render(request, 'profile.html', {"form": form})
@login_required(login_url='/accounts/login/')
def viewprofile(request):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user).first()
    return render(request,'viewprofile.html',{'profile':profile})
def project(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)
class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
@login_required(login_url='/accounts/login/')
def rating(request,id):
    project=Project.objects.get(id=id)
    rating = round(((project.design + project.usability + project.content)/3),1)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            project.vote_submissions += 1
            if project.design == 0:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 0:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 0:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
            return redirect('welcome')
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'project':project,'rating':rating})    
