from rest_framework import routers
from .api_views import ArticleViewset

router = routers.SimpleRouter()
router.register('article', ArticleViewset, basename='article')