from django.db import models


class CaudexerBook(models.Model):
    isbn_13 = models.CharField(null=True, blank=True, max_length=300, unique=True)
    title = models.CharField(null=True, blank=True, max_length=300)
    authors = models.CharField(null=True, blank=True, max_length=300)
    categories = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (("isbn_13", "title", "authors"),)


class GoogleBooksData(models.Model):
    caudexer_book = models.ForeignKey(CaudexerBook)
    timestamp = models.DateField(auto_now_add=True)

    google_book_id = models.CharField(max_length=100)
    title = models.CharField(null=True, blank=True, max_length=300)
    snippet = models.TextField(null=True, blank=True)
    authors = models.CharField(null=True, blank=True, max_length=300)
    small_img = models.CharField(null=True, blank=True, max_length=300)
    img = models.CharField(null=True, blank=True, max_length=300)
    isbn_13 = models.CharField(null=True, blank=True, max_length=300)
    average_rating = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=10)
    nr_reviews = models.IntegerField(null=True, blank=True)
    language = models.CharField(null=True, blank=True, max_length=300)
    page_count = models.IntegerField(null=True, blank=True)
    publish_year = models.IntegerField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class GoodReadsData(models.Model):
    caudexer_book = models.ForeignKey(CaudexerBook)
    timestamp = models.DateField(auto_now_add=True)

    good_reads_id = models.CharField(max_length=100)
    average_rating = models.DecimalField(null=True, blank=True, decimal_places=4, max_digits=10)
    nr_reviews = models.IntegerField(null=True, blank=True)
    nr_text_reviews = models.IntegerField(null=True, blank=True)
    pub_year = models.IntegerField(null=True, blank=True)
    pub_month = models.IntegerField(null=True, blank=True)
    pub_day = models.IntegerField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=300)
    authors = models.CharField(null=True, blank=True, max_length=300)
    author_id = models.IntegerField()
    small_img = models.CharField(null=True, blank=True, max_length=300)
    img = models.CharField(null=True, blank=True, max_length=300)
