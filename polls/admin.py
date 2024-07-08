from django.contrib import admin
from .models import Question, Choice

# To register a model with default Django form representation:
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3
  
# Or to customize how the admin form looks and works, we can use the ModelAdmin class.
class QuestionAdmin(admin.ModelAdmin):
  list_display = ['question_text', 'pub_date', 'was_recently_published']
  list_filter = ['pub_date']
  search_fields = ['question_text']
  fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  

admin.site.register(Question, QuestionAdmin)
