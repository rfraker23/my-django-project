# Generated by Django 5.2 on 2025-04-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_opensolarbattery_proposal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opensolarproposal',
            name='online_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
