from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, UserPhotoForm, MyPasswordResetForm, ChangePasswordForm, PersonalInfoForm
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.views import PasswordResetView
from .models import Avatar
from books.models import Comment, Book


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин или пароль!')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].strip()
            if User.objects.filter(email__iexact=email).exists():
                messages.error(request, 'Пользователь с таким email уже существует')
                return render(request, 'account/register.html', {'form': form})
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Пароли не совпадают или пароль слишком легкий(мин. 8 символов)')

    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


class Reset(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    form_class = MyPasswordResetForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.filter(email__iexact=email).exists():
                return self.form_valid(form)
            else:
                messages.error(request, 'Пользователя с таким email не существует')
        return render(request, self.template_name, {'form': form})


def cabinet(request):
    user = request.user

    if request.method == 'POST' and 'btnform1' in request.POST:
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user_avatar = Avatar.objects.get(user__id=user.id)
                user_avatar.avatar = request.FILES['avatar']
                user_avatar.save()
            except Avatar.DoesNotExist:
                user_avatar = Avatar(user=user)
                user_avatar.avatar = request.FILES['avatar']
                user_avatar.save()
    else:
        form = UserPhotoForm()

    if request.method == 'POST' and 'btnform2' in request.POST:
        form2 = PersonalInfoForm(request.POST)
        if form2.is_valid():
            fn = form2.cleaned_data['firstname']
            ln = form2.cleaned_data['lastname']
            em = form2.cleaned_data['email']
            if fn != '':
                user.first_name = fn
            else:
                user.first_name = user.first_name

            if ln != '':
                user.last_name = ln
            else:
                user.last_name = user.last_name

            if em != '':
                user.email = em
            else:
                user.email = user.email
            user.save()
    else:
        form2 = PersonalInfoForm()

    try:
        img = Avatar.objects.get(user=user).avatar.url
    except:
        img = False

    user_joined = str(user.date_joined).split()[0]
    ru_format_date = user_joined[8:] + '.' + user_joined[5:7] + '.' + user_joined[:4]

    comments = Comment.objects.filter(user=user)
    books = list(set([i.book for i in comments]))

    new_books = Book.objects.all().order_by('-id')[:3]

    context = {
        'form': form,
        'form2': form2,
        'img': img,
        'books': books,
        'comments': comments[:4],
        'date_join': ru_format_date,
        'new_books': new_books,
    }

    return render(request, 'account/cabinet.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            if form.cleaned_data['new_password1'] == form.cleaned_data['new_password2']:
                user = form.save(commit=True)
                update_session_auth_hash(request, user)
                messages.success(request, 'Ваш пароль был успешно обновлен!')
        else:
            messages.error(request, 'Старый пароль введён неверно или новый пароль не совпадает!')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'account/password_change.html', {'form': form})



