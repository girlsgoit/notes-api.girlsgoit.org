# Generated by Django 2.2.3 on 2019-07-26 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField()),
                ('content', models.TextField()),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_elements', to='notes.Note')),
            ],
        ),
    ]