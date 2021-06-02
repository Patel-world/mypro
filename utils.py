import string, random

from django.utils.text import slugify

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def random_string_generator():
    letters = string.ascii_lowercase
    result_str1 = ''.join(random.choice(letters) for i in range(3))
    result_str2 = ''.join(random.choice(letters) for i in range(4))
    result_str3 = ''.join(random.choice(letters) for i in range(3))
    year = result_str1 + '-' + result_str2 + '-' + result_str3
    return year

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator()
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
