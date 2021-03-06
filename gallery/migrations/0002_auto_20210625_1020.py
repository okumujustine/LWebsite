# Generated by Django 3.2.4 on 2021-06-25 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypage',
            name='internal_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='gallerypage',
            name='gallery_image',
            field=models.ForeignKey(blank=True, help_text='It will be used in the gallery listing page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
