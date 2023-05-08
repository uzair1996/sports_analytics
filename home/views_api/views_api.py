from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import permissions
from ..models import Matches,Innings,Teams,Series
from .. import serializers
from django.shortcuts import render
from django.db.models import F,Q
from django.conf import settings



#def my_view(request):
 #   mymatches = Innings.objects.all()
  #  print(mymatches)
    #context = {'mymodels': mymatches}
   # return render(request, 'api.html', {'mymatches':mymatches})

#def my_view(request):
 #   mymatches = Matches.objects.using('sports_analysis').order_by('-match_id')[:10]
  #  print(mymatches)
   # return render(request, 'project.html', {'mymatches': mymatches})

class MatchesListApiView(APIView):
    def get(self,request,*args,**kwargs):
        mymatches = Matches.objects.all().using('sports_analysis')
        serializer = serializers.MatchesSerializer(mymatches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
def my_view2(request):
    teams = Teams.objects.using('sports_analysis').order_by('team_name')
    print(teams)
    return render(request, 'project.html', {'teams': teams})

    
#def my_view4(request):
 #   queryset = Series.objects.using('sports_analysis').filter(
  #    seriesmatches__match__winning_team__isnull=False
   # ).annotate(
    #    winning_team=F('seriesmatches__match__winning_team__team_name'),
     #   match_type=F('seriesmatches__match__match_type'),
      #  venue=F('seriesmatches__match__venue'),
       # city=F('seriesmatches__match__city')
    #).values(
     #   'series_name', 'series_start_date', 'series_end_date',
      #  'match_type', 'venue', 'city', 'winning_team'
   # ).distinct()
    #return render(request, 'series.html', {'queryset': queryset})

def my_view4(request):
    search_query = request.GET.get('search', '')
    queryset = Series.objects.using('sports_analysis').filter(
        Q(series_name__icontains=search_query) | 
        Q(seriesmatches__match__winning_team__team_name__icontains=search_query)
    ).annotate(
        winning_team=F('seriesmatches__match__winning_team__team_name'),
        match_type=F('seriesmatches__match__match_type'),
        venue=F('seriesmatches__match__venue'),
        city=F('seriesmatches__match__city')
    ).values(
       'series_name', 'series_start_date', 'series_end_date',
        'match_type', 'venue', 'city', 'winning_team'
    ).distinct()

    context = {'queryset': queryset, 'search_query': search_query}
    return render(request, 'series.html', context)

def my_view6(request):
    search_query = request.GET.get('search', '')
    queryset = Series.objects.using('sports_analysis').filter(
        Q(series_name__icontains=search_query) | 
        Q(seriesmatches__match__winning_team__team_name__icontains=search_query),
        seriesmatches__match__match_type='Test'
    ).annotate(
        winning_team=F('seriesmatches__match__winning_team__team_name'),
        match_type=F('seriesmatches__match__match_type'),
        venue=F('seriesmatches__match__venue'),
        city=F('seriesmatches__match__city')
    ).values(
       'series_name', 'series_start_date', 'series_end_date',
        'match_type', 'venue', 'city', 'winning_team'
    ).distinct()

    context = {'queryset': queryset, 'search_query': search_query}
    return render(request, 'series.html', context)



def my_view5(request):
    search_query = request.GET.get('search', '')
    test_series = Series.objects.using('sports_analysis').filter(
        Q(series_start_date__year__gte=2002) &
        Q(series_start_date__year__lte=2005) &
        Q(seriesmatches__match__match_type='Test') &
        (Q(series_name__icontains=search_query) | 
         Q(seriesmatches__match__winning_team__team_name__icontains=search_query))
    ).annotate(
        winning_team=F('seriesmatches__match__winning_team__team_name'),
        match_type=F('seriesmatches__match__match_type'),
        venue=F('seriesmatches__match__venue'),
        city=F('seriesmatches__match__city')
    ).values(
        'series_name', 'series_start_date', 'series_end_date',
        'match_type', 'venue', 'city', 'winning_team'
    ).distinct()

    print(test_series)

    context = {'test_series': test_series, 'search_query': search_query}
    return render(request, 'series.html', context)





def images1(request):
    # your view logic here
    context = {'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'home.html', context)


#def test_match_table(request):
 #   test_matches = TestMatch.objects.filter(match_type='Test', start_date__year__gte=2002, end_date__year__lte=2005)
  #  return render(request, 'test_match_table.html', {'test_matches': test_matches})






