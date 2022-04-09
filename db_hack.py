from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Commendation
import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in marks:
        mark.points = 5
        mark.save()


def delete_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    Chastisements.delete()


def delete_commendations(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Commendations = Commendation.objects.filter(schoolkid=schoolkid)
    Commendations.delete()


def get_commendation():
    text = ('Молодец!',
            'Отлично!',
            'Хорошо!',
            'Гораздо лучше, чем я ожидал!',
            'Ты меня приятно удивил!',
            'Великолепно!',
            'Прекрасно!',
            'Ты меня очень обрадовал!',
            'Именно этого я давно ждал от тебя!',
            'Сказано здорово – просто и ясно!',
            'Ты, как всегда, точен!',
            'Очень хороший ответ!',
            'Талантливо!,'
            'Ты сегодня прыгнул выше головы!',
            'Я поражен!',
            'Уже существенно лучше!',
            'Потрясающе!',
            'Замечательно!',
            'Прекрасное начало!',
            'Так держать!',
            'Ты на верном пути!',
            'Здорово!',
            'Это как раз то, что нужно!',
            'Я тобой горжусь!',
            'С каждым разом у тебя получается всё лучше!',
            'Мы с тобой не зря поработали!',
            'Я вижу, как ты стараешься!',
            'Ты растешь над собой!',
            'Ты многое сделал, я это вижу!',
            'Теперь у тебя точно все получится!'
            )
    return random.choice(text)


def get_schoolkid(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except ObjectDoesNotExist:
        print("Имя должно существовать в БД.")
    except MultipleObjectsReturned:
        print("Уточните имя, запрос вернул больше одного ученика.")


def get_lessons(schoolkid, lesson_title):
    return Lesson.objects.filter(year_of_study=schoolkid.year_of_study, subject__title=title)



def add_commendation(schoolkid_name, title):
    schoolkid = get_schoolkid(schoolkid_name)
    lesson = random.choice(get_lessons(schoolkid, title))
    Commendation.objects.create(text=get_commendation(), created=lesson.date, schoolkid=schoolkid,
                                subject=lesson.subject, teacher=lesson.teacher)
