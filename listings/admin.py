from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('price', 'realtor', 'list_date', 'is_published')
    list_editable = ('is_published', )
    search_fields = ('description', 'title', 'address', 'price', 'city', 'state', 'zipcode')
    list_per_page = 10


admin.site.register(Listing, ListingAdmin)


