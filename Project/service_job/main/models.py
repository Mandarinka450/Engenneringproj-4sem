from django.db import models


class Vacancies_cities(models.Model):
    id_city = models.AutoField(primary_key=True)
    name_cities = models.CharField('Название города', max_length=55)
    quantity_vacancies = models.IntegerField('Количество актуальных ваансий')
    id_vacancies = models.IntegerField('ID вакансии')
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


    def __str__(self):
        return self.name_cities


STATUS_CHOICES = [
    ('Полная занятость/гибкий график', 'Полная занятость/гибкий график'),
    ('Полная занятость/полный день', 'Полная занятость/полный день'),
    ('Полная занятость/удаленная работа', 'Полная занятость/удаленная работа'),
]

class Vacancies(models.Model):
    id_vacancies = models.ForeignKey(Vacancies_cities, on_delete=models.CASCADE)
    name_of_vacancy = models.CharField('Название вакансии', max_length=100)
    description = models.TextField('Описание вакансии')
    salary_of_mounth = models.IntegerField('Заработная плата (руб/мес)')
    graphic_of_work = models.CharField('График работы/занятость', max_length=255)
    id_company = models.IntegerField('ID компании')
    id_summary = models.IntegerField('ID резюме')
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


    def __str__(self):
       return self.name_of_vacancy



class Summary(models.Model):
     id_summary = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
     about_myself = models.TextField('Обо мне(пользователе)')
     position_worker = models.TextField('Должность')
     work_experience = models.IntegerField('Опыт работы (в годах)')
     id_user = models.IntegerField('ID пользователя')
     class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

     def __str__(self):
       return self.about_myself


AGE = [
    ('p', '21'),
    ('34', '34'),
    ('42', '42'),
]


class Users(models.Model):
    id_user = models.ForeignKey(Summary, on_delete=models.CASCADE)
    name_user = models.CharField('Имя пользователя', max_length=55)
    surname_user = models.CharField('Фамилия пользователя', max_length=255)
    email = models.EmailField('Почта')
    age = models.IntegerField('Возраст пользователя')
    date_register = models.DateField('Дата регистрации')
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
       return self.name_user


class Companies(models.Model):
    id_company = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    name_company = models.CharField('Название компании', max_length=100)
    description_company = models.TextField('Описание компании')
    rating_company = models.IntegerField('Рейтинг компании')
    id_reviews = models.IntegerField('ID отзыва')
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


    def __str__(self):
       return self.name_company


class Reviews(models.Model):
    id_reviews = models.ForeignKey(Companies, on_delete=models.CASCADE)
    name = models.CharField('Имя пользователя', max_length=55)
    surname = models.CharField('Фамилия пользователя', max_length=155)
    title = models.CharField('Заголовок отзыва', max_length=255)
    message = models.TextField('Сообщение')
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


    def __str__(self):
       return self.name

class Reviews_about_service(models.Model):
    id_review = models.AutoField(primary_key=True)
    name = models.CharField('Имя пользователя', max_length=55)
    surname = models.CharField('Фамилия пользователя', max_length=155)
    title = models.CharField('Заголовок отзыва', max_length=255)
    message = models.TextField('Сообщение')
    class Meta:
        verbose_name = "Отзыв о сервисе"
        verbose_name_plural = "Отзывы о сервисе"


    def __str__(self):
       return self.name
