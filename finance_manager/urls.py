from rest_framework import routers
from .views import BankViewSet, AccountViewSet, CategoryViewSet, TransactionViewSet


router = routers.DefaultRouter()

router.register(r"banks", BankViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"transactions", TransactionViewSet)
