from django.db import models

class loginpage(models.Model):
    Email = models.EmailField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.Email
    
    class Meta:
        verbose_name = 'log in page'
        ordering = ['Email']

class profil(models.Model):
    gen = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    fname = models.CharField(max_length= 15)
    lname = models.CharField(max_length= 15)
    Email = models.EmailField()
    Password = models.CharField(max_length=20) 
    gender = models.CharField(max_length=20, choices=gen)


    def __str__(self):
        return self.fname
    
    class Meta:
        verbose_name = 'Profile'
        ordering = ['fname']
    


