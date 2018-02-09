# Generated by Django 2.0.1 on 2018-02-09 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('keywords', models.CharField(max_length=250)),
                ('authors', models.CharField(max_length=250)),
                ('cover', models.CharField(default='https://lh3.googleusercontent.com/zqfUbCXdb1oGmsNEzNxTjQU5ZlS3x46nQoB83sFbRSlMnpDTZgdVCe_LvCx-rl7sOA=w300', max_length=1000)),
                ('copies', models.PositiveIntegerField(default=1)),
                ('type', models.CharField(default='Document', max_length=100)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_reference', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default='2018-02-09 12:56')),
                ('returning_date', models.DateTimeField(default='2018-02-09 12:56')),
                ('time_left', models.CharField(max_length=250, null=True)),
                ('level', models.PositiveIntegerField(default=1)),
                ('room', models.PositiveIntegerField(default=1)),
                ('fine_price', models.IntegerField(null=True)),
                ('checked_up_by_whom', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Document copies',
            },
        ),
        migrations.CreateModel(
            name='AVFile',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Documents.Document')),
            ],
            bases=('Documents.document',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Documents.Document')),
                ('publisher', models.CharField(blank=True, max_length=250)),
                ('edition', models.PositiveIntegerField(default=1)),
                ('publication_date', models.DateField(blank=True, max_length=250)),
            ],
            bases=('Documents.document',),
        ),
        migrations.CreateModel(
            name='JournalArticle',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Documents.Document')),
                ('publisher_journal', models.CharField(blank=True, max_length=250)),
                ('editors', models.CharField(blank=True, max_length=250)),
                ('publication_date', models.DateField(blank=True, max_length=250)),
            ],
            bases=('Documents.document',),
        ),
        migrations.AddField(
            model_name='documentcopy',
            name='doc',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Documents.Document'),
        ),
    ]
