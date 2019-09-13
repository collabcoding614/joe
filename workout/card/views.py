# import viewsets and serializers from django rest framework
from rest_framework import viewsets, serializers

# import our models to use in our serializers and viewset
from .models import Weight, Card

#
# Make a serializer and a viewset for each model
#


# all serializers name as "Model"Serializer and inherits from modelserializer
class CardSerializer(serializers.ModelSerializer):

    # definition of serializer, what model are we using and what fields from the model do we want to show
    class Meta:
        model = Card
        fields = "__all__"


class WeightSerializer(serializers.ModelSerializer):

    # meta is a class inside a class, this is a python thingy, not used in most languages
    class Meta:
        model = Weight
        fields = "__all__"


class CardViewSet(viewsets.ModelViewSet):
    # this is a db lookup
    # you can do filters or other such things
    # Card.objects.filter(name='bob') if name == bob exists in the db
    # normally for a base queryset you wouldn't do a filtered set
    queryset = Card.objects.all()

    # just the serializer associated with the viewset
    serializer_class = CardSerializer


class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
