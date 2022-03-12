# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BusinessFiles(models.Model):
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_files'


class BusinessLicenses(models.Model):
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_licenses'


class Certs(models.Model):
    user = models.IntegerField(blank=True, null=True)
    exam_paper = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certs'


class Comments(models.Model):
    content = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    dive_log = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    community = models.IntegerField(blank=True, null=True)
    magazine = models.IntegerField(blank=True, null=True)
    product = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Communities(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    views = models.BigIntegerField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communities'


class CommunityCategories(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_categories'


class CoreStore(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    environment = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_store'


class DiveGrams(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_grams'


class DiveLogs(models.Model):
    nation = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    divepoint = models.CharField(db_column='divePoint', max_length=255, blank=True, null=True)
    weather = models.CharField(max_length=255, blank=True, null=True)
    bird = models.CharField(max_length=255, blank=True, null=True)
    birdie = models.CharField(max_length=255, blank=True, null=True)
    suit = models.CharField(max_length=255, blank=True, null=True)
    tank = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    divingminute = models.IntegerField(db_column='divingMinute', blank=True, null=True)
    maxwaterdepth = models.DecimalField(db_column='maxWaterDepth', max_digits=10, decimal_places=2, blank=True, null=True)
    waterdepth = models.DecimalField(db_column='waterDepth', max_digits=10, decimal_places=2, blank=True, null=True)
    personnel = models.IntegerField(blank=True, null=True)
    windspeed = models.IntegerField(db_column='windSpeed', blank=True, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wave = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    starttair = models.DecimalField(db_column='startTair', max_digits=10, decimal_places=2, blank=True, null=True)
    finishshair = models.DecimalField(db_column='finishShair', max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    public = models.CharField(max_length=255, blank=True, null=True)
    lognumber = models.CharField(db_column='logNumber', max_length=255, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    dive_point = models.IntegerField(blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    divingtype = models.CharField(db_column='divingType', max_length=255, blank=True, null=True)
    gas = models.CharField(max_length=255, blank=True, null=True)
    divinggoal = models.CharField(db_column='divingGoal', max_length=255, blank=True, null=True)
    bcd = models.CharField(max_length=255, blank=True, null=True)
    sight = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    resort = models.CharField(max_length=255, blank=True, null=True)
    teacher = models.IntegerField(blank=True, null=True)
    divepointkeyword = models.CharField(db_column='divePointKeyword', max_length=255, blank=True, null=True)
    resortkeyword = models.CharField(db_column='resortKeyword', max_length=255, blank=True, null=True)
    teacherkeyword = models.CharField(db_column='teacherKeyword', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_logs'


class DiveLogsResorts(models.Model):
    dive_log_id = models.IntegerField(blank=True, null=True)
    resort_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_logs__resorts'


class DiveLogsTeachers(models.Model):
    dive_log_id = models.IntegerField(blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_logs__teachers'


class DiveMagazines(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_magazines'


class DivePoints(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    placeinfo = models.CharField(db_column='placeInfo', max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    star = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    sn = models.CharField(max_length=255, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    collecting = models.IntegerField(blank=True, null=True)
    extreme = models.IntegerField(blank=True, null=True)
    ecosystem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_points'


class DivePointsCollectings(models.Model):
    dive_point_id = models.IntegerField(blank=True, null=True)
    select_option_id = models.IntegerField(db_column='select-option_id', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'dive_points__collectings'


class DivePointsEcosystems(models.Model):
    dive_point_id = models.IntegerField(blank=True, null=True)
    select_option_id = models.IntegerField(db_column='select-option_id', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'dive_points__ecosystems'


class DivePointsExtremes(models.Model):
    dive_point_id = models.IntegerField(blank=True, null=True)
    select_option_id = models.IntegerField(db_column='select-option_id', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'dive_points__extremes'


class DivePointsResortsResortsDivePoints(models.Model):
    dive_point_id = models.IntegerField(db_column='dive-point_id', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    resort_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_points_resorts__resorts_dive_points'


class DivePointsRestaurantsRestaurantsDivePoints(models.Model):
    dive_point_id = models.IntegerField(db_column='dive-point_id', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    restaurant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_points_restaurants__restaurants_dive_points'


class DivePointsTeachersTeachersDivePoints(models.Model):
    dive_point_id = models.IntegerField(db_column='dive-point_id', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    teacher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_points_teachers__teachers_dive_points'


class DiveTours(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)
    enddate = models.DateField(db_column='endDate', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    star = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dive_tours'


class EducationResults(models.Model):
    education = models.IntegerField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ispass = models.IntegerField(db_column='isPass', blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_results'


class Educations(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    video = models.IntegerField(blank=True, null=True)
    exam_paper = models.IntegerField(blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'educations'


class ExamPapers(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    questions = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_papers'


class I18NLocales(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i18n_locales'


class Inquiries(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answerdate = models.DateTimeField(db_column='answerDate', blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inquiries'


class Keywords(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)
    dive_log = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Licenses(models.Model):
    user = models.IntegerField(blank=True, null=True)
    licenseissuer = models.CharField(db_column='LicenseIssuer', max_length=255, blank=True, null=True)
    licenseissueddate = models.CharField(db_column='LicenseIssuedDate', max_length=255, blank=True, null=True)
    association = models.CharField(db_column='Association', max_length=255, blank=True, null=True)
    licensenumber = models.CharField(db_column='LicenseNumber', max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    domesticlogcount = models.IntegerField(db_column='domesticLogCount', blank=True, null=True)
    overseaslogcount = models.IntegerField(db_column='overseasLogCount', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licenses'


class Likes(models.Model):
    user = models.IntegerField(blank=True, null=True)
    dive_log = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    liketype = models.CharField(db_column='likeType', max_length=255, blank=True, null=True)
    community = models.IntegerField(blank=True, null=True)
    product = models.IntegerField(blank=True, null=True)
    magazine = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'


class Magazines(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    showhome = models.IntegerField(db_column='showHome', blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magazines'


class Products(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    isused = models.IntegerField(db_column='isUsed', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    views = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class ResortEvents(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)
    enddate = models.DateField(db_column='endDate', blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resort_events'


class ResortReservations(models.Model):
    divingtype = models.CharField(db_column='divingType', max_length=255, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)
    enddate = models.DateField(db_column='endDate', blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    divegroup = models.CharField(db_column='diveGroup', max_length=255, blank=True, null=True)
    licenseissuer = models.CharField(db_column='licenseIssuer', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    addressdetail = models.CharField(db_column='addressDetail', max_length=255, blank=True, null=True)
    licenselist = models.CharField(db_column='licenseList', max_length=255, blank=True, null=True)
    sleepperiod = models.CharField(db_column='sleepPeriod', max_length=255, blank=True, null=True)
    accommodation = models.IntegerField(blank=True, null=True)
    breakfast = models.IntegerField(blank=True, null=True)
    pickup = models.IntegerField(blank=True, null=True)
    instrpart = models.IntegerField(db_column='instrPart', blank=True, null=True)
    nightdiving = models.IntegerField(db_column='nightDiving', blank=True, null=True)
    naiteuroksseu = models.IntegerField(blank=True, null=True)
    equipment = models.CharField(max_length=255, blank=True, null=True)
    guide = models.IntegerField(blank=True, null=True)
    instrinfo = models.CharField(db_column='instrInfo', max_length=255, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resort_reservations'


class Resorts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    star = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    showresortmainview = models.IntegerField(db_column='showResortMainView', blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    breakfast = models.IntegerField(blank=True, null=True)
    accommodation = models.IntegerField(blank=True, null=True)
    education = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    camera = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    addressdetail = models.CharField(db_column='addressDetail', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resorts'


class ResortsRestaurantsRestaurantsResorts(models.Model):
    resort_id = models.IntegerField(blank=True, null=True)
    restaurant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resorts_restaurants__restaurants_resorts'


class Restaurants(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    addressdetail = models.CharField(db_column='addressDetail', max_length=255, blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurants'


class Reviews(models.Model):
    servicestar = models.DecimalField(db_column='serviceStar', max_digits=10, decimal_places=2, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answerdate = models.DateField(db_column='answerDate', blank=True, null=True)
    cleanstar = models.DecimalField(db_column='cleanStar', max_digits=10, decimal_places=2, blank=True, null=True)
    convstar = models.DecimalField(db_column='convStar', max_digits=10, decimal_places=2, blank=True, null=True)
    restaurantstar = models.DecimalField(db_column='restaurantStar', max_digits=10, decimal_places=2, blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    dive_point = models.IntegerField(blank=True, null=True)
    dive_log = models.IntegerField(blank=True, null=True)
    divepointstar = models.DecimalField(db_column='divePointStar', max_digits=10, decimal_places=2, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    tour = models.IntegerField(blank=True, null=True)
    goodcontent = models.TextField(db_column='goodContent', blank=True, null=True)
    badcontent = models.TextField(db_column='badContent', blank=True, null=True)
    teacher = models.IntegerField(blank=True, null=True)
    teacherstar = models.DecimalField(db_column='teacherStar', max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class RoomCarts(models.Model):
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    daterange = models.IntegerField(db_column='dateRange', blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_carts'


class RoomReservations(models.Model):
    user = models.IntegerField(blank=True, null=True)
    checkin = models.DateTimeField(db_column='checkIn', blank=True, null=True)
    checkout = models.DateTimeField(db_column='checkOut', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    roomname = models.CharField(db_column='roomName', max_length=255, blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_reservations'


class Rooms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    lift = models.IntegerField(blank=True, null=True)
    enter = models.TimeField(blank=True, null=True)
    checkout = models.TimeField(db_column='checkOut', blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class ScubaShops(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    addressdetail = models.CharField(db_column='addressDetail', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scuba_shops'


class SelectOptions(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'select_options'


class Shops(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    addressdetail = models.CharField(db_column='addressDetail', max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    businessnumber = models.CharField(db_column='businessNumber', max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class StrapiAdministrator(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    resetpasswordtoken = models.CharField(db_column='resetPasswordToken', max_length=255, blank=True, null=True)
    registrationtoken = models.CharField(db_column='registrationToken', max_length=255, blank=True, null=True)
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)
    blocked = models.IntegerField(blank=True, null=True)
    preferedlanguage = models.CharField(db_column='preferedLanguage', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strapi_administrator'


class StrapiPermission(models.Model):
    action = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strapi_permission'


class StrapiRole(models.Model):
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strapi_role'


class StrapiUsersRoles(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strapi_users_roles'


class StrapiWebhooks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strapi_webhooks'


class Teachers(models.Model):
    infotitle = models.CharField(db_column='infoTitle', max_length=255, blank=True, null=True)
    infocontent = models.CharField(db_column='infoContent', max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    calltime = models.CharField(db_column='callTime', max_length=255, blank=True, null=True)
    paymenttype = models.CharField(db_column='paymentType', max_length=255, blank=True, null=True)
    service = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'


class TourItems(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    tour = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_items'


class TourPayments(models.Model):
    price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    tourname = models.CharField(db_column='tourName', max_length=255, blank=True, null=True)
    tour = models.IntegerField(blank=True, null=True)
    totalprice = models.IntegerField(db_column='totalPrice', blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_payments'


class TourReviews(models.Model):
    score = models.IntegerField(blank=True, null=True)
    positivecomment = models.TextField(db_column='positiveComment', blank=True, null=True)
    negativecomment = models.CharField(db_column='negativeComment', max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_reviews'


class TourWishLists(models.Model):
    tour = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_wish_lists'


class Tours(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tours'


class UploadFile(models.Model):
    name = models.CharField(max_length=255)
    alternativetext = models.CharField(db_column='alternativeText', max_length=255, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    formats = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=255)
    ext = models.CharField(max_length=255, blank=True, null=True)
    mime = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=255)
    previewurl = models.CharField(db_column='previewUrl', max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255)
    provider_metadata = models.TextField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_file'


class UploadFileMorph(models.Model):
    upload_file_id = models.IntegerField(blank=True, null=True)
    related_id = models.IntegerField(blank=True, null=True)
    related_type = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_file_morph'


class UserProfiles(models.Model):
    user = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profiles'


class UserTests(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    career = models.IntegerField(blank=True, null=True)
    krdivingcount = models.IntegerField(db_column='krDivingCount', blank=True, null=True)
    overseasdivingcount = models.IntegerField(db_column='overseasDivingCount', blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    dormantmonth = models.IntegerField(db_column='dormantMonth', blank=True, null=True)
    suit = models.CharField(max_length=255, blank=True, null=True)
    totalscore = models.DecimalField(db_column='totalScore', max_digits=10, decimal_places=2, blank=True, null=True)
    resulttext = models.TextField(db_column='resultText', blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tests'


class UsersPermissionsPermission(models.Model):
    type = models.CharField(max_length=255)
    controller = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    enabled = models.IntegerField()
    policy = models.CharField(max_length=255, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users-permissions_permission'


class UsersPermissionsRole(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users-permissions_role'


class UsersPermissionsUser(models.Model):
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(max_length=255)
    provider = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    resetpasswordtoken = models.CharField(db_column='resetPasswordToken', max_length=255, blank=True, null=True)
    confirmationtoken = models.CharField(db_column='confirmationToken', max_length=255, blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    blocked = models.IntegerField(blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    addressdetail = models.CharField(db_column='addressDetail', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    divenumber = models.CharField(db_column='diveNumber', max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    association = models.CharField(max_length=255, blank=True, null=True)
    licensenumber = models.CharField(db_column='licenseNumber', max_length=255, blank=True, null=True)
    equipment = models.CharField(max_length=255, blank=True, null=True)
    equipmentbuydate = models.DateField(db_column='equipmentBuyDate', blank=True, null=True)
    divingscore = models.DecimalField(db_column='divingScore', max_digits=10, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    divingtestresult = models.TextField(db_column='divingTestResult', blank=True, null=True)
    personalterm = models.IntegerField(db_column='personalTerm', blank=True, null=True)
    useterm = models.IntegerField(db_column='useTerm', blank=True, null=True)
    bankingterm = models.IntegerField(db_column='bankingTerm', blank=True, null=True)
    positionterm = models.IntegerField(db_column='positionTerm', blank=True, null=True)
    adterm = models.IntegerField(db_column='adTerm', blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    businessnumber = models.CharField(db_column='businessNumber', max_length=255, blank=True, null=True)
    resort = models.IntegerField(blank=True, null=True)
    subemail = models.CharField(db_column='subEmail', max_length=255, blank=True, null=True)
    licenseissueddate = models.CharField(db_column='licenseIssuedDate', max_length=255, blank=True, null=True)
    licenseissuer = models.CharField(db_column='licenseIssuer', max_length=255, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    user_profile = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    businessname = models.CharField(db_column='businessName', max_length=255, blank=True, null=True)
    homepagelink = models.CharField(db_column='homePageLink', max_length=255, blank=True, null=True)
    businessbuilddate = models.CharField(db_column='businessBuildDate', max_length=255, blank=True, null=True)
    phoneagency = models.CharField(db_column='phoneAgency', max_length=255, blank=True, null=True)
    emailtext = models.CharField(db_column='emailText', max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    infodisclosure = models.IntegerField(db_column='infoDisclosure', blank=True, null=True)
    domesticlogcount = models.IntegerField(db_column='domesticLogCount', blank=True, null=True)
    overseaslogcount = models.IntegerField(db_column='overseasLogCount', blank=True, null=True)
    business_license = models.IntegerField(blank=True, null=True)
    license_image = models.IntegerField(blank=True, null=True)
    isinstructor = models.IntegerField(db_column='isInstructor', blank=True, null=True)
    licensecertified = models.CharField(db_column='licenseCertified', max_length=255, blank=True, null=True)
    business_file = models.IntegerField(blank=True, null=True)
    resortconfirm = models.IntegerField(db_column='resortConfirm', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users-permissions_user'


class Videos(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos'
