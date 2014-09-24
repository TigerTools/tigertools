# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hash'
        db.create_table(u'tigertools_hash', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyhash', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'tigertools', ['Hash'])


    def backwards(self, orm):
        # Deleting model 'Hash'
        db.delete_table(u'tigertools_hash')


    models = {
        u'tigertools.hash': {
            'Meta': {'object_name': 'Hash'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyhash': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tigertools']
