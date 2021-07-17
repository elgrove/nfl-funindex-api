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

    date = serializers.DateField()
    time = serializers.TimeField()
    teama_name = serializers.CharField()
    teamh_name = serializers.CharField()
    fun_score = serializers.DecimalField(
        max_digits = 5, decimal_places = 2
    )

    class Meta:
        model = WebView
        fields = [
            "date",
            "time",
            "teama_name",
            "teamh_name",
            "fun_score",
        ]
