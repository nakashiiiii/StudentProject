from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, full_name, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            #email=email,
            full_name=full_name,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, full_name, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            #email=email,
            account_id=full_name,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):

    # 学年の選択肢
    GRADE_CHOICES = (
        ('B4', 'B4'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    )
    
    # 研究室の選択肢
    LAB_CHOICES = (
        ('Serikawa Lab', '芹川研究室'),
        ('Yamawaki Lab', '山脇研究室'),
        ('Yang Lab', '楊研究室'),
        ('Zhang Lab', '張研究室'),
    )
    
    # フルネームを格納するフィールド
    full_name = models.CharField(max_length=200, verbose_name='名前')
    # 学籍番号を格納するフィールド
    student_id = models.CharField(max_length=100, verbose_name='学籍番号')
    # 学年を格納するフィールド
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True, verbose_name='学年')
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=LAB_CHOICES, blank=True, null=True, verbose_name='研究室')

    objects = UserManager()

    USERNAME_FIELD = 'full_name' # ログイン時、ユーザー名の代わりにaccount_idを使用
    #REQUIRED_FIELDS = ['email']  # スーパーユーザー作成時にemailも設定する

    def __str__(self):
        # 表示される文字列を定義
        return f"{self.full_name} ({self.student_id})"
    
"""
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def _create_user(self, email, account_id, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, account_id=account_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, account_id, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, account_id, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            account_id=account_id,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    # 学年の選択肢
    GRADE_CHOICES = (
        ('B4', 'B4'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    )
    
    # 研究室の選択肢
    LAB_CHOICES = (
        ('Serikawa Lab', '芹川研究室'),
        ('Yamawaki Lab', '山脇研究室'),
        ('Yang Lab', '楊研究室'),
        ('Zhang Lab', '張研究室'),
    )
    
    # フルネームを格納するフィールド
    full_name = models.CharField(max_length=200, verbose_name='名前')
    # 学籍番号を格納するフィールド
    student_id = models.CharField(max_length=100, verbose_name='学籍番号')
    # 学年を格納するフィールド
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True, verbose_name='学年')
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=LAB_CHOICES, blank=True, null=True, verbose_name='研究室')

    def __str__(self):
        # 表示される文字列を定義
        return f"{self.full_name} ({self.student_id})"

    account_id = models.CharField(
        verbose_name=_("account_id"),
        unique=True,
        max_length=10
    )
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_("first_name"),
        max_length=150,
        null=True,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=_("last_name"),
        max_length=150,
        null=True,
        blank=False
    )
    birth_date = models.DateField(
        verbose_name=_("birth_date"),
        blank=True,
        null=True
    )
    is_superuser = models.BooleanField(
        verbose_name=_("is_superuer"),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updateded_at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'account_id' # ログイン時、ユーザー名の代わりにaccount_idを使用
    REQUIRED_FIELDS = ['email']  # スーパーユーザー作成時にemailも設定する

    def __str__(self):
        return self.account_id
"""