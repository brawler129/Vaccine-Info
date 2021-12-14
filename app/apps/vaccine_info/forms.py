from django import forms
from apps.core.models import VaccineInfoKeywords, VaccineInfo


class KeywordsField(forms.Field):

    def clean(self, value: str):
        keyword_strings = [keyword.strip().lower() for keyword in value.split(',')]
        keywords = []
        for keyword_string in keyword_strings:
            try:
                vaccine_keyword = VaccineInfoKeywords.objects.get(keyword=keyword_string)
            except VaccineInfoKeywords.DoesNotExist:
                vaccine_keyword = VaccineInfoKeywords.objects.create(keyword=keyword_string)
            keywords.append(vaccine_keyword)
        return keywords


class VaccineInfoForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={'id': 'author',
                                                           'class': 'form-control'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'id': 'institution',
                                                                'class': 'form-control'}))
    institution_website = forms.URLField(widget=forms.URLInput(
        attrs={'id': 'institution_website', 'class': 'form-control'}
        )
    )
    author_phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'author-phone',
                                                                 'class': 'form-control'}))
    author_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'id': 'author_email', 'class': 'form-control', 'type': 'email'}
        )
    )
    date_of_research = forms.DateField(widget=forms.DateInput(attrs={'id': 'date-of-research',
                                                                     'class': 'form-control',
                                                                     'type': 'date'}))
    research_title = forms.CharField(widget=forms.TextInput(attrs={'id': 'research-title',
                                                                   'class': 'form-control'}))
    research_link = forms.URLField(widget=forms.URLInput(attrs={'id': 'research_link',
                                                                'class': 'form-control'}))
    keywords = KeywordsField(widget=forms.Textarea(attrs={'id': 'keywords', 'rows': 3,
                                                          'class': 'form-control'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'id': 'notes', 'rows': 4,
                                                         'class': 'form-control'}))

    class Meta:
        model = VaccineInfo
        fields = '__all__'
