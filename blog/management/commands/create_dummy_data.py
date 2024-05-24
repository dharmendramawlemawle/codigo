# blog/management/commands/create_dummy_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Author, Category, Tag, Post, Comment
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generate dummy data for the blog'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of dummy data to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        # Create dummy users
        for _ in range(total):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password'
            )
            Author.objects.create(user=user, bio=fake.text())

        # Create dummy categories
        categories = ['Technology', 'Travel', 'Food', 'Fashion', 'Sports']
        for category_name in categories:
            Category.objects.create(name=category_name)

        # Create dummy tags
        tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5']
        for tag_name in tags:
            Tag.objects.create(name=tag_name,slug= None)

        # Create dummy posts
        authors = Author.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        for _ in range(total):
            author = random.choice(authors)
            title = fake.sentence()
            content = fake.paragraphs(nb=5, ext_word_list=None)
            created_at = fake.date_time_between(start_date='-30d', end_date='now')
            post = Post.objects.create(
                title=title,
                author=author,
                content=content,
                created_at=created_at
            )
            post.categories.set(random.sample(list(categories), k=random.randint(1, 3)))
            post.tags.set(random.sample(list(tags), k=random.randint(1, 3)))

            # Create dummy comments for each post
            for _ in range(total):
                commenter = random.choice(authors)
                Comment.objects.create(
                    post=post,
                    author=commenter.user,
                    content=fake.paragraph()
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} dummy data for the blog'))
