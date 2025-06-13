from django import template
register = template.Library()

@register.inclusion_tag('common/_pagination.html', takes_context=True)
def render_pagination(context, page_obj, adjacent=5):
    paginator = page_obj.paginator
    current = page_obj.number
    start = max(current - adjacent, 1)
    end = min(current + adjacent, paginator.num_pages)
    return {
        'page_obj': page_obj,
        'page_range': range(start, end + 1),
    }
