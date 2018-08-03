from django.db import models

# Create your models here.

# Add blog model
# - title
# - body
# - createdAt
# - updatedAt
# - image
class Blog(models.Model):
  title=models.CharField(max_length=255)
  description=models.TextField()
  image = models.ImageField(upload_to='images/')
  created_at=models.DateTimeField()

# Add blog to settings
# Create a migration
# Add to Admin