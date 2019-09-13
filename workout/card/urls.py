from rest_framework.routers import DefaultRouter

# this is a local import that just imports the entire views file
# you can import specifically a view but this is cleaner(less imports)
# specific view import looks like....
# from .views import CardViewSet
from . import views

app_name = 'card'

router = DefaultRouter()

# urls here are plural, but the base urls in workout/urls.py is singular and is an overall url
# like
# card/cards/
# card/weights/

# if we imported each viewset alone we would not add views. to the beginning of views.CardViewSet
router.register('cards', views.CardViewSet)
router.register('weights', views.WeightViewSet)

urlpatterns = [
] + router.urls
