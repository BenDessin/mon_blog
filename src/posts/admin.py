from django.contrib import admin

from posts.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    # indiquer ce qu'on souhaite afficher à parti de notre modèle
    list_display = ("title", "published", "created_on", "last_updated", )
    # permet d'éditer certain champs par l'interface d'admin
    list_editable = ("published", )

# dire à django qu'on souhaite afficher cette classe dans notre interface d'admin
admin.site.register(BlogPost, BlogPostAdmin)