from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_blogmodel_title_delete_viewsmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='likes',
        ),
    ]
