from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email,password=None, password2=None, **extra_fields):
        
        if not email:
            raise ValueError('Users must have an email address')

        email=self.normalize_email(email)
        extra_fields.setdefault('avatar',"user.png")

        user = self.model(email=email,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None,password2=None ,**extra_fields):
        
        user = self.create_user(email,password,**extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user