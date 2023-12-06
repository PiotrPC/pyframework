from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    year = models.PositiveSmallIntegerField(default=2023)
    imgThumb = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
