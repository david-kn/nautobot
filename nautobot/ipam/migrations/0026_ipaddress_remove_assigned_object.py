# Generated by Django 3.2.18 on 2023-03-07 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ipam", "0025_interface_ipaddress_m2m_data_migration"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ipaddress",
            name="assigned_object_id",
        ),
        migrations.RemoveField(
            model_name="ipaddress",
            name="assigned_object_type",
        ),
    ]
