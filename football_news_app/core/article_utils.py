def apply_likes_count_articles(article):
    article.likes_count = article.articlelike_set.count()
    return article


def apply_user_liked_article(article):
    article.is_liked_by_user = article.likes_count > 0
    return article


def apply_likes_count_photos(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo
