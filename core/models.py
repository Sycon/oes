from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # pp = models.ImageField(upload_to='/home/chimaobi/ws/Python/oes/static/globals/images',
    #                        default='/home/chimaobi/ws/Python/oes/static/globals/images/profile.jpg')
    #
    # def image_tag(self):
    #     return u'<img src="%s" />' % self.pp.url
    #
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True


class Adminlogin(models.Model):
    admname = models.CharField(primary_key=True, max_length=32)
    admpassword = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'adminlogin'


class Question(models.Model):
    testid = models.ForeignKey('Test', models.DO_NOTHING, db_column='testid')
    qnid = models.IntegerField()
    question = models.CharField(max_length=500, blank=True, null=True)
    optiona = models.CharField(max_length=100, blank=True, null=True)
    optionb = models.CharField(max_length=100, blank=True, null=True)
    optionc = models.CharField(max_length=100, blank=True, null=True)
    optiond = models.CharField(max_length=100, blank=True, null=True)
    correctanswer = models.CharField(max_length=7, blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'question'
        unique_together = (('testid', 'qnid'),)


class School(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'school'


class Student(models.Model):
    stdid = models.BigAutoField(primary_key=True)
    stdname = models.CharField(unique=True, max_length=40, blank=True, null=True)
    stdpassword = models.CharField(max_length=40, blank=True, null=True)
    emailid = models.CharField(unique=True, max_length=40, blank=True, null=True)
    contactno = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'student'


class Studentquestion(models.Model):
    stdid = models.ForeignKey(Student, models.DO_NOTHING, db_column='stdid')
    testid = models.ForeignKey(Question, models.DO_NOTHING, db_column='testid', related_name="custom_user_profile")
    qnid = models.ForeignKey(Question, models.DO_NOTHING, db_column='qnid')
    answered = models.CharField(max_length=10, blank=True, null=True)
    stdanswer = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        db_table = 'studentquestion'
        unique_together = (('stdid', 'testid', 'qnid'),)


class Studenttest(models.Model):
    stdid = models.ForeignKey(Student, models.DO_NOTHING, db_column='stdid')
    testid = models.ForeignKey('Test', models.DO_NOTHING, db_column='testid')
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    correctlyanswered = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True, choices=(('O', 'Over'), ('I', 'Inprogress')))

    class Meta:
        db_table = 'studenttest'
        unique_together = (('stdid', 'testid'),)


class Subject(models.Model):
    subid = models.IntegerField(primary_key=True)
    subname = models.CharField(unique=True, max_length=40, blank=True, null=True)
    subdesc = models.CharField(max_length=100, blank=True, null=True)
    tcid = models.ForeignKey('Testconductor', models.DO_NOTHING, db_column='tcid', blank=True, null=True)

    class Meta:
        db_table = 'subject'


class Test(models.Model):
    testid = models.BigIntegerField(primary_key=True)
    testname = models.CharField(unique=True, max_length=30)
    testdesc = models.CharField(max_length=100, blank=True, null=True)
    testdate = models.DateField(blank=True, null=True)
    testtime = models.TimeField(blank=True, null=True)
    subid = models.ForeignKey(Subject, models.DO_NOTHING, db_column='subid', blank=True, null=True)
    testfrom = models.DateTimeField()
    testto = models.DateTimeField()
    duration = models.IntegerField(blank=True, null=True)
    totalquestions = models.IntegerField(blank=True, null=True)
    attemptedstudents = models.BigIntegerField(blank=True, null=True)
    testcode = models.CharField(max_length=40)
    tcid = models.ForeignKey('Testconductor', models.DO_NOTHING, db_column='tcid', blank=True, null=True)

    class Meta:
        db_table = 'test'


class Testconductor(models.Model):
    tcid = models.BigIntegerField(primary_key=True)
    tcname = models.CharField(unique=True, max_length=40, blank=True, null=True)
    tcpassword = models.CharField(max_length=40, blank=True, null=True)
    emailid = models.CharField(unique=True, max_length=40, blank=True, null=True)
    contactno = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'testconductor'
