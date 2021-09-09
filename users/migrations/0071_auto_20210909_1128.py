# Generated by Django 3.2.6 on 2021-09-09 14:28

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0070_auto_20210909_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'mid'), ('jg', 'jg'), ('adc', 'adc'), ('top', 'top'), ('sup', 'sup')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'mid'), ('jg', 'jg'), ('adc', 'adc'), ('top', 'top'), ('sup', 'sup')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('O', 'Outro'), ('F', 'Feminino'), ('M', 'Masculino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'mid'), ('jg', 'jg'), ('adc', 'adc'), ('top', 'top'), ('sup', 'sup')], default=None, max_length=18),
        ),
    ]
