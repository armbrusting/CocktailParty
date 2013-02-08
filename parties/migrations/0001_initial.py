# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Preparation'
        db.create_table('parties_preparation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('parties', ['Preparation'])

        # Adding model 'Process'
        db.create_table('parties_process', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('parties', ['Process'])

        # Adding model 'Category'
        db.create_table('parties_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('parties', ['Category'])

        # Adding model 'Style'
        db.create_table('parties_style', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('parties', ['Style'])

        # Adding model 'CocktailIngredient'
        db.create_table('parties_cocktailingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cocktail', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cocktail_ingredients', to=orm['parties.Cocktail'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Ingredient'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('parties', ['CocktailIngredient'])

        # Adding model 'Ingredient'
        db.create_table('parties_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=48)),
            ('preparation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Preparation'], null=True, blank=True)),
            ('process', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Process'], null=True, blank=True)),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('parties', ['Ingredient'])

        # Adding model 'Cocktail'
        db.create_table('parties_cocktail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=48)),
        ))
        db.send_create_signal('parties', ['Cocktail'])

        # Adding model 'PantryItem'
        db.create_table('parties_pantryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.ListedCocktail'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Ingredient'])),
        ))
        db.send_create_signal('parties', ['PantryItem'])

        # Adding model 'ListedCocktail'
        db.create_table('parties_listedcocktail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cocktaillist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='listed_cocktail', to=orm['parties.Cocktaillist'])),
            ('cocktail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Cocktail'])),
        ))
        db.send_create_signal('parties', ['ListedCocktail'])

        # Adding model 'Cocktaillist'
        db.create_table('parties_cocktaillist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=48)),
        ))
        db.send_create_signal('parties', ['Cocktaillist'])

        # Adding model 'Guest'
        db.create_table('parties_guest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('parties', ['Guest'])

        # Adding model 'BroughtItem'
        db.create_table('parties_broughtitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invitation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Invitation'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Ingredient'])),
        ))
        db.send_create_signal('parties', ['BroughtItem'])

        # Adding model 'Invitation'
        db.create_table('parties_invitation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guestlist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invited_guests', to=orm['parties.Guestlist'])),
            ('guest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parties.Guest'])),
        ))
        db.send_create_signal('parties', ['Invitation'])

        # Adding model 'Guestlist'
        db.create_table('parties_guestlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=48)),
        ))
        db.send_create_signal('parties', ['Guestlist'])

        # Adding model 'Party'
        db.create_table('parties_party', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=48)),
        ))
        db.send_create_signal('parties', ['Party'])


    def backwards(self, orm):
        # Deleting model 'Preparation'
        db.delete_table('parties_preparation')

        # Deleting model 'Process'
        db.delete_table('parties_process')

        # Deleting model 'Category'
        db.delete_table('parties_category')

        # Deleting model 'Style'
        db.delete_table('parties_style')

        # Deleting model 'CocktailIngredient'
        db.delete_table('parties_cocktailingredient')

        # Deleting model 'Ingredient'
        db.delete_table('parties_ingredient')

        # Deleting model 'Cocktail'
        db.delete_table('parties_cocktail')

        # Deleting model 'PantryItem'
        db.delete_table('parties_pantryitem')

        # Deleting model 'ListedCocktail'
        db.delete_table('parties_listedcocktail')

        # Deleting model 'Cocktaillist'
        db.delete_table('parties_cocktaillist')

        # Deleting model 'Guest'
        db.delete_table('parties_guest')

        # Deleting model 'BroughtItem'
        db.delete_table('parties_broughtitem')

        # Deleting model 'Invitation'
        db.delete_table('parties_invitation')

        # Deleting model 'Guestlist'
        db.delete_table('parties_guestlist')

        # Deleting model 'Party'
        db.delete_table('parties_party')


    models = {
        'parties.broughtitem': {
            'Meta': {'object_name': 'BroughtItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Ingredient']"}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Invitation']"})
        },
        'parties.category': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'parties.cocktail': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Cocktail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'cocktail_ingredients'", 'blank': 'True', 'through': "orm['parties.CocktailIngredient']", 'to': "orm['parties.Ingredient']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '48'})
        },
        'parties.cocktailingredient': {
            'Meta': {'object_name': 'CocktailIngredient'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'cocktail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cocktail_ingredients'", 'to': "orm['parties.Cocktail']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Ingredient']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'parties.cocktaillist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Cocktaillist'},
            'cocktail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'listed_cocktail'", 'blank': 'True', 'through': "orm['parties.ListedCocktail']", 'to': "orm['parties.Cocktail']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '48'})
        },
        'parties.guest': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Guest'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'parties.guestlist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Guestlist'},
            'guest': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'invited_guests'", 'blank': 'True', 'through': "orm['parties.Invitation']", 'to': "orm['parties.Guest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '48'})
        },
        'parties.ingredient': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ingredient'},
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '48'}),
            'preparation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Preparation']", 'null': 'True', 'blank': 'True'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Process']", 'null': 'True', 'blank': 'True'})
        },
        'parties.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Guest']"}),
            'guestlist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invited_guests'", 'to': "orm['parties.Guestlist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'brought_item'", 'blank': 'True', 'through': "orm['parties.BroughtItem']", 'to': "orm['parties.Ingredient']"})
        },
        'parties.listedcocktail': {
            'Meta': {'object_name': 'ListedCocktail'},
            'cocktail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Cocktail']"}),
            'cocktaillist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'listed_cocktail'", 'to': "orm['parties.Cocktaillist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'panty_item'", 'symmetrical': 'False', 'through': "orm['parties.PantryItem']", 'to': "orm['parties.Ingredient']"})
        },
        'parties.pantryitem': {
            'Meta': {'object_name': 'PantryItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.Ingredient']"}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parties.ListedCocktail']"})
        },
        'parties.party': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Party'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '48'})
        },
        'parties.preparation': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Preparation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'parties.process': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Process'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'parties.style': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['parties']