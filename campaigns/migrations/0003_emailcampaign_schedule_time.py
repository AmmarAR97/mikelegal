# Generated by Django 4.2.5 on 2023-09-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_alter_campaign_created_at_alter_campaign_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcampaign',
            name='schedule_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
