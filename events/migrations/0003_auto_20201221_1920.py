# Generated by Django 2.2.13 on 2020-12-21 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200724_1323'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventuserwishlist',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='eventuserwishlist',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='eventuserwishlist',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventuserwishlist',
            name='updated_user',
        ),
        migrations.RemoveField(
            model_name='eventuserwishlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usercoin',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='usercoin',
            name='updated_user',
        ),
        migrations.RemoveField(
            model_name='usercoin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='event',
            name='job_category',
        ),
        migrations.DeleteModel(
            name='EventJobCategoryLinking',
        ),
        migrations.DeleteModel(
            name='EventUserWishList',
        ),
        migrations.DeleteModel(
            name='JobCategory',
        ),
        migrations.DeleteModel(
            name='UserCoin',
        ),
    ]