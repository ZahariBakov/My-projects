from django.contrib import admin

from Puddle.conversation.models import Conversation, ConversationMessage

admin.site.register(Conversation)
admin.site.register(ConversationMessage)
