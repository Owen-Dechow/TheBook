from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def md_safe(value):
    value = value.replace("<script>", "&lt;script&gt;").replace(
        "</script>", "&lt;/script&gt;"
    )
    return mark_safe(value)
