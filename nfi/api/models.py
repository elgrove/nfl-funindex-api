# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Raw(models.Model):
    match_id = models.CharField(blank=False, null=False, max_length=11, primary_key=True) # 11 chars = 20200101abc
    date = models.DateField(auto_now=False, blank=False, null=False)
    time = models.TimeField(auto_now=False, blank=False, null=False)
    week = models.IntegerField(blank=False, null=False)
    season = models.IntegerField(blank=False, null=False)
    ot = models.IntegerField(blank=False, null=False)
    teama_name = models.CharField(blank=False, null=False, max_length=50)
    teama_pts = models.IntegerField(blank=False, null=False)
    teama_pts_q1 = models.IntegerField(blank=False, null=False)
    teama_pts_q2 = models.IntegerField(blank=False, null=False)
    teama_pts_q3 = models.IntegerField(blank=False, null=False)
    teama_pts_q4 = models.IntegerField(blank=False, null=False)
    teama_yds = models.IntegerField(blank=False, null=False)
    teama_yds_rush = models.IntegerField(blank=False, null=False)
    teama_yds_pass = models.IntegerField(blank=False, null=False)
    teama_tds = models.IntegerField(blank=False, null=False)
    teama_tds_rush = models.IntegerField(blank=False, null=False)
    teama_tds_pass = models.IntegerField(blank=False, null=False)
    teama_tos = models.IntegerField(blank=False, null=False)
    teama_4d_att = models.IntegerField(blank=False, null=False)
    teama_4d_comp = models.IntegerField(blank=False, null=False)
    teama_sacks = models.IntegerField(blank=False, null=False)
    teama_sack_yds = models.IntegerField(blank=False, null=False)
    teama_rtn_td = models.IntegerField(blank=False, null=False)
    teama_drives = models.IntegerField(blank=False, null=False)
    teamh_name = models.CharField(blank=False, null=False, max_length=50)
    teamh_pts = models.IntegerField(blank=False, null=False)
    teamh_pts_q1 = models.IntegerField(blank=False, null=False)
    teamh_pts_q2 = models.IntegerField(blank=False, null=False)
    teamh_pts_q3 = models.IntegerField(blank=False, null=False)
    teamh_pts_q4 = models.IntegerField(blank=False, null=False)
    teamh_yds = models.IntegerField(blank=False, null=False)
    teamh_yds_rush = models.IntegerField(blank=False, null=False)
    teamh_yds_pass = models.IntegerField(blank=False, null=False)
    teamh_tds = models.IntegerField(blank=False, null=False)
    teamh_tds_rush = models.IntegerField(blank=False, null=False)
    teamh_tds_pass = models.IntegerField(blank=False, null=False)
    teamh_tos = models.IntegerField(blank=False, null=False)
    teamh_4d_att = models.IntegerField(blank=False, null=False)
    teamh_4d_comp = models.IntegerField(blank=False, null=False)
    teamh_sacks = models.IntegerField(blank=False, null=False)
    teamh_sack_yds = models.IntegerField(blank=False, null=False)
    teamh_rtn_td = models.IntegerField(blank=False, null=False)
    teamh_drives = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'raw'


class SummaryView(models.Model):
    match_id = models.CharField(blank=False, null=False, max_length=11, primary_key=True)
    date = models.DateField(auto_now=False, blank=False, null=False)
    time = models.TimeField(auto_now=False, blank=False, null=False)
    week = models.IntegerField(blank=False, null=False)
    season = models.IntegerField(blank=False, null=False)
    teama_name = models.CharField(blank=False, null=False, max_length=50)
    teamh_name = models.CharField(blank=False, null=False, max_length=50)
    pts = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    ptsqf = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    yds = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    tds = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    tos = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    fdpc = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    sacks = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    sackyds = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    rtns = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    drives = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    drvtdpc = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    close = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    closeqf = models.IntegerField(blank=False, null=False)  # This field type is a guess.
    ot = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'summary_view'


class WebView(models.Model):
    match_id = models.CharField(blank=False, null=False, max_length=11, primary_key=True)
    date = models.DateField(auto_now=False, blank=False, null=False)
    time = models.TimeField(auto_now=False, blank=False, null=False)
    week = models.IntegerField(blank=False, null=False)
    season = models.IntegerField(blank=False, null=False)
    teama_name = models.CharField(blank=False, null=False, max_length=50)
    teamh_name = models.CharField(blank=False, null=False, max_length=50)
    fun_score = models.IntegerField(blank=False, null=False)  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'web_view'
