# Generated by Django 3.0.5 on 2021-08-04 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fertilizers', '0002_auto_20210604_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('FARMER', 'FARMER'), ('AGO', 'AGO'), ('FERTILIZER_DISTRIBUTOR', 'FERTILIZER_DISTRIBUTOR'), ('MANDAL_OFFICER', 'MANDAL_OFFICER')], default='FARMER', max_length=50),
        ),
        migrations.CreateModel(
            name='FarmerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_part', models.CharField(max_length=200)),
                ('pest_image_url', models.TextField()),
                ('crop_in_acres', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
