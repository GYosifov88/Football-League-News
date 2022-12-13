def get_article_url(request, article_id):
    return request.META['HTTP_REFERER'] + f'#article-{article_id}'
