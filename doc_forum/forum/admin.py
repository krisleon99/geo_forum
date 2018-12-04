from django.contrib import admin
from doc_forum.forum.models import Topic , Forum, ForumLike, ReplyForum

admin.site.register(Topic)
admin.site.register(Forum)
admin.site.register(ForumLike)
admin.site.register(ReplyForum)
