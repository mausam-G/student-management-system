from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django.utils.translation import gettext_lazy as _


class Tracker(models.Model):

    '''
    Base Class to track creation and updation time
    '''

    created_at = CreationDateTimeField(_('Created at'))
    updated_at = ModificationDateTimeField(_('Updated at'))

    class Meta:
        abstract = True


# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ( (1, "Teacher"), (2, "Student"))
    user_type = models.IntegerField(default=2, choices=user_type_data)

    REQUIRED_FIELDS = ['first_name']

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Teacher(Tracker):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ["-updated_at"]




class Student(Tracker):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)

    gender_choices = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    gender = models.CharField(choices=gender_choices, max_length=10)
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    reporting_teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ["-updated_at"]


class StudentResult(Tracker):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    maths_marks = models.FloatField(default=0, 
        validators=[
                MaxValueValidator(100),
                MinValueValidator(0)
        ])
    science_marks = models.FloatField(default=0,
        validators=[
                MaxValueValidator(100),
                MinValueValidator(0)
        ])
    history_marks = models.FloatField(default=0,
        validators=[
                MaxValueValidator(100),
                MinValueValidator(0)
        ])
    term_choices = ((1, "One"), (2, "Two"))
    term = models.IntegerField(default=1, choices=term_choices)

    @property
    def total_marks(self):
        return self.maths_marks + self.science_marks + self.history_marks

    def __str__(self):
        return f'{self.student} | Term: {self.term}'

    class Meta:
        verbose_name = _('Student Report')
        verbose_name_plural = _('Student Reports')
        ordering = ["-updated_at"]

    
    
