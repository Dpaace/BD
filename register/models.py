from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class AddBook(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
        
    book_id = models.AutoField(auto_created=True, primary_key=True)
    b_name = models.CharField(max_length=100, blank=True)
    b_desc = models.CharField(max_length=250, blank=True)
    auther=models.CharField(max_length=100, blank=True)
    b_genre=models.CharField(max_length=100, blank=True)
    b_price=models.IntegerField(blank=True)
    b_pic= models.FileField(upload_to='books', blank=True)
    favourite =models.ManyToManyField(User, related_name='favourite', blank=True)
    New_slug=AutoSlugField(populate_from='b_name',unique=True,null=True,default=None)
    objects=models.Manager() #default manager
    newmanager= NewManager() #custom manager
    quantity = models.IntegerField(default=0, blank=True)
    status = models.BooleanField(default=False, blank=True)


    class Meta:
        db_table="addbook"

class Contact(models.Model):
    contact_id=models.AutoField(auto_created=True, primary_key=True)
    c_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    c_name=models.CharField(max_length=200, blank=True)
    c_phone=models.IntegerField()
    c_adrs=models.CharField(max_length=100, blank=True)
    c_email=models.CharField(max_length=100, blank=True)
    C_msg=models.CharField(max_length=300, blank=True)

    class Meta:
        db_table="contact"


class UserP(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    id = models.ForeignKey(User, on_delete= models.CASCADE)
    username = models.CharField(max_length=100, blank=True)
    phone_num = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    occupation=models.CharField(max_length=100, blank=True)
    customer_picture =  models.FileField(upload_to='profile', blank=True)

    class Meta:
        db_table = 'user_tbl'