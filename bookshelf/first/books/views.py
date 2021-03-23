from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import NewBookForm, BookForm
from .models import Book, Category, Subcategory, Comment
from random import choice


def get_random_book():
    queryset_books = Book.objects.all()
    ids = list(queryset_books.values_list('id', flat=True))
    lst = []
    for _ in range(3):
        number = choice(ids)
        lst.append(queryset_books.get(id=number))
        ids.remove(number)
    return lst


class HomeBook(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all().order_by('title')
        context['subcategory'] = Subcategory.objects.all().order_by('title')
        context['books'] = get_random_book()
        return context


class ListBook(ListView):
    model = Book
    template_name = 'books/specificbooks.html'
    context_object_name = 'book'
    paginate_by = 9

    def get_queryset(self):
        return Book.objects.filter(subcategory__slug=self.kwargs['subcategory_slug']).order_by('title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = Subcategory.objects.filter(slug=self.kwargs['subcategory_slug']).order_by('title')
        return context


def get_rating(r):
    a = [i for i in r]
    lst = [i.get('rating') for i in a]
    if len(lst) == 0:
        return round(sum(lst), 1)
    return round(sum(lst) / len(lst), 1)


def get_onebook(request, book_id, book_slug, category_slug, subcategory_slug):
    book = get_object_or_404(Book, id=book_id)
    name = Book.objects.filter(id=book_id)[0]
    comments = Comment.objects.filter(book__title=name).order_by('-published')
    rating = get_rating(Comment.objects.filter(book=name).values('rating'))

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.book = book
            form.save()
            return redirect(f'/book/{category_slug}/{subcategory_slug}/{book_id}/{book_slug}/')
    else:
        form = BookForm()

    return render(request, 'books/onebook.html', {'book': book, 'form': form, 'comments': comments, 'rating': rating})


def add_new_book(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)
        if form.is_valid():
            newbook = form.save()
            return redirect(newbook)
    else:
        form = NewBookForm()
    return render(request, 'books/addbook.html', {'form': form})



# def index(request):
# """Через функцию"""
#     book = Book.objects.filter(subcategory_id=4)
#     category = Category.objects.all().order_by('title')
#     subcategory = Subcategory.objects.order_by('title')
#     context = {'category': category, 'subcategory': subcategory, 'book': book}
#     return render(request, 'books/index.html', context)

# def get_subcategory(request, subcategory_id):
#     """Через функцию"""
#     book = Book.objects.filter(subcategory_id=subcategory_id).order_by('title')
#     subcategory = Subcategory.objects.filter(pk=subcategory_id).order_by('title')
#     return render(request, 'books/specificbooks.html', {'book': book, 'subcategory': subcategory})


