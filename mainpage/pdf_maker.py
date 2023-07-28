from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import random
import string
import os

#
# def downlaod_pdf(request: HttpRequest): #Скачать pdf
#     image_3()
#     image_4()
#     make_pdf()
#     with open('mainpage/application/pdf/result.pdf', 'rb') as f:
#         file_data = f.read()
#
#     response = HttpResponse(file_data, content_type='application/pdf')
#     response['Content-Disposition'] = "attachment; filename=Result.pdf"
#     return response
#
#
def image_3(industry_type,organisation_type,worker_amount,area_type,rashod_na_account,building_sum_min, ndfl,total_sum_personal,total_all_sum,path='/home/c/cp31594/django_gsvno/public_html/media/img/3.jpg'): #Здесь данные для 3 страницы
    im = Image.open(path)
    font = ImageFont.truetype("/home/c/cp31594/django_gsvno/public_html/media/fonts/Roboto-Regular.ttf", 64,layout_engine=ImageFont.LAYOUT_BASIC, encoding='UTF-8')
    draw_text = ImageDraw.Draw(im)

    branch = str(industry_type)
    draw_text.text((1200, 560), branch, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    org_type =str(organisation_type)
    draw_text.text((1600, 770), org_type, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    employees_count = str(worker_amount)+ " человек"
    draw_text.text((1500, 1120), employees_count, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    district =str( area_type)
    draw_text.text((1580, 1380), district, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    min_total_expenses = str(total_all_sum)
    max_total_expenses = ''
    draw_text.text((1300, 1800), "От {} руб.".format(min_total_expenses, max_total_expenses),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    employees_expenses = str(total_sum_personal)+" руб."
    draw_text.text((1500, 2190), employees_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    rent_expenses =str(building_sum_min)+" руб."
    draw_text.text((1500, 2410), rent_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    taxes_expenses = str(ndfl)+" руб."
    draw_text.text((1500, 2610), taxes_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    services_expenses = str(rashod_na_account)+" руб."
    draw_text.text((1500, 2800), services_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
    pdf_name='/home/c/cp31594/django_gsvno/public_html/media/img/'+'3_1.jpg'

    im.save(pdf_name)
    return pdf_name


def image_4(pfr_min,oms_min, pfr_max, oms_max,worker_amount,total_sum_personal,path='/home/c/cp31594/django_gsvno/public_html/media/img/4.jpg'): #Здесь данные для 4 страницы
    im = Image.open(path)
    font = ImageFont.truetype("/home/c/cp31594/django_gsvno/public_html/media/fonts/Roboto-Regular.ttf", 64,layout_engine=ImageFont.LAYOUT_BASIC, encoding='UTF-8')
    draw_text = ImageDraw.Draw(im)

    min_totals = str(total_sum_personal)
    max_totals = ''
    draw_text.text((1400, 1910), text="От {} руб.".format(min_totals, max_totals),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    employees_count = str(worker_amount)
    draw_text.text((1550, 2170), "{} человек ".format(employees_count), fill=('#1C0606'),
                   font=font, stroke_width=1, stroke_fill="black")

    min_pensionary_expenses = str(pfr_min)
    max_pensionary_expenses = str(pfr_max)
    draw_text.text((1400, 2430), "От {} до {} руб. ".format(min_pensionary_expenses, max_pensionary_expenses),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    min_health_expenses = str(oms_min)
    max_health_expenses = str(oms_max)
    draw_text.text((1400, 2700), "От {} до {} руб. ".format(min_health_expenses, max_health_expenses),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
    pdf_name ='/home/c/cp31594/django_gsvno/public_html/media/img/'+'4_1.jpg'


    im.save(pdf_name)
    return pdf_name


def make_pdf(page3,page4): #Создание pdf
    pdf = FPDF(format='A4')
    pdf.add_page()
    pdf.image('/home/c/cp31594/django_gsvno/public_html/media/img/1.jpg', x=0, y=0, w=211)
    pdf.add_page()
    pdf.image('/home/c/cp31594/django_gsvno/public_html/media/img/2.jpg', x=0, y=0, w=211)
    pdf.add_page()
    pdf.image(page3, x=0, y=0, w=211)
    pdf.add_page()
    pdf.image(page4, x=0, y=0, w=211)
    pdf.add_page()
    pdf.image('/home/c/cp31594/django_gsvno/public_html/media/img/5.jpg', x=0, y=0, w=211)

    letters = string.ascii_lowercase
    file_name_pdf = ''.join(random.choice(letters) for i in range(10))
    pdf.output("/home/c/cp31594/django_gsvno/public_html/media/pdf/"+str(file_name_pdf)+"result.pdf")
    xxx2=str(file_name_pdf)+'result.pdf'
    return xxx2
#

def make_excel(branch,org_type,personal, district, salary_fss_pfr,total_sum_personal,building_sum_min,ndfl,rashod_na_account): #Скачать excel

    #Первый лист
    branch = branch
    org_type = org_type
    employees_count =str(personal)+" человек"
    district = district
    organization_info = pd.DataFrame({'Наименование': ['Отрасль', 'Тип организации', 'Количество сотрудников',
                                                       'Район расположения производства'],
                                      'Значение': [branch, org_type, employees_count, district]})

    #Второй лист
    min_total_expenses = str(total_sum_personal)
    max_total_expenses = str(building_sum_min)
    employees_expenses = str(total_sum_personal)+"руб."
    rent_expenses =str(building_sum_min)+" руб."
    taxes_expenses =str(ndfl)+"руб."
    services_expenses =str(rashod_na_account)+" руб."
    possible_costs = pd.DataFrame(
        {'Наименование': ['Персонал', 'Аренда объектов недвижимости',
                          'Налоги', 'Услуги', 'Итого возможных расходов'],
            'Значение': [employees_expenses, rent_expenses, taxes_expenses, services_expenses,
                         "От {} до {} руб.".format(min_total_expenses, max_total_expenses)]})

    #Третий лист
    min_totals = salary_fss_pfr['6 месяцев']['Итого']
    max_totals = salary_fss_pfr['Год']['Итого']
    employees_count = personal
    min_pensionary_expenses = salary_fss_pfr['6 месяцев']['ОПС']
    max_pensionary_expenses = salary_fss_pfr['Год']['ОПС']
    min_health_expenses = salary_fss_pfr['6 месяцев']['ОМС']
    max_health_expenses = salary_fss_pfr['Год']['ОМС']
    organization_personal = pd.DataFrame(
        {'Наименование': ['Итого возможных расходов на содержание персонала организации',
                          'Планируемая численность персонала', 'Страховые взносы(пенсионное страхование)',
                          'Страховые взносы(медицинское страхование)'],
        'Значение': ["От {} до {} руб.".format(min_totals, max_totals), "{} человек ".format(employees_count),
                     "От {} до {} руб.".format(min_pensionary_expenses, max_pensionary_expenses),
                     "От {} до {} руб.".format(min_health_expenses, max_health_expenses)]})
    letters = string.ascii_lowercase
    file_name=''.join(random.choice(letters) for i in range(10))

    writer = pd.ExcelWriter('/home/c/cp31594/django_gsvno/public_html/media/'+file_name+'result.xlsx', engine='xlsxwriter')

    #Названия листов
    info_sheets = {'Информация о вашей организации': organization_info,
                   'Итоговые возможные затраты': possible_costs,
                   'Персонал организации': organization_personal}

    #Заполнение excel
    for sheetname, df in info_sheets.items():
        df.to_excel(writer, sheet_name=sheetname, index=False)
        worksheet = writer.sheets[sheetname]
        for idx, col in enumerate(df):
            series = df[col]
            max_len = max(series.astype(str).map(len).max(), len(str(series.name))) + 10
            worksheet.set_column(idx, idx, max_len)
    writer.close()
    xxx=file_name+'result.xlsx'
    return xxx

    # with open('mainpage/application/ms-excel/result.xlsx', 'rb') as f:
    #     file_data = f.read()
    # response = HttpResponse(file_data, content_type='application/ms-excel')
    # response['Content-Disposition'] = "attachment; filename=Result.xlsx"
    #
    # return response


def make_invest_pdf(industry_type,organisation_type,worker_amount,area_type, pfr_min,oms_min, pfr_max, oms_max,rashod_na_account,building_sum_min,ndfl,total_sum_personal,total_all_sum):
    page3=image_3(industry_type,organisation_type,worker_amount,area_type,rashod_na_account,building_sum_min,ndfl,total_sum_personal, total_all_sum)
    page4=image_4(pfr_min,oms_min, pfr_max, oms_max,worker_amount, total_sum_personal)
    pdfname=make_pdf(page3,page4)
    return pdfname