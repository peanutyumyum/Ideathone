from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    price = models.IntegerField()
    water_period = models.TextField()
    proper_place = models.TextField()
    temperature = models.TextField()
    caution = models.TextField()
    image = image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    # name필드에 no_data 라는 데이터를 넣어서 검색결과가 없을 때 보여줄 이미지를 삽입해야함
    

class Garden(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200) # 실내 실외
    place_size = models.CharField(max_length=200) # 3~22평
    style = models.CharField(max_length=200) # 밝은 산뜻한 어두운 푸르른 청명한 아늑한
    color = models.CharField(max_length=200) # 빨강 초록 검정 회색 파랑 하늘
    size = models.CharField(max_length=200) # 손바닥사이즈 A4용지사이즈 소파사이즈
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    # 주석으로 표기한 선택지에서 선택하여 데이터 넣기