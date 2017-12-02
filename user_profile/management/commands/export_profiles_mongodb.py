from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from user_profile.models import ProviderProfile, Course, Provider, Status, CourseStatus
import requests
import timeit

class Command(BaseCommand):
    help = 'Scraps courses from codeschool'

    def handle(self, *args, **options):

        def manage_relation_course_profile(profile, course, status):
            relation, created = CourseStatus.objects.update_or_create(profile=profile,
                                                                      course=course,
                                                                      status=status)

        def add_courses_to_user(user, courses, status, provider):
            status = Status.objects.get(name=status)
            provider = Provider.objects.get(name=provider)
            profile, created = ProviderProfile.objects.get_or_create(user=user,
                                                                     provider=provider)

            for course in courses:
                new_course, created = Course.objects.get_or_create(
                    title=course.get('title'),
                    url=course.get('url'),
                    badge=course.get('badge'),
                    provider=provider
                )
                manage_relation_course_profile(profile, new_course, status)
                # profile.CourseStatus.add(new_course)
                # profile.save()



        CODESCHOOL_URL = 'https://www.codeschool.com/users/{}.json'
        for profile in ProviderProfile.objects.all():
            try:
                start = timeit.default_timer()

                # Your statements here

                if not profile.username_provider:
                    raise Exception('Username does not have a provider profile')
                url = CODESCHOOL_URL.format(profile.username_provider)
                # print('Doing request to ... {}'.format(url))
                response = requests.get(url).json()
                courses = response.get('courses')
                add_courses_to_user(user=profile.user,
                                    courses=courses.get('in_progress'),
                                    status='i',
                                    provider='codeschool')

                add_courses_to_user(user=profile.user,
                                    courses=courses.get('completed'),
                                    status='c',
                                    provider='codeschool')
                stop = timeit.default_timer()
                print(stop-start)
            except Exception as e:
                raise CommandError('Error in request {}'.format(e))
