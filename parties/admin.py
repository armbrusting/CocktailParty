from parties.models import *
from django.contrib import admin
from django.contrib.auth.models import User

class CocktailIngredientInline(admin.TabularInline):
    model = CocktailIngredient
    extra = 1

class CocktailAdmin(admin.ModelAdmin):
    inlines = (CocktailIngredientInline,)

class InvitationInline(admin.TabularInline):
    model = Invitation
    extra = 1

class GuestlistAdmin(admin.ModelAdmin):
    inlines = (InvitationInline,)

class CocktailInline(admin.TabularInline):
    model = ListedCocktail
    extra = 1


class CocktaillistAdmin(admin.ModelAdmin):
    inlines = (CocktailInline,)

admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Process)
admin.site.register(Preparation)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Cocktaillist, CocktaillistAdmin)
admin.site.register(Guest)
admin.site.register(Guestlist, GuestlistAdmin)
admin.site.register(Party)





