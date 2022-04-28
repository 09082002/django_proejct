
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import PostForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.conf import settings


def news_home(request):
    news = Post1.objects.all()
    return render(request, 'main/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Post1
    template_name = 'main/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Post1
    template_name = 'main/create.html'
    form_class = PostForm


class NewsDeleteView(DeleteView):
    model = Post1
    template_name = 'main/news-delete.html'
    success_url = '/news_home/'


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news_home')
        else:
            error = 'Форма была неверной'

    form = PostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


#
# def userinfo(request):
#     return render(request, 'main/userinfo.html')
#
#
# def userinfo(request):
#     error = ''
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/userinfo')
#         else:
#             error = 'Форма была неверной'
#
#     form = RegisterUserForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/login.html', data)


def base(request):
    return render(request, 'main/base.html')


def index(request):
    med = Medical.objects.all
    return render(request, 'main/index.html', {'medtit': med})


def about(request):
    about = Persons.objects.order_by('id')[:1]
    return render(request, 'main/about.html', {'aboutitle': about})


def home(request):
    national = National.objects.all
    return render(request, 'main/home.html', {'dishes': national})


def travel(request):
    return render(request, 'main/travel.html')


def games(request):
    return render(request, 'main/games.html')


def tours(request):
    return render(request, 'main/tours.html')


def foods(request):
    return render(request, 'main/foods.html')


def culture(request):
    return render(request, 'main/culture.html')


def register(request):
    return render(request, 'main/register.html')


# def info(request):
#     return render(request, 'main/info.html', {'info': Userinfo.objects.all() })

# def login(request):
#     return render(request, 'main/login.html')


def addpage(request):
    # form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Postusers.objects.create(**form.cleaned_data)
                return redirect('login')
            except:
                form.add_error(None, 'Мақаланы қосқанда қате шықты.')
    else:
        form = AddPostForm()

    return render(request, 'main/addpage.html', {'title': 'Мақаланы қосу', 'form': form})


# def show_post(request, post_id):
#     post = get_object_or_404(Posts1, pk=post_id)
#     context = {'post': post}
#     return render(request, 'main/post.html', context=context)


class RegisterUser(CreateView):
    form_class = AddPostForm
    template_name = 'main/register.html'
    # success_url = reverse_lazy('login')
    success_url = reverse_lazy('register_done')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title='Registration')
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_user_context(title="Login")
        return dict(list(context.items()))

    def get_user_context(self, title):
        pass

    def get_success_url(self):
        return reverse_lazy('/')


def logout_user(request):
    logout(request)
    return redirect('login')


def done(request):
    new = Postusers.objects.order_by('-id')[:1]
    return render(request, 'main/register_done.html', {'new': new})


def sends_message(request):
    email = EmailMessage(
        "Hello",
        'Body goes here',
        '200103075@stu.sdu.edu.kz',
        ['200103084@stu.sdu.edu.kz', '200103075@stu.sdu.edu.kz'],
        headers={'Message-ID': 'foo'},
    )
    email.attach_file(r'C:\Users\Asus\Desktop\myphoto.jpg')

    email.send(fail_silently=False)
    return render(request, 'main/successfull.html')

    # return render(request, 'main/successfull.html')



class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'main/susccessfull.html'

    def get(self, request):
        form = self.form_class()
        return render(request, 'main/successfull.html', {'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'main/successfull.html',
                              {'email_form': form,
                               'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'main/successfull.html',
                              {'email_form': form, 'error_message': 'Не тіркеме тым үлкен немесе бүлінген'})

        return render(request, 'main/successfull.html',
                      {'email_form': form,
                       'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})


