# Generated by Django 3.2.6 on 2021-09-07 00:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0068_auto_20210906_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('adc', 'adc'), ('sup', 'sup')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('adc', 'adc'), ('sup', 'sup')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('adc', 'adc'), ('sup', 'sup')], default=None, max_length=18),
        ),
    ]
