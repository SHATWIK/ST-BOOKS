from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlebooks', '0003_auto_20190811_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
