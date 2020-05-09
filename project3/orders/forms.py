#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:46:56 2020

@author: user
"""


from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2"]


        