from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from ngads.utils import *
from django.shortcuts import get_object_or_404
# Create your models here.


class State(models.Model):

    STATES = [
        ('Remote', 'Remote'), ('Abuja', 'Abuja'), ('Lagos', 'Lagos'), ('Rivers', 'Rivers'), ('Oyo', 'Oyo'),
        ('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'),
        ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'),('Gombe', 'Gombe'), ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'),
        ('Plateau', 'Plateau'),  ('Sokoto', 'Sokoto'),  ('Taraba', 'Taraba'),  ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'), ('All Nigeria', 'All Nigeria')
    ]
    name = models.CharField(choices=STATES, max_length=30, null=True, blank=True, unique=True)
    priority = models.IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    headline = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='categories', blank=True, null=False)

    # def __str__(self):
    #     return self.title

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug

        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        try:
            this = Category.objects.get(id=self.id)
            if this.image != self.image:    # and this.image != 'static_media/user.png':
                this.image.delete(save=False)

            # if self.image == '':
            #     self.image = 'static_media/user.png'
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

    @property
    def short_description(self):
        return breadcrumb(str(self.description), 250)

    def get_title(self):
        title = str(self.title).lower().replace(' ', '_')
        return title

    def get_parent(self):
        return str(self.parent).lower().replace(' ', '_')


class SubCategory(models.Model):
    parent = models.ForeignKey(Category, related_name='kids', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    headline = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='subcategories', blank=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug

        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)
        verbose_name_plural = "services"

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # Format title text
        # self.title = str(self.title.title())
        super(SubCategory, self).save(*args, **kwargs)

    @property
    def short_description(self):
        return breadcrumb(str(self.description), 250)

    def get_title(self):
        title = str(self.title).lower().replace(' ', '_')
        return title

    def get_parent(self):
        return str(self.parent).lower().replace(' ', '_')


