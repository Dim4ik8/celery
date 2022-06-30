# Generated by Django 4.0.2 on 2022-06-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='время запуска')),
                ('status', models.CharField(choices=[('STARTED', 'started'), ('FINISHED', 'finished'), ('FAILED', 'failed')], max_length=10, verbose_name='статус задачи')),
                ('subject', models.CharField(max_length=255, verbose_name='тема рассылки')),
                ('message', models.TextField(verbose_name='текст сообщения')),
            ],
        ),
    ]
