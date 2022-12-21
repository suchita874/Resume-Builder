from django.shortcuts import render
from .models import profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io 


# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        school=request.POST.get("school","")
        degree=request.POST.get("degree","")
        university=request.POST.get("university","")
        skill=request.POST.get("skill","")
        
        p=profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skill=skill,)

        p.save()
    return render(request,"accept.html")

def resume(request,id):
    user_profile=profile.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({'user_profile':user_profile})
    option = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,option)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachments'
    return response
    #return render(request,"resume.html",{'user_profile':user_profile})
def list(request):
    pr=profile.objects.all()
    return render(request,"list.html",{'profile':pr})