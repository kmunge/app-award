from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import NewProfileForm, NewProjectForm, NewCommentForm
from .models import Profile, Projects, Comments
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfSerializer, ProjectSerializer

def home(request):
    current_user = request.user
    projects = Projects.get_projects()
    title = "projects"

    return render(request,'projects/home.html', {"title":title, "projects":projects})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.poster_id = current_user.id
            post.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_post.html', {"form": form})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def profile(request):
    current_user = request.user
    projects = Projects.objects.filter(profile = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'projects':projects,'current_user':current_user})


def search_results(request):
    if 'project' in request.GET and request.GET ["project"]:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'projects/search.html', {"message":message, "projects":searched_projects})

    else:
        message = "You haven't searched for any projects yet!"
        return render (request, 'projects/search.html', {"message": message})

def find_user(request,username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user_id = user)
    projects = Projects.objects.filter(profile_id = user)

    return render(request, 'projects/find_user.html', {'profile':profile, "projects":projects})

def review_project(request,id):
    project = Projects.objects.filter(id=id)
    current_user = request.user

    if request.method=='POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.project_id = id
            form.save()
            return redirect('review_project',id)
    else:
        form=NewCommentForm()

    try:
        user_comment=Comments.objects.filter(project_id=id)
    except Exception as e:
        raise Http404()
   
    return render(request, 'projects/review_project.html',{'project':project, 'current_user': current_user,  'form':form, 'comments':user_comment })


class ProfList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfSerializer(all_profiles,many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects,many=True)
        return Response(serializers.data)


