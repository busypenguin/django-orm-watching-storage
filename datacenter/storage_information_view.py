from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits_serialized = []
    for visit in non_closed_visits:

        non_closed_visits_serialized.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(visit),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits_serialized,
    }
    return render(request, 'storage_information.html', context)


