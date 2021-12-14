from django.db import models


class VaccineInfoKeywords(models.Model):
    keyword = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.keyword


class VaccineInfo(models.Model):
    author = models.CharField(max_length=300)
    institution = models.CharField(max_length=300)
    institution_website = models.URLField(max_length=800)
    author_phone = models.CharField(max_length=20, null=True)
    author_email = models.EmailField(max_length=254)
    date_of_research = models.DateField()
    research_title = models.CharField(max_length=800)
    research_link = models.URLField(max_length=2000)
    keywords = models.ManyToManyField(VaccineInfoKeywords)
    notes = models.TextField()

    def __str__(self):
        return self.research_title
