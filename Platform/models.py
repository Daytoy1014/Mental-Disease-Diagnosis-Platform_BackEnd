from django.db import models

class Public(models.Model):
    id = models.CharField(verbose_name='用户账号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='用户姓名',max_length=255)
    password = models.CharField(verbose_name='用户密码',max_length=255)
    gender = models.CharField(verbose_name='用户性别',max_length=10)
    age = models.IntegerField(verbose_name='用户年龄')
    birthdate = models.DateField(verbose_name='用户生日',null=True)
    region = models.CharField(verbose_name='用户住址',max_length=255)
    education = models.CharField(verbose_name='用户学历',max_length=255)
    phone = models.CharField(verbose_name='用户电话',max_length=255)
    ApoE = models.FloatField(verbose_name='ApoE')
    MMSE = models.FloatField(verbose_name='MMSE')
    CDR_Global = models.FloatField(verbose_name='CDR_Global')
    CDR_SOB = models.FloatField(verbose_name='CDR_SOB')
    ADAS_Cog = models.FloatField(verbose_name='ADAS_Cog')
    MRI = models.FloatField(verbose_name='MRI')
    PET = models.FloatField(verbose_name='PET')

    class Meta:
        db_table = 'public'
        verbose_name = '用户信息'
        indexes = [models.Index(fields=['id'])]

class Doctor(models.Model):
    id = models.CharField(verbose_name='医生账号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='医生姓名',max_length=255)
    password = models.CharField(verbose_name='医生密码',max_length=255)
    hospital = models.CharField(verbose_name='所属医院',max_length=255)
    department = models.CharField(verbose_name='所属部门',max_length=255)

    class Meta:
        db_table = 'doctor'
        verbose_name = '医生信息'
        indexes = [models.Index(fields=['id'])]

class Researcher(models.Model):
    id = models.CharField(verbose_name='研究员账号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='研究员姓名',max_length=255)
    password = models.CharField(verbose_name='研究员密码',max_length=255)
    department = models.CharField(verbose_name='所属单位',max_length=255)

    class Meta:
        db_table = 'researcher'
        verbose_name = '研究员信息'
        indexes = [models.Index(fields=['id'])]

class DiagnosisMission(models.Model):
    id = models.CharField(verbose_name='任务编号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='任务名称',max_length=255)
    patient_id = models.ForeignKey(Public, on_delete=models.CASCADE, verbose_name='患者账号')
    startTime = models.DateField(verbose_name='任务开始时间')
    endTime = models.DateField(verbose_name='任务结束时间')
    description = models.TextField(verbose_name='任务描述')
    result = models.TextField(verbose_name='任务结果')
    state = models.CharField(verbose_name='任务状态',max_length=255)


    class Meta:
        db_table = 'diagnosis_mission'
        verbose_name = '诊断任务'
        indexes = [models.Index(fields=['id'])]

class PredictMission(models.Model):
    id = models.CharField(verbose_name='任务编号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='任务名称',max_length=255)
    patient_id = models.ForeignKey(Public, on_delete=models.CASCADE, verbose_name='患者账号')
    startTime = models.DateField(verbose_name='任务开始时间')
    endTime = models.DateField(verbose_name='任务结束时间')
    risk = models.TextField(verbose_name='风险预测')
    state = models.CharField(verbose_name='任务状态',max_length=255)

    class Meta:
        db_table = 'predict_mission'
        verbose_name = '预测任务'
        indexes = [models.Index(fields=['id'])]

class PlanRecommendMission(models.Model):
    id = models.CharField(verbose_name='任务编号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='任务名称',max_length=255)
    patient_id = models.ForeignKey(Public, on_delete=models.CASCADE, verbose_name='患者账号')
    startTime = models.DateField(verbose_name='任务开始时间')
    endTime = models.DateField(verbose_name='任务结束时间')
    plan = models.TextField(verbose_name='干预方案')
    state = models.CharField(verbose_name='任务状态',max_length=255)

    class Meta:
        db_table = 'plan_recommend_mission'
        verbose_name = '干预方案推荐任务'
        indexes = [models.Index(fields=['id'])]

class Data(models.Model):
    id = models.CharField(verbose_name='数据集编号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='数据集名称',max_length=255)
    ownerID = models.CharField(verbose_name='数据集所有者',max_length=50)
    ownerName = models.CharField(verbose_name='数据集所有者姓名',max_length=255)
    time = models.DateTimeField(verbose_name='数据集上传时间')
    size = models.IntegerField(verbose_name='数据集大小')
    scene = models.CharField(verbose_name='数据集应用场景',max_length=255)
    description = models.TextField(verbose_name='数据集描述')
    model = models.CharField(verbose_name='数据集关联模型',max_length=255)
    data = models.FileField(verbose_name='数据集文件')

    class Meta:
        db_table = 'data'
        verbose_name = '数据集信息'
        indexes = [models.Index(fields=['id'])]

class Model(models.Model):
    id = models.CharField(verbose_name='模型编号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='模型名称',max_length=255)
    type = models.CharField(verbose_name='模型类型',max_length=255)
    ownerID = models.CharField(verbose_name='模型所有者',max_length=50)
    ownerName = models.CharField(verbose_name='模型所有者姓名',max_length=255)
    time = models.DateTimeField(verbose_name='模型上传时间')
    scene = models.CharField(verbose_name='模型应用场景',max_length=255)
    data = models.CharField(verbose_name='模型数据集',max_length=255)
    model = models.FileField(verbose_name='模型文件')
    description = models.TextField(verbose_name='模型描述')

    class Meta:
        db_table = 'model'
        verbose_name = '模型信息'
        indexes = [models.Index(fields=['id'])]

class RecordTemplate(models.Model):
    id = models.CharField(verbose_name='模板编号',max_length=50, primary_key=True)
    name = models.CharField(verbose_name='模板名称',max_length=255)
    ownerID = models.CharField(verbose_name='模板所有者',max_length=50)
    ownerName = models.CharField(verbose_name='模板所有者姓名',max_length=255)
    time = models.DateTimeField(verbose_name='模板上传时间')
    scene = models.CharField(verbose_name='模板应用场景',max_length=255)
    description = models.TextField(verbose_name='模板描述')
    data = models.FileField(verbose_name='模板文件')

    class Meta:
        db_table = 'record_template'
        verbose_name = '病例模板'
        indexes = [models.Index(fields=['id'])]