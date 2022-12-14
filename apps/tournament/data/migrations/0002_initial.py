# Generated by Django 4.0.4 on 2022-06-24 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ygo', '0001_initial'),
        ('users', '0001_initial'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='win_tournaments', to='users.player'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='managers',
            field=models.ManyToManyField(related_name='tournaments', to='users.manager', verbose_name='managers'),
        ),
        migrations.AddField(
            model_name='round',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='participant',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ygo.deck'),
        ),
        migrations.AddField(
            model_name='participant',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.player'),
        ),
        migrations.AddField(
            model_name='participant',
            name='registration_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.date', verbose_name='registration'),
        ),
        migrations.AddField(
            model_name='participant',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='tournament.tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.date', verbose_name='date'),
        ),
        migrations.AddField(
            model_name='match',
            name='player1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchs1', to='tournament.participant'),
        ),
        migrations.AddField(
            model_name='match',
            name='player2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchs2', to='tournament.participant'),
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchs', to='tournament.round'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='win_matchs', to='tournament.participant'),
        ),
    ]
