# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Party'
        db.delete_table('parties_party')


    def backwards(self, orm):
        # Adding model 'Party'
        db.create_table('parties_party', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=48, unique=True)),
        ))
        db.send_create_signal('parties', ['Party'])


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