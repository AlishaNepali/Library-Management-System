from django.contrib import admin
from . models import AuthorPenName, Student, Teacher, Author, Book

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorPenName)