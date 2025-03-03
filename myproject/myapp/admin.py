from django.contrib import admin
from .models import Feature

class FeatureAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'details')

    # Add a search bar
    search_fields = ('name', 'details')

    # Add filters
    list_filter = ('name',)

    # Enable editing directly from the list view
    list_editable = ('details',)

    # Set the number of items per page
    list_per_page = 10


# Register the model with the custom admin class
admin.site.register(Feature, FeatureAdmin)