from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta: #type: ignore
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
