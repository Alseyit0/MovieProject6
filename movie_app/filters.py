from django_filters import FilterSet, DateFilter, CharFilter
from .models import Movie

class MovieFilter(FilterSet):
    year = DateFilter(field_name="year", lookup_expr="year")
    genre = CharFilter(field_name="genre__genre_name", lookup_expr="icontains")
    class Meta:
        model = Movie
        fields = ['year', 'genre', 'status_movie']
