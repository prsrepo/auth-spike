from django.db import models


class KRMap(models.Model):
    identifier = models.CharField(max_length=70, primary_key=True)
    workitem_ids = models.JSONField(null=True)
    is_active = models.BooleanField()
    # connection_id = models.()


class Connection(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(primary_key=True)
    is_active = models.BooleanField(default=True)
    meta_data = models.JSONField()
    type = models.CharField(default="excel365", max_length=70)
#     class Meta:
#         pass
#
#
# class Excel365Connection(Connection):
#     type = "excel365"

