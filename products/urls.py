from django.urls import path, include
from rest_framework.routers import DefaultRouter


from products.views import ProductViewSet, CastVoteView, VoteCountView, RatingViewSet, RatingListView

router = DefaultRouter()
#router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vote/<int:id>/', CastVoteView.as_view({'post': 'create', 'patch': 'update', 'delete': 'destroy'}), name='vote'),
    path('vote/count/<int:rating_id>', VoteCountView.as_view(), name='vote_count'),
    path('product/review/', RatingViewSet.as_view({'post': 'create'}), name='product_review'),
    path('product/reviews/', RatingListView.as_view(), name='product_reviews'),
]
