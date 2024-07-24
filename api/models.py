from django.db import models
from django.utils import timezone
import uuid


class Person(models.Model):
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

    # 状態の選択肢
    STATE_CHOICES = (
        (1, 'ENTRY'),
        (2, 'EXIT')
    )

    # フルネームを格納するフィールド
    full_name = models.CharField(max_length=200, verbose_name='名前')
    # 学籍番号を格納するフィールド
    student_id = models.CharField(max_length=100, verbose_name='学籍番号')
    # 学年を格納するフィールド
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True, verbose_name='学年')
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=LAB_CHOICES, blank=True, null=True, verbose_name='研究室')
    # 状態IDを格納するフィールド
    state = models.IntegerField(choices=STATE_CHOICES, verbose_name='状態')

    def __str__(self):
        # 表示される文字列を定義
        return f"{self.full_name} ({self.student_id})"


# RoomOccupancyクラスは個人の研究室における入退室を管理します
class RoomOccupancy(models.Model):
    # 個人を参照する外部キー
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=Person.LAB_CHOICES, verbose_name='研究室')
    # 入室時間を格納するフィールド
    entry_time = models.DateTimeField()
    # 退室時間を格納するフィールド
    exit_time = models.DateTimeField(null=True)

    def __str__(self):
        # 表示される文字列を定義
        return f"{self.person} - {self.lab} ({self.entry_time} - {self.exit_time})"

# DailyOccupancySummaryクラスはdaily_occupancy_summaryビューに対応します
class DailyOccupancySummary(models.Model):
    # 個人を参照する外部キー
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 日付を格納するフィールド
    date = models.DateField()
    # 合計在室時間を格納するフィールド
    total_time = models.DurationField()

    class Meta:
        # このモデルはマネージされない（データベースビューに対応）
        managed = False
        # 対応するデータベースビュー名を指定
        db_table = 'daily_occupancy_summary'

    def __str__(self):
        return f"{self.person.full_name} - {self.date} - {self.total_time}"

# CurrentUsersInRoomクラスはcurrent_users_in_roomビューに対応します
class CurrentUsersInRoom(models.Model):
    # 個人を参照する外部キー
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=Person.LAB_CHOICES, verbose_name='研究室')
    # 入室時間を格納するフィールド
    entry_time = models.DateTimeField()

    class Meta:
        # このモデルはマネージされない（データベースビューに対応）
        managed = False
        # 対応するデータベースビュー名を指定
        db_table = 'current_users_in_room'

    def __str__(self):
        return f"{self.person.full_name} - {self.lab} - {self.entry_time}"

# RoomUtilizationReportクラスはroom_utilization_reportビューに対応します
class RoomUtilizationReport(models.Model):
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=Person.LAB_CHOICES, verbose_name='研究室')
    # 合計在室時間を格納するフィールド
    total_time = models.DurationField()

    class Meta:
        # このモデルはマネージされない（データベースビューに対応）
        managed = False
        # 対応するデータベースビュー名を指定
        db_table = 'room_utilization_report'

    def __str__(self):
        return f"{self.lab} - {self.total_time}"

# MostUsedRoomクラスはmost_used_roomビューに対応します
class MostUsedRoom(models.Model):
    # 研究室を格納するフィールド
    lab = models.CharField(max_length=100, choices=Person.LAB_CHOICES, verbose_name='研究室')
    # 合計在室時間を格納するフィールド
    total_time = models.DurationField()

    class Meta:
        # このモデルはマネージされない（データベースビューに対応）
        managed = False
        # 対応するデータベースビュー名を指定
        db_table = 'most_used_room'

    def __str__(self):
        return f"{self.lab} - {self.total_time}"

    
#活動内容入れるところ
class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    text = models.CharField(verbose_name='本文', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)
    lab = models.CharField(max_length=100)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.name
