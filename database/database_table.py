from tortoise import fields
from tortoise.models import Model


class ID_NAME(Model):
    table = 'ID_NAME'
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookID_BName(Model):
    table = 'BookID_BName'
    bookId = fields.IntField(pk=True)
    bookName = fields.CharField(max_length=255)

    def __str__(self):
        return self.bookName


class ID_BookID_Status(Model):
    statusId = fields.IntField(pk=True)
    bookId = fields.ForeignKeyField('models.BookID_BName', related_name='ID_BookID_Status')
    userId = fields.ForeignKeyField('models.ID_NAME', related_name='ID_BookID_Status')
    status = fields.BooleanField()

    class Meta:
        table = 'ID_BookID_Status'
        unique_together = (('bookId', 'userId'),)

    def __str__(self):
        return self.bookId.bookName
