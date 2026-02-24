from django.db import models


# our model for the client
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    location = models.CharField(max_length=100,null=True)
    industry= models.CharField(max_length=100,null=True)
    description = models.TextField(blank=True, null=True,default="")
    # Automatically set tbe field to the current datetime when a record is first created
    created_at= models.DateTimeField(auto_now_add=True) 
    # Automatically sets the field to the current datetime every time the record is saved
    updated_at= models.DateTimeField(auto_now=True)
    website= models.URLField(null=True)
    active= models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Role(models.Model):
    name= models.CharField(max_length=50, unique=True)
    description= models.TextField(blank=True, null=True)

    created_at= models.DateTimeField(auto_now_add=True) 
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    # core fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    # Automatically set tbe field to the current datetime when a record is first created
    created_at= models.DateTimeField(auto_now_add=True) 
    # Automatically sets the field to the current datetime every time the record is saved
    updated_at= models.DateTimeField(auto_now=True)

    # Foreign key relationships
    company= models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    role= models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True, related_name='employees')
    
    def __str__(self):
        role_text = f"as a {self.role.name}" if self.role else ""
        return f"{self.first_name} {self.last_name} works at {self.company.name} {role_text}"


'''

    # date fields
    # the auto_now_add Automatically set the date when the record is created
    date_joined = models.DateField(auto_now_add=True)
    # the
    updated_at = models.DateField(auto_now=True)

'''