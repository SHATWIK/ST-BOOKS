from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlebooks', '0006_books_preview_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ID',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='books',
            name='preview_link',
            field=models.URLField(),
        ),
    ]
