from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='ViewsModel',
        ),
    ]
