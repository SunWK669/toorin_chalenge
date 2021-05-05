from django.db import models

class Author(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="Name of the author"
    )

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "authors"
        ordering = ['name']

    def __str__(self):
        return self.name

class PublishingCompany(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="Name of the publishing company"
    )

    class Meta:
        db_table = "publishing_company"
        verbose_name = "Publishing Company"
        verbose_name_plural = "Publishing Companys"
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        help_text="Title of the book"
    )

    isbn = models.CharField(
        max_length=13,
        verbose_name="ISBN",
        help_text="International Standard Book Number"
    )

    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.PROTECT,
        verbose_name="Authors",
        help_text="Authors of the book"
    )

    publishing_company = models.ForeignKey(
        PublishingCompany,
        related_name="books",
        on_delete=models.PROTECT,
        verbose_name="Publishing Company",
        help_text="Publishing company of the book"
    )

    edition = models.CharField(
        max_length=150,
        verbose_name="Edition",
        help_text="Edition of the book"
    )

    number_of_pages = models.IntegerField(
        verbose_name="Number of pages",
        help_text="Number of pages of the book"
    )

    description = models.CharField(
        max_length=255,
        verbose_name="Description",
        help_text="Brief description of the book"
    )

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']

    def __str__(self):
        return self.title