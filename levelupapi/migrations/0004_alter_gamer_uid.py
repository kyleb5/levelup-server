# Generated by Django 4.1.3 on 2023-12-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_alter_game_number_of_players_alter_game_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamer',
            name='uid',
            field=models.CharField(max_length=55, unique=True),
        ),
    ]