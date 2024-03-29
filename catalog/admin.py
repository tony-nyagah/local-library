from django.contrib import admin

from catalog.models import Author, Book, BookInstance, Genre, Language

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book
    extra: int = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra: int = 0


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
    inlines = [BookInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back", "borrower")}),
    )


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
