from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, related_name="snippets", blank=True, null=True)
    description = models.TextField(null=True)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

def highlight_code(code, language):
    formatter = HtmlFormatter()
    return formatter.format(language.get_lexerbyname(language).get_tokens(code))




class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255)
    #version = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

