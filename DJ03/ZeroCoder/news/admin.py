from django.contrib import admin


from .models import News_post


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        # Если новость создается впервые, или поле author не установлено
        if not change or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(News_post, NewsPostAdmin)