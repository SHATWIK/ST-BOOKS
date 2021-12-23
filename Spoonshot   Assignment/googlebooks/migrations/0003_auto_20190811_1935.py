from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlebooks', '0002_auto_20190811_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
