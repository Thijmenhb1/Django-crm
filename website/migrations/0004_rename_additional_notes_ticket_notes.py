# Generated by Django 5.1.3 on 2024-12-17 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_tickets_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='additional_notes',
            new_name='notes',
        ),
    ]
