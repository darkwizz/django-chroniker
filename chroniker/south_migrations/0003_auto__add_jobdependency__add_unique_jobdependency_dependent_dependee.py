# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.utils import timezone

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'JobDependency'
        db.create_table('chroniker_jobdependency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dependent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dependencies', to=orm['chroniker.Job'])),
            ('dependee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dependents', to=orm['chroniker.Job'])),
            ('wait_for_completion', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wait_for_success', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wait_for_next_run', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('chroniker', ['JobDependency'])

        # Adding unique constraint on 'JobDependency', fields ['dependent', 'dependee']
        db.create_unique('chroniker_jobdependency', ['dependent_id', 'dependee_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'JobDependency', fields ['dependent', 'dependee']
        db.delete_unique('chroniker_jobdependency', ['dependent_id', 'dependee_id'])

        # Deleting model 'JobDependency'
        db.delete_table('chroniker_jobdependency')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'timezone.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'timezone.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chroniker.job': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Job'},
            'args': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_errors_to_subscribers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_success_to_subscribers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'force_run': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'force_stop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_heartbeat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_run_successful': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lock_file': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'next_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'chroniker.jobdependency': {
            'Meta': {'unique_together': "(('dependent', 'dependee'),)", 'object_name': 'JobDependency'},
            'dependee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dependents'", 'to': "orm['chroniker.Job']"}),
            'dependent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dependencies'", 'to': "orm['chroniker.Job']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wait_for_completion': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wait_for_next_run': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wait_for_success': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'chroniker.log': {
            'Meta': {'ordering': "('-run_start_datetime',)", 'object_name': 'Log'},
            'duration_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['chroniker.Job']"}),
            'run_end_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'run_start_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'timezone.now'}),
            'stderr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stdout': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chroniker']
