from django.db import models


class DBLogEntry(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10)
    message = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.time.strftime("%d.%B.%Y %H:%M"))+" "+str(self.level)


class GeneralLog(DBLogEntry):
    pass


class SpecialLog(DBLogEntry):
    pass
