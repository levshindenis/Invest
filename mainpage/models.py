from django.db import models
from django.contrib.auth.models import User
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'


class Branch(models.Model):
    name = models.TextField(max_length=100) #отрасль

    def __str__(self):
        return self.name
class Machines(models.Model): #Станки средняя цена
    equipment_type = models.TextField(max_length=100)
    average_cost_dol = models.FloatField(max_length=100)
    avegare_price_rub = models.FloatField(max_length=100)

    def __str__(self):
        return self.equipment_type


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    organization = models.CharField(max_length=100)
    inn = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


class BusinessType(models.Model): #Аренда/строительство
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name
class company_type(models.Model): #Организационно правовая форма
    type_name = models.TextField(max_length=10)
    def __str__(self):
        return self.type_name

class Moscow_zone(models.Model):
    name = models.TextField(max_length=100)#районы Москвы
    def __str__(self):
        return self.name
class Cadastra_val_Value(models.Model): #Средняя кадастровая стоимость
    district = models.ForeignKey(Moscow_zone, on_delete=models.CASCADE) #район Москвы
    cost = models.IntegerField(max_length=100)

class Order_Varibles(models.Model): #калькулятор
    industry_type = models.ForeignKey(Branch, on_delete=models.CASCADE) #отрасль
    organisation_type = models.ForeignKey(company_type, on_delete=models.CASCADE) #ООПФ
    worker_amount = models.IntegerField(max_length=99)# количество сотрудников
    area_type = models.ForeignKey(Moscow_zone, on_delete=models.CASCADE)  #район расположения
    area_is_special_economic = models.BooleanField(default=False )
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    area_yardage = models.IntegerField(max_length=99)
    #building_yardage = models.IntegerField(max_length=99)
    need_water = models.BooleanField(default=False )
    need_gas = models.BooleanField(default=False )
    need_electricity = models.BooleanField(default=False )
    is_patent_use = models.BooleanField(default=False )
    User_create_order = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    order_create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    total_AC6=models.IntegerField(max_length=99,blank=True, null=True)
    total_AC15=models.IntegerField(max_length=99,blank=True, null=True)
    total_AC_OSN=models.IntegerField(max_length=99,blank=True, null=True)
    total_ndfl=models.IntegerField(max_length=99,blank=True, null=True)
    pfr_min=models.IntegerField(max_length=99,blank=True, null=True)
    oms_min=models.IntegerField(max_length=99,blank=True, null=True)
    pfr_max=models.IntegerField(max_length=99,blank=True, null=True)
    oms_max=models.IntegerField(max_length=99,blank=True, null=True)
    vnim_min=models.IntegerField(max_length=99,blank=True, null=True)
    vnim_max=models.IntegerField(max_length=99,blank=True, null=True)
    ndfl_min=models.IntegerField(max_length=99,blank=True, null=True)
    ndfl_max=models.IntegerField(max_length=99,blank=True, null=True)
    salary_min=models.IntegerField(max_length=99,blank=True, null=True)
    salary_max=models.IntegerField(max_length=99,blank=True, null=True)
    total_personal_min=models.IntegerField(max_length=99,blank=True, null=True)
    total_personal_max=models.IntegerField(max_length=99,blank=True, null=True)


    total_gosposhlina=models.IntegerField(max_length=99,blank=True, null=True)
    nalog_na_build=models.IntegerField(max_length=99,blank=True, null=True)
    nalog_na_zemlya=models.IntegerField(max_length=99,blank=True, null=True)
    all_nalog=models.IntegerField(max_length=99,blank=True, null=True)
    all_personal=models.IntegerField(max_length=99,blank=True, null=True)
    all_personal=models.IntegerField(max_length=99,blank=True, null=True)
    excel_link=models.CharField(max_length=99,blank=True, null=True)
    pdf_link=models.CharField(max_length=99,blank=True, null=True)
    stanki_name_1 = models.ForeignKey(Machines, default=None,blank=True, null=True, on_delete=models.CASCADE,related_name="stanki_name_1")
    stanki_name_2 = models.ForeignKey(Machines, default=None,blank=True, null=True, on_delete=models.CASCADE,related_name="stanki_name_2")
    stanki_name_3 = models.ForeignKey(Machines, default=None,blank=True, null=True, on_delete=models.CASCADE, related_name="stanki_name_3")
    stanki_name_4 = models.ForeignKey(Machines, default=None,blank=True, null=True, on_delete=models.CASCADE,related_name="stanki_name_4")
    stanki_amount_1 = models.IntegerField(blank=True, null=True)
    stanki_amount_2 = models.IntegerField(blank=True, null=True)
    stanki_amount_3 = models.IntegerField(blank=True, null=True)
    stanki_amount_4 = models.IntegerField(blank=True, null=True)
    stanki_total_sum = models.IntegerField(blank=True, null=True)
    transport_sum=models.IntegerField(blank=True, null=True)
    other_sum=models.IntegerField(blank=True, null=True)
    building_sum_min=models.IntegerField(blank=True, null=True)
    building_sum_max=models.IntegerField(blank=True, null=True)
    total_registrastion_fee=models.IntegerField(blank=True, null=True)
    total_patent_sum=models.IntegerField(blank=True, null=True)
    stanki_sum1=models.IntegerField(blank=True, null=True)
    stanki_sum2=models.IntegerField(blank=True, null=True)
    stanki_sum3=models.IntegerField(blank=True, null=True)
    stanki_sum4=models.IntegerField(blank=True, null=True)
    stanki_total_sum=models.IntegerField(blank=True, null=True)








class CostCapitalConstraction(models.Model): #Стоимость капитального строительства
    min_CostCapitalConstraction = models.IntegerField(max_length=100)
    max_CostCapitalConstraction = models.IntegerField(max_length=100)


class Accounting(models.Model): #Бухгалтерский учет
    name = models.TextField(max_length=100)
    min_osn = models.IntegerField(max_length=100)
    max_osn = models.IntegerField(max_length=100)
    min_usn = models.IntegerField(max_length=100)
    max_usn = models.IntegerField(max_length=100)
    min_patent = models.IntegerField(max_length=100)
    max_patent = models.IntegerField(max_length=100)

class StateDuty(models.Model): #Госпошлина
    name = models.TextField(max_length=100)
    cost = models.IntegerField(max_length=100)

class Industry_data(models.Model): #Обезличенные данные
    main_branch = models.CharField(max_length=100)
    sub_branch = models.CharField(max_length=100)
    average_number_staff = models.IntegerField(max_length=100)
    average_salary = models.IntegerField(max_length=100)
    taxes_to_budget = models.IntegerField(max_length=100)
    income_tax = models.IntegerField(max_length=100)
    property_tax = models.IntegerField(max_length=100)
    land_tax = models.IntegerField(max_length=1000)
    ndfl = models.IntegerField(max_length=100)
    transport_tax = models.IntegerField(max_length=100)
    other_taxes = models.IntegerField(max_length=100)

