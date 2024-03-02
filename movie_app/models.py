from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=30, null=True)
    movies_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=20)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='movies')
    movie = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                              blank=True, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    stars = models.IntegerField(
        verbose_name='Звезды',
        help_text='Рейтинг отзыва от 1 до 5',
        choices=[(i, i) for i in range(1, 6)],  # Ограничивает значение от 1 до 5
        default=1, )

    def __str__(self):
        return self.text
