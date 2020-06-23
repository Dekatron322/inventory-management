from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Setting(models.Model):

	STATUS = (
		('True', 'True'),
		('False', 'False'),
	)
	main = RichTextUploadingField(blank=True)
	features = RichTextUploadingField(blank=True)
	aboutus = RichTextUploadingField(blank=True)
	contact = RichTextUploadingField(blank=True)
	references = RichTextUploadingField(blank=True)
	status = models.CharField(max_length=10, choices=STATUS)

	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.status


class Stock(models.Model):
	category = models.CharField(max_length=50, blank=True, null=True)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	price = models.FloatField(blank=True)
	aboutus = RichTextUploadingField(blank=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	barcode = models.IntegerField(default='0', blank=True, null=True)
	recieved_quantity = models.IntegerField(default='0', blank=True, null=True)
	sold_quantity = models.IntegerField(default='0', blank=True, null=True)
	sold_by = models.CharField(max_length=50, blank=True, null=True)
	sold_to = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	sold = models.IntegerField(default='0', blank=True, null=True)
	amount = models.IntegerField()
	total=models.FloatField()
	sub_total = models.FloatField()
	export_to_CSV = models.BooleanField(default=False)

	def __str__(self):
		return self.item_name

	@property
	def amount(self):
		return (self.quantity - self.sold_quantity)

	@property
	def total(self):
		return (self.quantity * self.price)

	@property
	def sub_total(self):
		return (self.sold_quantity * self.price) 



