from football_news_app.articles.models import Article, ArticleLike, ArticleComment
from football_news_app.matches.models import Match
from football_news_app.photos.models import Photo
from football_news_app.photos.models import PhotoLike
from football_news_app.players.models import Player
from football_news_app.teams.models import Team
from datetime import date


def create_teams(count=5):
    result = []
    for i in range(count):
        team = Team(
            team_name=f'Team {i+1}',
            team_logo_photo=f'http://teams.com/{i+1}',
            stadium=f'stadium {i+1}',
        )
        team.save()
        result.append(team)
    return result


def create_photo_for_user(user, count=5):
    photos = [Photo(
        photo=f'var/images/img-{i+1}.png',
        description=f'random text-{i+1}',
        location=f'random location-{i+1}',
        user=user,
    ) for i in range(count)]

    for photo in photos:
        photo.save()

    return photos


def create_photo_likes_for_user_and_photos(user, photos):
    current = 0
    total_likes_count = 0

    for photo in photos:
        for i in range(current):
            PhotoLike(
                photo=photo,
                user=user
            ).save()
            total_likes_count += 1
        current += 1
    return total_likes_count


def create_article_for_user(user, count=5):
    articles = [Article(
        author=f'random_author {i+1}',
        photo=f'var/images/img-{i+1}.png',
        description=f'random text-{i+1}',
        title=f'random title-{i+1}',
        user=user,
    ) for i in range(count)]

    for article in articles:
        article.save()

    return articles


def create_articles_likes_for_user_and_article(user, article):
    current = 0
    total_likes_count = 0
    for i in range(current):
        ArticleLike(
            article=article,
            user=user
        ).save()
        total_likes_count += 1
        current += 1
    return total_likes_count


def create_articles_comments_for_user_and_article(user, article):
    current = 0
    total_comments_count = 0
    for i in range(current):
        ArticleComment(
            text=f'random_text {i+1}',
            article=article,
            user=user
        ).save()
        total_comments_count += 1
        current += 1
    return total_comments_count


def create_match(count=5):
    teams = [Team(
                team_name=f'Team {k + 1}',
                team_logo_photo=f'http://teams.com/{k + 1}',
                stadium=f'stadium {k + 1}',
            )
        for k in range(count*2)]
    for team in teams:
        team.save()

    matches = [Match(
        home_team=teams[i],
        guest_team=teams[i+1],
        photo=f'var/images/img-{i+1}.png',
        league=f'random league-{i+1}',
        match_date=date(2015 + i, (1 + i) % 12, (1 + i) % 28),
        match_location=f'random location-{i+1}',
        league_stage=f'random league stage-{i + 1}',
    ) for i in range(count)]

    for match in matches:
        match.save()

    return matches


def create_players(count=5):
    teams = [Team(
        team_name=f'Team',
        team_logo_photo=f'http://teams.com/',
        stadium=f'stadium',
    )]
    for team in teams:
        team.save()

    players = [Player(
        first_name=f'first_name {i+1}',
        last_name=f'last_name {i+1}',
        personal_photo=f'var/images/img-{i+1}.png',
        date_of_birth=date(2015 + i, (1 + i) % 12, (1 + i) % 28),
        biography=f'random text-{i+1}',
        position=f'position-{i+1}',
        nationality=f'nationality-{i+1}',
        team=teams[0],
        assists=i+1,
        goals=i+1,
        matches=i+1,
        rating=i+1,
        team_number=i+1,

    ) for i in range(count)]

    for player in players:
        player.save()

    players.sort(key=lambda x: x.rating, reverse=True)
    players = sorted(players, key=lambda x: x.rating, reverse=True)
    return players
