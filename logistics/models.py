from django.db import models



class Logistics(models.Model):
    senders_name = models.CharField(max_length=300, null=True, blank=True)
    senders_phone_number = models.CharField(max_length=300, null=True, blank=True)
    senders_email = models.CharField(max_length=300, null=True, blank=True)
    pick_up_city = models.CharField(max_length=300, null=True, blank=True)
    pick_up_state = models.CharField(max_length=300, null=True, blank=True)

    receivers_name = models.CharField(max_length=300, null=True, blank=True)
    receivers_phone_number = models.CharField(max_length=300, null=True, blank=True)
    receivers_email = models.CharField(max_length=300, null=True, blank=True)
    destination_city = models.CharField(max_length=300, null=True, blank=True)
    destination_state = models.CharField(max_length=300, null=True, blank=True)

    item = models.CharField(max_length=300, null=True, blank=True)
    
    tracking_id = models.CharField(max_length=100, null=True, blank=True)
    delivery_fee = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} {} {}".format(self.senders_name, self.senders_phone_number,self.receivers_name, self.receivers_phone_number)

    class Meta:
        verbose_name_plural = "logistics"