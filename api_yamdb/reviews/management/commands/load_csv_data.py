import csv

from django.core.management import BaseCommand

from reviews.models import Comments, Review
from titles.models import Category, Genre, Title
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwarg):
        self.stdout.write(self.style.SUCCESS("Загружаем данные Category"))
        with open("static/data/category.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                Category(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                ).save()
                n += 1
                print(f"done {n}")

        self.stdout.write(self.style.SUCCESS("Загружаем данные Genre"))
        with open("static/data/genre.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                Genre(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                ).save()
                n += 1
                print(f"done {n}")

        self.stdout.write(self.style.SUCCESS("Загружаем данные Title"))
        with open("static/data/titles.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                category = Category.objects.get(id=row[3])
                Title(
                    id=row[0], name=row[1], year=row[2], category=category
                ).save()
                n += 1
                print(f"done {n}")

        self.stdout.write(self.style.SUCCESS("Загружаем данные GenreTitle"))
        with open("static/data/genre_title.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                title_id = Title.objects.get(id=row[1])
                genre_id = Genre.objects.get(id=row[2])
                genre_id.titles.add(title_id)
                n += 1
                print(f"done {n}")

        self.stdout.write(self.style.SUCCESS("Загружаем данные User"))
        with open("static/data/users.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                User(
                    id=row[0],
                    username=row[1],
                    first_name=row[5],
                    last_name=row[6],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                ).save()
                n += 1
                print(f"done {n}")

        self.stdout.write(self.style.SUCCESS("Загружаем данные Review"))
        with open("static/data/review.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                title = Title.objects.get(id=row[1])
                author = User.objects.get(id=row[3])
                Review(
                    id=row[0],
                    author=author,
                    title_id=title.id,
                    text=row[2],
                    score=row[4],
                    pub_date=row[5],
                ).save()
                n += 1
                print(f"done {n}")

        self.stdout.write(self.style.SUCCESS("Загружаем данные Comments"))
        with open("static/data/comments.csv", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            n = 0
            for row in reader:
                review_id = Review.objects.get(id=row[1])
                author = User.objects.get(id=row[3])
                Comments.objects.create(
                    id=row[0],
                    author=author,
                    review=review_id,
                    text=row[2],
                    pub_date=row[4],
                ).save()
                n += 1
                print(f"done {n}")
