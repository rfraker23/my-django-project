from django.db import models

class OpenSolarCustomer(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class OpenSolarProject(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100, null=True, blank=True)
    customer = models.ForeignKey(OpenSolarCustomer, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class OpenSolarProposal(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    project = models.ForeignKey(OpenSolarProject, on_delete=models.CASCADE, related_name='proposals')
    title = models.CharField(max_length=255)
    pdf_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.project.name}"
