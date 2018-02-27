from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from .models import Post
from .forms import DetailForm,LoginForm,UserRegisterForm,UserProfileEditForm
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required


def index(request):
    posts=Post.objects.last()
    return render(request,"post/index.html",context={"posts":posts})


@login_required(login_url='/index/login/')
def changing(request,id):#PostUpdate

    post=get_object_or_404(Post,id=id)
    form=DetailForm(request.POST or None,request.FILES or None,instance=post)

    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("post:list"))
    return render(request,"post/update_form.html",context={'forms':form})

def user_login(request):
    if  request.user.is_authenticated():
        return HttpResponseRedirect(reverse("post:list"))


    form=LoginForm(request.POST or None)

    if form.is_valid():
        yetkili_mi=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])
        if yetkili_mi:
            login(request,yetkili_mi)
            return HttpResponseRedirect(reverse("post:list"))

    return render(request,"post/login_form.html",context={"forms":form})


def user_profile_edit(request):#UserProfile
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("post:list"))


    form=UserProfileEditForm(request.POST or None,instance=request.user)

    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse("post:list"))

    return render(request, "post/user_profile_edit.html", context={'forms': form})


def user_register(request):
    if  request.user.is_authenticated():
        return HttpResponseRedirect(reverse("post:list"))


    form=UserRegisterForm(request.POST or None)

    if form.is_valid():
        user=form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()

        yetki_var_mi=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])

        if yetki_var_mi:
            login(request,user)
            return HttpResponseRedirect(reverse("post:list"))

    return render(request,"post/user_register.html",context={'forms':form})

def user_logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse("post:list"))


    logout(request)
    return HttpResponseRedirect(reverse("post:list"))




