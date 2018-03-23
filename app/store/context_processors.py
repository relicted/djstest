from django.conf import settings
import datetime


def get_copyrights(request):
    this_year = datetime.datetime.now().year
    copyrights = f'© {settings.COPY_START_YEAR} - {this_year} ' \
                f'All Rights Reserved. privet kak dela?'
    return {'copyrights': copyrights,
            'cr_start': settings.COPY_START_YEAR,
            'cr_end': this_year}
