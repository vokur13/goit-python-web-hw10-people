import json
import os
import sys
from datetime import datetime

import django

sys.path.append(
    "/Users/vokur/PycharmProjects/goit/python-web/goit-python-web-hw10/people/django_project"
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from quotes.models import *

author_data = (
    "/Users/vokur/PycharmProjects/goit/python-web/goit-python-web-hw10/people/django_project/json_data"
    "/authors.json"
)
quote_data = (
    "/Users/vokur/PycharmProjects/goit/python-web/goit-python-web-hw10/people/django_project/json_data/quotes"
    ".json"
)

tags = set()

author_rows = {}
tag_rows = {}
quote_rows = {}


def create_authors():
    Author.objects.all().delete()
    with open(author_data, "r") as fa:
        data = json.load(fa)

        for item in data:
            born_date_str = item["born_date"]
            born_date = datetime.strptime(born_date_str, "%B %d, %Y")
            row = Author(
                fullname=item["fullname"],
                born_date=born_date,
                born_location=item["born_location"],
                biography=item["biography"],
            )
            row.save()
            author_rows[item["fullname"]] = row


def create_tags():
    Tag.objects.all().delete()
    with open(quote_data, "r") as fq:
        data = json.load(fq)

        for item in data:
            for name in item["tags"]:
                tags.add(name)

    for tag in tags:
        row = Tag(tag=tag)
        row.save()
        tag_rows[tag] = row


def create_quotes():
    # Tag.objects.all().delete()
    Quote.objects.all().delete()

    authors = Author.objects.all()
    tags_dict = Tag.objects.all()

    with open(quote_data, "r") as fq:
        data = json.load(fq)

        for quote in data:
            for author in authors:
                if author.fullname == quote["author"]:
                    row = Quote(author=author, quote=quote["quote"])
                    row.save()

                    for record in quote["tags"]:
                        for tag in tags_dict:
                            if tag.tag == record:
                                row.tags.add(tag)


if __name__ == "__main__":
    # create_authors()
    # create_tags()
    create_quotes()
