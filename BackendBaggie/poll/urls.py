from django.urls import path
from poll.views import PollAPIView

urlpatterns = [
    path('', PollAPIView.as_view(), name="new add"),
    # path('<int:id>/edit/', PollView.as_view(), name='poll_edit'),
    # path('<int:id>/delete/', PollView.as_view(), name='poll_delete'),
    # path('list/', index, name='polls_list'),
    # path('<int:id>/details/', details, name="poll_details"),
    # path('<int:id>/', vote_poll, name="poll_vote")
]
