from django.db import models

class BaseModel(models.Model):
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 


class Slider(models.Model):
    title = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    
class Navbar(BaseModel):
    logo_dark = models.ImageField(upload_to="logo/photo",verbose_name="Dark mode uchun logo ")
    logo_light = models.ImageField(upload_to="logo/photo",verbose_name="Dark mode uchun logo ")
    phone= models.CharField(max_length=13)


class Category(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to="Service/photo",   verbose_name='Servis  ikon kiriting')
   
    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    subcat_title = models.TextField(null=True, blank=True)
    subcat_title_ru = models.TextField(null=True, blank=True)
    subcat_title_en = models.TextField(null=True, blank=True)
    sub_description = models.TextField(null=True, blank=True)
    sub_description_ru = models.TextField(null=True, blank=True)
    sub_description_en = models.TextField(null=True, blank=True)
    sub_description1 = models.TextField(null=True, blank=True)
    sub_description1_ru = models.TextField(null=True, blank=True)
    sub_description1_en = models.TextField(null=True, blank=True)
    sub_photo = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting')
    sub_photo1 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    sub_photo2 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    sub_photo3 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    sub_photo4 = models.ImageField(upload_to="Service/photo", verbose_name='Portfolio rasmini kiriting',blank=True,null=True)
    subcat = models.ForeignKey(Category, verbose_name='Qaysi categoriyaga oidligini kiriting', on_delete=models.CASCADE)
    def __str__(self):
        return self.subcat_title


class Text(BaseModel):
    title = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

class About_image(BaseModel):
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="about/image1", verbose_name='About rasmini kiriting')
    image2 = models.ImageField(upload_to="about/image1", verbose_name='About rasmini kiriting')


class Porfolio(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Name')
    name_ru = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name (Russian)')
    name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name (English)')
    client_name = models.CharField(max_length=100, verbose_name='Client Name')
    client_name_ru = models.CharField(max_length=100, null=True, blank=True, verbose_name='Client Name (Russian)')
    client_name_en = models.CharField(max_length=100, null=True, blank=True, verbose_name='Client Name (English)')
    about_project = models.TextField(null=True, blank=True, verbose_name='About Project')
    about_project_ru = models.TextField(null=True, blank=True, verbose_name='About Project (Russian)')
    about_project_en = models.TextField(null=True, blank=True, verbose_name='About Project (English)')
    problems = models.TextField(null=True, blank=True, verbose_name='Problems')
    problems_ru = models.TextField(null=True, blank=True, verbose_name='Problems (Russian)')
    problems_en = models.TextField(null=True, blank=True, verbose_name='Problems (English)')
    our_solution = models.TextField(null=True, blank=True, verbose_name='Our Solution')
    our_solution_ru = models.TextField(null=True, blank=True, verbose_name='Our Solution (Russian)')
    our_solution_en = models.TextField(null=True, blank=True, verbose_name='Our Solution (English)')
    photo = models.ImageField(upload_to="portfolio/photo", verbose_name='Portfolio Photo')
    photo1 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 1', blank=True, null=True)
    photo2 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 2', blank=True, null=True)
    photo3 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 3', blank=True, null=True)
    photo4 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 4', blank=True, null=True)
    photo5 = models.ImageField(upload_to="portfolio/photo", verbose_name='Additional Photo 5', blank=True, null=True)
    category_id = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    
    def get_category_name(self):
        return self.category_id.name 

    

class Client_about(BaseModel):
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)


class Client(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="clients/photo", verbose_name='Portfolio rasmini kiriting')

    def __str__(self) -> str:
        return self.name


class Contact(BaseModel):
    description = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="contact/photo", verbose_name='Portfolio rasmini kiriting')
    image2 = models.ImageField(upload_to="contact/photo", verbose_name='Portfolio rasmini kiriting')

    def __str__(self) -> str:
        return self.description


class Social(BaseModel):
    name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Register(BaseModel):
    name = models.CharField(max_length=120)
    phone_num = models.CharField(max_length=13)
    service = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    

