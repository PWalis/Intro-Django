from rest_framework import serializers, viewsets
from .models import PersonalNote

# Creates hyperlink to the PersonalNote model
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

# Allows us to connect and see models specified
class PersonalNoteViewSet(viewsets.ModelViewSet):
    # Hyper link to the PersonalNote model
    serializer_class = PersonalNoteSerializer
    # Initializes the query set with none
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        # self refers to the ViewSet
        logged_in_user = self.request.user
        # If session user is anon don't show any personal notes because they don't have any
        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        # Otherwise show the PersonalNotes that corrispong to the session user
        else:
            return PersonalNote.objects.filter(user=logged_in_user)