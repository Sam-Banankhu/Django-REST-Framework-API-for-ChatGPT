from django.urls import path

# internals
from api.views import QueryResponderView
urlpatterns = [
   # all the Views are in views file.
    # path('users/', UserView.as_view(), name='users'),
    # path('token/', TokenView.as_view(), name='tokens'),
    path('query-responser/', QueryResponderView.as_view(), name='query-responser'),
]