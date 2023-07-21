from django.db import models

from funcs.postgres.enums import PgOrderStatusTypeEnum, PgOrderStatusTypeField, PgPaymentStatusTypeEnum, PgPaymentStatusTypeField

class Sku(models.Model):
    sku = models.CharField(primary_key=True, max_length=255, db_column='sku')
    srp = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, db_column='srp')
    last_restock = models.DateTimeField(
        blank=True, null=True, db_column='last_restock')
    last_stock_update = models.DateTimeField(
        blank=True, null=True, db_column='last_stock_update')
    last_stock_qty = models.IntegerField(db_column='last_stock_qty')
    comment = models.TextField(blank=True, null=True, db_column='comment')

    class Meta:
        managed = True
        db_table = 'sku'

class User(models.Model):
    id = models.UUIDField(primary_key=True, db_column='user_guid')
    birthday = models.DateTimeField(
        blank=True, null=True, db_column='user_birthday')
    email = models.CharField(
        unique=True, max_length=255, db_column='user_email')
    password_hash = models.CharField(max_length=64, blank=True,
                                     null=True, db_column='user_password_hash')
    password = models.CharField(
        max_length=64, blank=True, null=True, db_column='user_password')
    image_url = models.CharField(
        max_length=255, blank=True, null=True, db_column='user_image_url')
    username = models.CharField(
        max_length=200, blank=True, null=True, db_column='user_url_profile')
    display_name = models.CharField(
        max_length=200, blank=True, null=True, db_column='user_name')
    login_dt = models.DateTimeField(
        blank=True, null=True, db_column='user_login_dt')
    signup_dt = models.DateTimeField(
        blank=True, null=True, db_column='user_signup_dt')
    suspended_at = models.DateTimeField(
        blank=True, null=True, db_column='suspended_at')

    class Meta:
        managed = True
        db_table = 'user'

class Manifest(models.Model):
    id = models.UUIDField(primary_key=True, db_column='mf_id')
    shipment = models.ForeignKey(
        'Shipment', models.DO_NOTHING, blank=True, null=True, db_column='mf_shipcase_id',
        related_name='manifests')
    full_price = models.DecimalField(
        max_digits=19, decimal_places=5, blank=True, null=True, db_column='mf_full_price')
    order = models.ForeignKey('Order', models.DO_NOTHING, blank=True,
                              null=True, db_column='mf_order', related_name='manifests')
    cogs = models.DecimalField(
        max_digits=19, decimal_places=5, blank=True, null=True, db_column='mf_cogs')
    discount = models.DecimalField(
        max_digits=19, decimal_places=5, db_column='mf_discount')
    is_cancelled = models.BooleanField(db_column='mf_is_canceled')
    suspended_at = models.DateTimeField(
        blank=True, null=True, db_column='mf_suspended_dt')
    user = models.ForeignKey(
        'User', on_delete=models.DO_NOTHING, db_column='mf_user_guid')
    sku = models.ForeignKey(Sku, models.DO_NOTHING, db_column='mf_sku_id')

    class Meta:
        managed = True
        db_table = 'manifest'

class Order(models.Model):
    id = models.UUIDField(primary_key=True, db_column='order_guid')
    user = models.ForeignKey(
        'User', models.DO_NOTHING, blank=True, null=True,
        db_column='order_user', related_name='orders')
    quantity = models.IntegerField(
        blank=True, null=True, db_column='order_qty')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, db_column='order_total_price')
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, db_column='order_discount')
    credit_discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, db_column='order_credit_discount')
    tax = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, db_column='order_tax')
    created = models.DateTimeField(
        blank=True, null=True, db_column='order_timestamp')
    status = PgOrderStatusTypeField(max_length=50, choices=PgOrderStatusTypeEnum.get_django_choices(
    ), default=PgOrderStatusTypeEnum.Error, db_column='order_status')

    class Meta:
        managed = True
        db_table = 'order'