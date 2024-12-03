from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1


class MovieMomentsInline(admin.TabularInline):
    model = Moments
    extra = 1



@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieLanguagesInline,MovieMomentsInline]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Country,Director,Actor,Genre)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Profile)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(Rating)
admin.site.register(History)