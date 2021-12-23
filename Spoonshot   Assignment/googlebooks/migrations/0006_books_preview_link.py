from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlebooks', '0005_auto_20190811_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='preview_link',
            field=models.URLField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
