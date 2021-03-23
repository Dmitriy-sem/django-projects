from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


def replace(string):
    dictionary = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',  'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'ь': '', 'ъ': '',
        'э': 'e', 'ю': 'ju', 'я': 'ja', '-': '-',
    }
    res_lst = []
    for i in string.lower():
        try:
            res_lst.append(dictionary[i])
        except KeyError:
            res_lst.append(i)

    return ''.join(res_lst[:25])


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    author = models.CharField(max_length=200, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание книги')
    rating = models.FloatField(verbose_name='Рейтинг(от 0 до 5)', blank=True, null=True)
    image = models.ImageField(upload_to='imgOfBook/%m', verbose_name='Фото', null=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT, null=True, verbose_name='Подкатегория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('onebook', kwargs={'book_id': self.pk, 'book_slug': self.slug,
                'subcategory_slug': self.subcategory.slug, 'category_slug': self.subcategory.category.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = replace(slugify(value, allow_unicode=True))
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=36)
    slug = models.SlugField(max_length=40, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = replace(slugify(value, allow_unicode=True))
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    title = models.CharField(max_length=36)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'category_slug': self.category.slug, 'subcategory_slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = replace(slugify(value, allow_unicode=True))
        super().save(*args, **kwargs)


class Comment(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT, null=True, related_name='+')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    avatar = models.OneToOneField('account.Avatar', on_delete=models.PROTECT, null=True, blank=True)
    rating = models.FloatField(verbose_name='Рейтинг(от 0 до 5)')
    content = models.TextField(verbose_name='Отзыв')
    published = models.DateField(auto_now_add=True)
