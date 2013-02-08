from django.db import models
from django.contrib.auth.models import User


class Preparation(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "preparations"
        ordering = ('name',)

class Process(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "processes"
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ('name',)

class Style(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "styles"
        ordering = ('name',)

class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey('Cocktail', related_name='cocktail_ingredients')
    ingredient = models.ForeignKey('Ingredient')
    amount = models.IntegerField(default=1)
    order = models.IntegerField(default=1,
        help_text="Controls the order in which ingredients are displayed.")

class Ingredient(models.Model):
    name = models.CharField(max_length=48, unique=True)    
    preparation = models.ForeignKey('Preparation', null=True, blank=True)
    process = models.ForeignKey('Process', null=True, blank=True)  
    categories = models.ForeignKey(Category, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "ingredients"
        ordering = ('name',)

class Cocktail(models.Model):
    name = models.CharField(max_length=48, unique=True)
    ingredients = models.ManyToManyField('Ingredient', related_name='cocktail_ingredients', blank=True,
        through=CocktailIngredient)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class ListedCocktail(models.Model):
    cocktaillist = models.ForeignKey('Cocktaillist', related_name='listed_cocktail')
    cocktail = models.ForeignKey('Cocktail')

class Cocktaillist(models.Model):
    name = models.CharField(max_length=48, unique=True)    
    cocktail = models.ManyToManyField('Cocktail', related_name='listed_cocktail', blank=True,
            through=ListedCocktail)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class Guest(models.Model):
#    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
   
    def __unicode__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "people"
        ordering = ('last_name', 'first_name')
    
    @property
    def full_name(self):
        return '%s %s' % (
            self.first_name,
            self.last_name,
        )

class Item(models.Model):
    invitation = models.ForeignKey('Invitation', related_name='invited_items')
    ingredient = models.ForeignKey('Ingredient')

class Invitation(models.Model):
    guestlist = models.ForeignKey('Guestlist', related_name='invited_guests')
    guest = models.ForeignKey('Guest')
    item = models.ManyToManyField('Ingredient', related_name='brought_item', blank=True,
            through=Item)

class Guestlist(models.Model):
    name = models.CharField(max_length=48, unique=True)    
    guest = models.ManyToManyField('Guest', related_name='invited_guests', blank=True,
            through=Invitation)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


class Party(models.Model):
    name = models.CharField(max_length=48, unique=True)
    cocktaillist = models.ManyToManyField('Cocktaillist', blank=True,)
    guestlist = models.ForeignKey('Guestlist', blank=True,)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "parties"
        ordering = ('name',)



