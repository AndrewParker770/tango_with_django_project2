from django.contrib import admin
from rango.models import Category, Page, Question, Choice
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(UserProfile)

class PageAdmin(admin.ModelAdmin):
    list_display =('title', 'category', 'url')
    
admin.site.register(Page, PageAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None,                  {'fields':['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display =('question_text', 'pub_date', 'was_published_recently')
    
admin.site.register(Question, QuestionAdmin)
