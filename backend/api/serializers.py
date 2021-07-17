from api.models import WebView
from rest_framework import serializers

class RawViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebView
        fields = [
            "match_id",
            "date",
            "time",
            "week",
            "season",
            "teama_name",
            "teamh_name",
            "fun_score",
        ]


class WebViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebView
        fields = [
            "date",
            "time",
            "teama_name",
            "teamh_name",
            "fun_score",
        ]
