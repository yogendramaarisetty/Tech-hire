from django.contrib import admin
from . models import Challenge,Question
# Register your models here.
# admin.site.register(Challenge)
# admin.site.register(Question)
class InLineQuestions(admin.StackedInline):
    model = Question
    extra = 0

class ChallengeAdmin(admin.ModelAdmin):
    inlines = [InLineQuestions]
    list_display=('Title','Slug','Duration','combine_title_slug','College')
    list_display_links = ('Title',
                        'Slug')
    list_filter = ('Title',
    )
    fieldsets = (
        (None, {
            "fields": (
                  'Slug',
                  'Title',
                  'Description',
                  'Duration',
                  'Active',
                  'College',
            ),
        }),
    )
    def combine_title_slug(self,obj):
        return "{} - {}".format(obj.Title,obj.Slug)

admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(Question)