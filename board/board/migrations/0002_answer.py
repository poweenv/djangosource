# Generated by Django 4.2.3 on 2023-07-27 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='수정 날짜')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.question')),
            ],
        ),
    ]
