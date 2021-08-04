from leads.forms import LeadModelForm,CustomUserCreationForm
from django.views.generic import( TemplateView,DetailView,ListView,CreateView,UpdateView,DeleteView)
from django.shortcuts import redirect, render,reverse
from .models import Leads
from django.core.mail import send_mail

class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name="landing.html"

def landing_page(request):
    return render(request,"landing.html")

class LeadListView(ListView):
    template_name="leads/lead_list.html"
    queryset=Leads.objects.all()
    context_object_name="leads"

def lead_list(request):
    leads=Leads.objects.all()
    context={
        "leads":leads
    }
    return render(request,"leads/lead_list.html",context)

class LeadCreateView(CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead_list")
    def form_valid(self,form):
        #####
        send_mail(
            subject="lead has been created ",
        message=" go to the site to see the new lead",
        from_email="test@test.com",
        recipient_list=["test1@test.com"]
        )

        return super(LeadCreateView,self).form_valid(form)
            

def lead_create(request):
    form =LeadModelForm()
    if request.method=="POST":
        print("reciving post request")
        form =LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context={
        "form" : form
    }
    return render(request,"leads/lead_create.html",context)

class LeadUpdateView(UpdateView):
    template_name="leads/lead_update.html"
    queryset=Leads.objects.all()
    form_class=LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead_list")

def lead_update(request,pk):
    leads=Leads.objects.get(id=pk)
    form =LeadModelForm(instance=leads)
    if request.method=="POST":
        print("reciving post request")
        form =LeadModelForm(request.POST,instance=leads)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context={
        "lead":leads,
        "form":form
    }
    return render(request,"leads/lead_update.html",context)

class LeadDetailView(DetailView):
    template_name="leads/lead_detail.html"
    queryset=Leads.objects.all()
    context_object_name="leads"

def lead_detail(request,pk):
    leads=Leads.objects.get(id=pk)
    context={
        "leads":leads
    }
    return render(request,"leads/lead_detail.html",context)

class LeadDeleteView(DeleteView):
    template_name="leads/lead_delete.html"
    queryset=Leads.objects.all()
    def get_success_url(self):
        return reverse("leads:lead_list")

def lead_delete(request,pk):
    leads=Leads.objects.get(id=pk)
    leads.delete()
    return redirect("/leads")

