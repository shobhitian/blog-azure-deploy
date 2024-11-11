# Generated by Django 3.2.20 on 2023-12-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/')),
                ('categories', models.ManyToManyField(to='techBlog.Category')),
            ],
        ),
    ]