# Generated by Django 4.2.5 on 2023-10-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_alter_sttmodel_audio_alter_ttsmodel_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='sttmodel',
            name='state',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Running'), (3, 'Done')], default=1),
        ),
        migrations.AddField(
            model_name='ttsmodel',
            name='state',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Running'), (3, 'Done')], default=1),
        ),
    ]
