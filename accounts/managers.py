from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,username,password):
        if not username:
            raise ValueError('users must have username')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password):
        user = self.create_user(username,password)
        user.is_admin = True
        user.save(using=self._db)
        return user
