# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DrugFormulation'
        db.create_table(u'bigpharma_drugformulation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('units', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('drug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Drug'])),
            ('custom_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'bigpharma', ['DrugFormulation'])

        # Adding model 'Practitioner'
        db.create_table(u'bigpharma_practitioner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bigpharma', ['Practitioner'])

        # Adding model 'SuppliedFromPharmacist'
        db.create_table(u'bigpharma_suppliedfrompharmacist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('formulation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigpharma.DrugFormulation'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('cancelled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pharmacist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('authorising_practitioner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='authorised_supplies', to=orm['bigpharma.Practitioner'])),
            ('receiving_practitioner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='received_supplies', null=True, to=orm['bigpharma.Practitioner'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opal.Patient'], null=True, blank=True)),
        ))
        db.send_create_signal(u'bigpharma', ['SuppliedFromPharmacist'])

        # Adding model 'ReceivedByPharmacist'
        db.create_table(u'bigpharma_receivedbypharmacist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('formulation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigpharma.DrugFormulation'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('cancelled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pharmacist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigpharma.Supplier'])),
        ))
        db.send_create_signal(u'bigpharma', ['ReceivedByPharmacist'])

        # Adding model 'AdhocAdjustment'
        db.create_table(u'bigpharma_adhocadjustment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('formulation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bigpharma.DrugFormulation'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('cancelled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pharmacist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('reason_for_error', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'bigpharma', ['AdhocAdjustment'])

        # Adding model 'Supplier'
        db.create_table(u'bigpharma_supplier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bigpharma', ['Supplier'])


    def backwards(self, orm):
        # Deleting model 'DrugFormulation'
        db.delete_table(u'bigpharma_drugformulation')

        # Deleting model 'Practitioner'
        db.delete_table(u'bigpharma_practitioner')

        # Deleting model 'SuppliedFromPharmacist'
        db.delete_table(u'bigpharma_suppliedfrompharmacist')

        # Deleting model 'ReceivedByPharmacist'
        db.delete_table(u'bigpharma_receivedbypharmacist')

        # Deleting model 'AdhocAdjustment'
        db.delete_table(u'bigpharma_adhocadjustment')

        # Deleting model 'Supplier'
        db.delete_table(u'bigpharma_supplier')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'bigpharma.adhocadjustment': {
            'Meta': {'object_name': 'AdhocAdjustment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'formulation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bigpharma.DrugFormulation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pharmacist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'reason_for_error': ('django.db.models.fields.TextField', [], {})
        },
        u'bigpharma.allergies': {
            'Meta': {'object_name': 'Allergies'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'drug_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Drug']", 'null': 'True', 'blank': 'True'}),
            'drug_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']"}),
            'provisional': ('django.db.models.fields.BooleanField', [], {})
        },
        u'bigpharma.antimicrobial': {
            'Meta': {'object_name': 'Antimicrobial'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'dose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'drug_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Drug']", 'null': 'True', 'blank': 'True'}),
            'drug_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            'frequency_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Drugfreq']", 'null': 'True', 'blank': 'True'}),
            'frequency_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Drugroute']", 'null': 'True', 'blank': 'True'}),
            'route_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'bigpharma.demographics': {
            'Meta': {'object_name': 'Demographics'},
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'country_of_birth_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Destination']", 'null': 'True', 'blank': 'True'}),
            'country_of_birth_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hospital_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nhs_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']"})
        },
        u'bigpharma.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'condition_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Condition']", 'null': 'True', 'blank': 'True'}),
            'condition_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_diagnosis': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provisional': ('django.db.models.fields.BooleanField', [], {})
        },
        u'bigpharma.drugformulation': {
            'Meta': {'object_name': 'DrugFormulation'},
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'custom_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'drug': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Drug']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'units': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bigpharma.investigation': {
            'Meta': {'object_name': 'Investigation'},
            'adenovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'anti_hbcore_igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'anti_hbcore_igm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'anti_hbs': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'c_difficile_antigen': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'c_difficile_toxin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'cmv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cryptosporidium': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date_ordered': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ebna_igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ebv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'entamoeba_histolytica': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'enterovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            'giardia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hbsag': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hsv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hsv_1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hsv_2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'igm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'influenza_a': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'influenza_b': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'metapneumovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'microscopy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'norovirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parainfluenza': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'parasitaemia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'resistant_antibiotics': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rotavirus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rpr': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'rsv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'sensitive_antibiotics': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'species': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'syphilis': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tppa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'vca_igg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'vca_igm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'viral_load': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'vzv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'bigpharma.location': {
            'Meta': {'object_name': 'Location'},
            'bed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            'hospital': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'bigpharma.pastmedicalhistory': {
            'Meta': {'object_name': 'PastMedicalHistory'},
            'condition_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Condition']", 'null': 'True', 'blank': 'True'}),
            'condition_ft': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Episode']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'bigpharma.practitioner': {
            'Meta': {'object_name': 'Practitioner'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bigpharma.receivedbypharmacist': {
            'Meta': {'object_name': 'ReceivedByPharmacist'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'formulation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bigpharma.DrugFormulation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pharmacist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bigpharma.Supplier']"})
        },
        u'bigpharma.suppliedfrompharmacist': {
            'Meta': {'object_name': 'SuppliedFromPharmacist'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'authorising_practitioner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authorised_supplies'", 'to': u"orm['bigpharma.Practitioner']"}),
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'formulation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bigpharma.DrugFormulation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']", 'null': 'True', 'blank': 'True'}),
            'pharmacist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'receiving_practitioner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'received_supplies'", 'null': 'True', 'to': u"orm['bigpharma.Practitioner']"})
        },
        u'bigpharma.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'opal.condition': {
            'Meta': {'ordering': "['name']", 'object_name': 'Condition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.destination': {
            'Meta': {'ordering': "['name']", 'object_name': 'Destination'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.drug': {
            'Meta': {'ordering': "['name']", 'object_name': 'Drug'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.drugfreq': {
            'Meta': {'ordering': "['name']", 'object_name': 'Drugfreq'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.drugroute': {
            'Meta': {'ordering': "['name']", 'object_name': 'Drugroute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'opal.episode': {
            'Meta': {'object_name': 'Episode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'inpatient'", 'max_length': '200'}),
            'consistency_token': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_episode': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discharge_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['opal.Patient']"})
        },
        u'opal.patient': {
            'Meta': {'object_name': 'Patient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bigpharma']