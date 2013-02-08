from parties.models import *
from django.contrib import admin
from django.contrib.auth.models import User

class CocktailIngredientInline(admin.TabularInline):
    model = CocktailIngredient
    extra = 1

class CocktailAdmin(admin.ModelAdmin):
    inlines = (CocktailIngredientInline,)

class PartyCocktailInline(admin.TabularInline):
    model = Cocktaillist
    extra = 1

class PartyAdmin(admin.ModelAdmin):
    inlines = (PartyCocktailInline,)

class InvitationInline(admin.TabularInline):
    model = Invitation
    extra = 1

class GuestlistAdmin(admin.ModelAdmin):
    inlines = (InvitationInline,)

admin.site.register(Process)
admin.site.register(Preparation)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Style)
admin.site.register(Party, PartyAdmin)
admin.site.register(Guest)
admin.site.register(Guestlist, GuestlistAdmin)




