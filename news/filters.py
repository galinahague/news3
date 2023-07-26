from django_filters import FilterSet,  DateTimeFilter
from django.forms import DateTimeInput
from .models import New

class NewFilter(FilterSet):
    added_after = DateTimeFilter(field_name='date_post',
                               lookup_expr='gt',
                               widget=DateTimeInput(format='%Y-%m-%dT%H:%M',
                                                    attrs={'type':'datetime-local'},
                                                    ),
                               )
    class Meta:
        model = New
        fields = {'title': ['icontains'],
                  'categoryType': ['exact'],
                  }