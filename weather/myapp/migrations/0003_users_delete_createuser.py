# Generated by Django 4.2.1 on 2023-10-06 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_createuser_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="CreateUser",
        ),
    ]