class Agent(models.Model):

    TEAM_CHOICES = [
        ('1 - 3', 'Less than 4'),
        ('4 - 10', '4 to 10'),
        ('11 - 49', '11 to 49'),
        ('50 - 100', '50 to 100'),
        ('100 - 500', '100 to 500'),
        ('500+', 'Over 500')
    ]

    MIN_PROJECT_SIZE_CHOICES = [
        ('5000', '5k'),
        ('10000', '10k'),
        ('50000', '50k'),
        ('100000', '100k'),
        ('500000', '500k'),
        ('1000000', '1m'),
        ('5000000', '5m'),
        ('10000000', '10m'),
        ('50000000', '50m'),
        ('100000000', '100m'),
    ]
    category = models.ManyToManyField(SubCategory)
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, editable=False)
    headline = models.CharField(max_length=250, null=True, blank=True)
    tags = models.CharField(max_length=250, null=True, blank=True)
    headquarters = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True)
    states = models.ManyToManyField(State, related_name='available_locations')
    date = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    promoted = models.BooleanField(default=False)
    rating = models.FloatField(max_length=5, blank=True, null=True)
    description = models.TextField(max_length=2500, blank=True, null=True)
    cover_photo = models.ImageField(upload_to='agents/cover_photos', blank=True, null=False, default="default/white.png")
    logo = models.ImageField(upload_to='agents/logos', blank=True, null=False)
    team = models.CharField(max_length=50, choices=TEAM_CHOICES, null=True, blank=True)
    min_project_size = models.CharField(max_length=50, choices=MIN_PROJECT_SIZE_CHOICES, null=True, blank=True)
    found = models.PositiveIntegerField(null=True, blank=True)
    collab = models.PositiveIntegerField(null=True, blank=True)
    team_photo = models.ImageField(upload_to='agents/team_photos', blank=True, null=False)
    languages = models.CharField(max_length=250, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    # map_location = models.MapField()
    # locations = models.ForeignKey()
    # project = models.ForeignKey()
    # awards = models.ForeignKey()
    # reviews = models.ForeignKey()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = str(self.name).lower()

        if self.cover_photo == '':
            self.cover_photo = "default/white.png"
        super(Agent, self).save(*args, **kwargs)

    def get_tags(self):
        tag_list = []
        for category in self.category.all():
            if category and category.get_title() not in tag_list:
                tag_list += [category.get_title()]
            if category.parent and category.parent.get_title() not in tag_list:
                tag_list += [category.parent.get_title()]
            if category.parent.parent and category.parent.parent.get_title() not in tag_list:
                tag_list += [category.parent.parent.get_title()]

        tags = ' '.join(tag_list)
        # print('\n\nTags:', tags)
        return tags

    def get_href_tags(self):
        tag_list = []
        for category in self.category.all():
            if category and category.get_title() not in tag_list:
                tag_list += [[category.get_title(), category.title]]
            if category.parent and category.parent.get_title() not in tag_list:
                tag_list += [[category.parent.get_title(), category.parent.title]]
            if category.parent.parent and category.parent.parent.get_title() not in tag_list:
                tag_list += [[category.parent.parent.get_title(), category.parent.parent.title]]

        # tags = ' '.join(tag_list)
        href_tags = []
        for tag in tag_list:
            if tag[1] not in href_tags:
                href_tags.append(tag[1])
            # href_tags.append(f'<a href="connect/{tag[0]}">{tag[1]}</a>')
        # print('\n\nTags:', tags)
        tags = ' | '.join(href_tags)
        return tags

    def get_service_tags(self):
        tag_list = []
        for service in self.category.all():
            tag_list.append(service.title)
        return ' | '.join(tag_list)

    def get_search_tags(self):
        search_tags = []
        tag_list = []
        for word in self.name.split():  # Search by name
            search_tags += [word]
        for word in str(self.headline).split():  # Search by headline
            search_tags += [word]
        for category in self.category.all():        # Search by categories
            if category and category.get_title() not in tag_list:        # Search by Service
                tag_list += [category.get_title().split('_')]
            if category.parent and category.parent.get_title() not in tag_list:     # Search by Subcat
                tag_list += [category.parent.get_title().split('_')]
            if category.parent.parent and category.parent.parent.get_title() not in tag_list:      # Search by category
                tag_list += [category.parent.parent.get_title().split('_')]

        for tag in tag_list:
            search_tags += tag
        filtered = []
        for tag in search_tags:
            if tag not in filtered:
                tag = tag.replace('!', '').lower()
                filtered.append(tag)

        return filtered

    def get_name(self):
        return breadcrumb(str(self.name).title(), 23)

    def get_full_name(self):
        return str(self.name).title()

    def get_headline(self):
        return breadcrumb(str(self.headline), 50)

    def get_rating_stars(self):
        rating = self.rating
        if rating == None:
            rating = 0
        mid_rating = int(rating) + 0.5
        star_box = []
        for i in range(int(rating)):
            star_box.append('bxs-star')
        for i in range(5):
            if rating >= mid_rating and 'bxs-star-half' not in star_box:
                star_box.append('bxs-star-half')
            if len(star_box) < 5:
                star_box.append('bx-star')
        return star_box


class Feature(models.Model):
    name = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name


class Plan(models.Model):

    DURATION_CHOICES = [
        ('Year', 'Annually'),
        ('Month', 'Monthly'),
    ]
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    duration = models.CharField(choices=DURATION_CHOICES, max_length=100)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name


class Pricing(models.Model):
    owner = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    plan1 = models.OneToOneField(Plan, related_name='price1', on_delete=models.PROTECT, unique=True, null=True, blank=True)
    plan2 = models.OneToOneField(Plan, related_name='price2', on_delete=models.PROTECT, unique=True, null=True, blank=True)
    plan3 = models.OneToOneField(Plan, related_name='price3', on_delete=models.PROTECT, unique=True, null=True, blank=True)

    def __str__(self):
        return self.owner


class Keyword(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
