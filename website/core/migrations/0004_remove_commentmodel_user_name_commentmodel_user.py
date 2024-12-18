from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_remove_blogmodel_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='user_name',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
