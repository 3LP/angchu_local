from django.db import models

from likert_field.models import LikertField


class LikertModel(models.Model):
    test_is_the_best = LikertField()


class ParametersModel(models.Model):
    #cabbage_is_yummy = LikertField(max_value=4)
    question_1 = LikertField('Quality of Leads')
    question_2 = LikertField('Original Style')
    question_3 = LikertField('Power')
    #seven = LikertField('seven is my lucky number', max_value=7)
    #ten = LikertField('ten is the best', max_value=10)

    
