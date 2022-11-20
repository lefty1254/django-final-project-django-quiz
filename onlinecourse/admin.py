from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice
from nested_admin import NestedTabularInline, NestedModelAdmin

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(NestedTabularInline):
    model=Choice
    extra=4

class QuestionInline(NestedTabularInline):
    model=Question
    inlines = [ChoiceInline]
    extra=5


class LessonInline(NestedTabularInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(NestedModelAdmin):
    inlines = [LessonInline, QuestionInline,]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(NestedModelAdmin):
    inlines = [ChoiceInline]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
