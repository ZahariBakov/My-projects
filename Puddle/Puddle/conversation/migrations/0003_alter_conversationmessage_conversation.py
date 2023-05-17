# Generated by Django 4.2.1 on 2023-05-17 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_alter_conversation_item_alter_conversation_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='conversation.conversation'),
        ),
    ]