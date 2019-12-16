from django.contrib import admin
from django.contrib.auth.models import User,Group
from . models import Challenge,Question,Candidate,testcases,submittedcodes
# Register your models here.
# admin.site.register(Challenge)
# admin.site.register(Question)


class InLineQuestions(admin.TabularInline):
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
                  'Date'
            ),
        }),
    )
    def combine_title_slug(self,obj):
        return "{} - {}".format(obj.Title,obj.Slug)

admin.site.register(Challenge,ChallengeAdmin)

class InLineTestcases(admin.TabularInline):
    model = testcases
    extra = 0
class QuestionAdmin(admin.ModelAdmin):
    inlines = [InLineTestcases]
    list_display=('Title','Slug','Type','combine_title_slug','challenge')
    list_display_links = ('Title',
                        'Slug')
    list_filter = ('Title', 'Type',
    )
    fieldsets = (
        (None, {
            "fields": (
                  'Slug',
                  'Title',
                  'Type',
                  'Description',
                  'sample_inputs',
                  'sample_outputs',
                  'challenge',
            ),
        }),
    )
    def combine_title_slug(self,obj):
        return "{} - {}".format(obj.Title,obj.Slug)
admin.site.register(Question,QuestionAdmin)


class InLineSubmittedcodes(admin.TabularInline):
    model = submittedcodes
    extra = 0
class CandidateAdmin(admin.ModelAdmin):
    inlines = [InLineSubmittedcodes]
    list_display=(
        'fullname',
        'rollnumber',
        'test_name',
        'college',
        'branch',
        'graduation_year',
        'mobile_number',
        'total_score',
        'resume',
    )
    fieldsets = (
        (None, {
            "fields": (
                  'user',
                  'fullname',
                  'rollnumber',
                  'college',
                  'branch',
                  'graduation_year',
                  'mobile_number',
                  'test_name',
                  'total_score',
                  'resume',
                  'start_time',
                  'end_time',
                  'count',
            ),
        }),
    )
    

admin.site.register(Candidate,CandidateAdmin)

admin.site.register(submittedcodes)