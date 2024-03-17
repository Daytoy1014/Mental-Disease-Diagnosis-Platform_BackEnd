from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


# Create your views here.
class PublicRegister(APIView):
    def get(self, request):
        userNickname = str(request.GET.get('userNickname', None))
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        userPassword2 = str(request.GET.get('userPassword2', None))
        res = Public.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            return Response(1)
        elif userPassword != userPassword2:
            return Response(2)
        else:
            public = Public(id=userName, name=userNickname, password=userPassword)
            public.save()
            return Response(0)


class PublicLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        res = Public.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            if res[0].password == userPassword:
                return Response(0)
            else:
                return Response(1)
        else:
            return Response(2)


class DoctorRegister(APIView):
    def get(self, request):
        userNickname = str(request.GET.get('userNickname', None))
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        userPassword2 = str(request.GET.get('userPassword2', None))
        res = Doctor.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            return Response(1)
        elif userPassword != userPassword2:
            return Response(2)
        else:
            doctor = Doctor(id=userName, name=userNickname, password=userPassword)
            doctor.save()
            return Response(0)

class DoctorLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        res = Doctor.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            if res[0].password == userPassword:
                return Response(0)
            else:
                return Response(1)
        else:
            return Response(2)

class ResearcherRegister(APIView):
    def get(self, request):
        userNickname = str(request.GET.get('userNickname', None))
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        userPassword2 = str(request.GET.get('userPassword2', None))
        res = Researcher.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            return Response(1)
        elif userPassword != userPassword2:
            return Response(2)
        else:
            researcher = Researcher(id=userName, name=userNickname, password=userPassword)
            researcher.save()
            return Response(0)

class ResearcherLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        res = Researcher.objects.filter(id=userName)
        flag = res.exists()
        if flag:
            if res[0].password == userPassword:
                return Response(0)
            else:
                return Response(1)
        else:
            return Response(2)

class getPublicResume(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassword = str(request.GET.get('userPassword', None))
        ans = []
        res = Public.objects.filter(id=userName, password=userPassword)
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'age':i.age, 'birthdate': i.birthdate, 'region': i.region, 'education': i.education, 'phone': i.phone, 'ApoE': i.ApoE, 'MMSE': i.MMSE, 'CDR_Global': i.CDR_Global, 'CDR_SOB': i.CDR_SOB, 'ADAS_Cog': i.ADAS_Cog, 'MRI': i.MRI, 'PET': i.PET})
        return Response(ans)

class publicSaveResume(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userNickname = str(request.GET.get('userNickname', None))
        userGender = str(request.GET.get('userGender', None))
        userAge = str(request.GET.get('userAge', None))
        userBirthdate = str(request.GET.get('userBirthdate', None))
        userRegion = str(request.GET.get('userRegion', None))
        userEducation = str(request.GET.get('userEducation', None))
        userPhone = str(request.GET.get('userPhone', None))
        userApoE = str(request.GET.get('userApoE', None))
        userMMSE = str(request.GET.get('userMMSE', None))
        userCDR_Global = str(request.GET.get('userCDR_Global', None))
        userCDR_SOB = str(request.GET.get('userCDR_SOB', None))
        userADAS_Cog = str(request.GET.get('userADAS_Cog', None))
        userMRI = str(request.GET.get('userMRI', None))
        userPET = str(request.GET.get('userPET', None))
        public = Public.objects.get(id=userName)
        public.name = userNickname
        public.gender = userGender
        public.age = userAge
        public.birthdate = userBirthdate
        public.region = userRegion
        public.education = userEducation
        public.phone = userPhone
        public.ApoE = userApoE
        public.MMSE = userMMSE
        public.CDR_Global = userCDR_Global
        public.CDR_SOB = userCDR_SOB
        public.ADAS_Cog = userADAS_Cog
        public.MRI = userMRI
        public.PET = userPET
        public.save()
        return Response(0)

class getPublicDiagnosisList(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        res = DiagnosisMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'startTime': i.startTime, 'endTime': i.endTime, 'content': i.result, 'state': i.state})
        return Response(ans)

class publicEstablishDiagnosis(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        description = str(request.GET.get('describe', None))
        disorder = str(request.GET.get('disorder', None))
        state = str(request.GET.get('state', None))
        taskName = str(request.GET.get('taskName', None))
        missionNum = DiagnosisMission.objects.all().count()
        diagnosisMission = DiagnosisMission(id=missionNum+1, name=taskName, patient_id=userName,description=description,state=state)
        diagnosisMission.save()
        return Response(0)

class publicLaunchPridict(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        disorder = str(request.GET.get('disorder', None))
        introduction = str(request.GET.get('introduction', None))
        taskName = str(request.GET.get('taskName', None))
        missonNum = PredictMission.objects.all().count()
        predictMission = PredictMission(id=missonNum+1,name=taskName, patient_id=userName)
        predictMission.save()
        return Response(0)

class getPublicPredictList(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        res = PredictMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'startTime': i.startTime, 'endTime': i.endTime, 'risk': i.risk, 'state': i.state})
        return Response(ans)

class getPublicRecmmendation(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        res = PlanRecommendMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            if i.state == '允许查看':
                ans.append({'推荐方案': i.plan})
        return Response(ans)

class getDatasetList(APIView):
    def get(self, request):
        res = Data.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'ownerID': i.ownerID, 'ownerName': i.ownerName, 'time': i.time, 'size': i.size, 'scenes': i.scene, 'introduction': i.description})
        return Response(ans)

class uploadDataset(APIView):
    def get(self, request):
        name = str(request.GET.get('name', None))
        introduction = str(request.GET.get('introduction', None))
        scene = str(request.GET.get('scene', None))
        model = str(request.GET.get('model', None))
        datasetNum = Data.objects.all().count()
        data = Data(id=datasetNum, name=name, scene=scene, description=introduction, model=model, data=request.FILES.get('file'))
        data.save()
        return Response(0)

class DeleteDataset(APIView):
    def get(self, request):
        id = str(request.GET.get('id', None))
        data = Data.objects.get(id=id)
        data.delete()
        return Response(0)

class getModelList(APIView):
    def get(self, request):
        res = Model.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'type': i.type, 'ownerID': i.ownerID, 'ownerName': i.ownerName, 'time': i.time, 'scenes': i.scene,'data': i.data, 'introduction': i.description})
        return Response(ans)

class getPatientsList(APIView):
    def get(self, request):
        res = Public.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'age': i.age, 'birthdate': i.birthdate, 'region': i.region, 'education': i.education, 'phone': i.phone, 'ApoE': i.ApoE, 'MMSE': i.MMSE, 'CDR_Global': i.CDR_Global, 'CDR_SOB': i.CDR_SOB, 'ADAS_Cog': i.ADAS_Cog, 'MRI': i.MRI, 'PET': i.PET})
        return Response(ans)

class getPatientAssistantTask(APIView):
    def get(self, request):
        patientID = str(request.GET.get('patientID', None))
        res = DiagnosisMission.objects.filter(patient_id=patientID)
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'state': i.state, 'startTime': i.startTime, 'endTime': i.endTime, 'introduction': i.description})
        return Response(ans)

class getBoardsList(APIView):
    def get(self, request):
        res = RecordTemplate.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'doctorID': i.ownerID, 'doctorName': i.ownerName, 'time': i.time, 'introduction': i.description})
        return Response(ans)
