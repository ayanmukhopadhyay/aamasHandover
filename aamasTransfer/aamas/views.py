from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        context_instance=RequestContext(request,
                                        {
                                            'title': 'Home Page',
                                            'year': datetime.now().year,
                                        })
    )

def venue(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'venue.html',
        context_instance=RequestContext(request, {})
    )

def submissions(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'submissions.html',
        context_instance=RequestContext(request, {})
    )

def about(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        context_instance=RequestContext(request, {})
    )

def attendingAamas(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'attendingAamas.html',
        context_instance=RequestContext(request, {})
    )

def callForPapers(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'callForPapers.html',
        context_instance=RequestContext(request, {})
    )

def about(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        context_instance=RequestContext(request, {})
    )

def committees(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'committees.html',
        context_instance=RequestContext(request, {})
    )

def doctorMentor(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'doctorMentor.html',
        context_instance=RequestContext(request, {})
    )

def importantDates(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'importantDates.html',
        context_instance=RequestContext(request, {})
    )

def specialInd(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'specialIndustrial.html',
        context_instance=RequestContext(request, {})
    )

def sponsors(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sponsors.html',
        context_instance=RequestContext(request, {})
    )

def sponsorshipLevels(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sponsorshipLevels.html',
        context_instance=RequestContext(request, {})
    )

def tourism(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'tourism.html',
        context_instance=RequestContext(request, {})
    )

def tutorials(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'tutorials.html',
        context_instance=RequestContext(request, {})
    )

def workshops(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'workshops.html',
        context_instance=RequestContext(request, {})
    )

def blueSkyIdeasTrack(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blueSkyIdeasTrack.html',
        context_instance=RequestContext(request, {})
    )

def roboticsTrack(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'roboticsTrack.html',
        context_instance=RequestContext(request, {})
    )


def sociallyInteractiveAgentsTrack(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sociallyInteractiveAgentsTrack.html',
        context_instance=RequestContext(request, {})
    )

def jaamasTrack(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'jaamas.html',
        context_instance=RequestContext(request, {})
    )

def spc(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'spc.html',
        context_instance=RequestContext(request, {})
    )

def areaChairs(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'areaChairs.html',
        context_instance=RequestContext(request, {})
    )

def pc(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pc.html',
        context_instance=RequestContext(request, {})
    )

def localOrganization(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'localOrganizingCommittee.html',
        context_instance=RequestContext(request, {})
    )

def callForTutorials(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'callForTutorials.html',
        context_instance=RequestContext(request, {})
    )


def callForDemos(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'callForDemos.html',
        context_instance=RequestContext(request, {})
    )

def studentTravel(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'studentTravel.html',
        context_instance=RequestContext(request, {})
    )

def accommodation(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'accommodation.html',
        context_instance=RequestContext(request, {})
        )

def stockholm(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'stockholm.html',
        context_instance=RequestContext(request, {})
    )

def additionalInfo(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'additionalInfo.html',
        context_instance=RequestContext(request, {})
    )

def traveling(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'traveling.html',
        context_instance=RequestContext(request, {})
    )

def map(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'map.html',
        context_instance=RequestContext(request, {})
    )

def acmSigai(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acmSigai.html',
        context_instance=RequestContext(request, {})
    )

def victorLesser(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'victor.html',
        context_instance=RequestContext(request, {})
    )

def exhibits(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'exhibits.html',
        context_instance=RequestContext(request, {})
    )

def ifaamasBestPaper(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'ifaamas.html',
        context_instance=RequestContext(request, {})
    )

def acceptedPapers(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acceptedPapers.html',
        context_instance=RequestContext(request, {})
    )

def acceptedPapersIndustrial(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acceptedIndustrial.html',
        context_instance=RequestContext(request, {})
    )

def acceptedPapersSIA(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acceptedSIA.html',
        context_instance=RequestContext(request, {})
    )

def acceptedPapersBlueSky(request):
    """Renders the home page."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acceptedBlueSky.html',
        context_instance=RequestContext(request, {})
    )

def acceptedPapersRobotics(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acceptedRobotics.html',
        context_instance=RequestContext(request, {})
    )

def workshopsList(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'workshopsList.html',
        context_instance=RequestContext(request, {})
    )

def tutorialsList(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'tutorials.html',
        context_instance=RequestContext(request, {})
    )

def invitedSpeakers(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'invitedSpeakers.html',
        context_instance=RequestContext(request, {})
    )

def registration(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'registration.html',
        context_instance=RequestContext(request, {})
    )

def schedule(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'schedule.html',
        context_instance=RequestContext(request, {})
    )

def acceptedDoctoral(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'acceptedDoctoral.html',
        context_instance=RequestContext(request, {})
    )

def jul11(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'jul11.html',
        context_instance=RequestContext(request, {})
    )

def jul12(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'jul12.html',
        context_instance=RequestContext(request, {})
    )

def jul13(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'jul13.html',
        context_instance=RequestContext(request, {})
    )

def posterSchedule(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'posterSchedule.html',
        context_instance=RequestContext(request, {})
    )

def detailedProgram(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'detailedProgram.html',
        context_instance=RequestContext(request, {})
    )

def demoSchedule(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'demoSchedule.html',
        context_instance=RequestContext(request, {})
    )

def paperAward(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'bestPaperNominees.html',
        context_instance=RequestContext(request, {})
    )

def infoLast(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'info.html',
        context_instance=RequestContext(request, {})
    )

def socialEvents(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'socialEvents.html',
        context_instance=RequestContext(request, {})
    )

def awardWinner(request):
    """Renders the homepage."""
    # Test Comment
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'awardWinners.html',
        context_instance=RequestContext(request, {})
    )


    # def scrollingnavbar(request):
#     """Renders the home page."""
#     # Test Comment
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'scrolling_nav.html',
#         context_instance=RequestContext(request, {})
#     )


