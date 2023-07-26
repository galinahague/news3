from django import template
from django.utils.safestring import mark_safe

register = template.Library()

FORBIDDEN_WORDS = ['редиска', 'барабан', 'ежик']

@register.filter()
def censor(value, FORBIDDEN_WORDS):
    censored_text = value

    for word in FORBIDDEN_WORDS:
        if len(word) > 1:
            replacement = word[0].lower() + '***'
            censored_text = censored_text.replace(word, replacement)

    return mark_safe(censored_text)