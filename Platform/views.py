from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import datetime


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


class ScientistLogin(APIView):
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


class ScientistRegister(APIView):
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
            ans.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'age': i.age, 'birthdate': i.birthdate,
                        'region': i.region, 'education': i.education, 'phone': i.phone, 'ApoE': i.ApoE, 'MMSE': i.MMSE,
                        'CDR_Global': i.CDR_Global, 'CDR_SOB': i.CDR_SOB, 'ADAS_Cog': i.ADAS_Cog, 'MRI': i.MRI,
                        'PET': i.PET})
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
            if i.whetherPublic == '是':
                ans.append(
                    {'id': i.id, 'name': i.name, 'startTime': i.startTime, 'endTime': i.endTime, 'content': i.result,
                     'state': i.state})
        return Response(ans)


class publicEstablishDiagnosis(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        description = str(request.GET.get('describe', None))
        disorder = str(request.GET.get('disorder', None))
        state = str(request.GET.get('state', None))
        taskName = str(request.GET.get('taskName', None))
        data = str(request.GET.get('data', None))
        model = str(request.GET.get('model', None))
        missionNum = DiagnosisMission.objects.all().count()
        res = Public.objects.get(id=userName)
        patientName = ''
        for i in res:
            patientName = i.name
        diagnosisMission = DiagnosisMission(id=missionNum + 1, name=taskName, patient_id=userName,
                                            patient_name=patientName, researcherEstablish='否', whetherPublic=state,
                                            startTime=datetime.datetime.now(), description=description, state='未完成',
                                            data=data, model=model, result='', scene=disorder)
        diagnosisMission.save()
        return Response(0)


class publicLaunchPridict(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        disorder = str(request.GET.get('disorder', None))
        introduction = str(request.GET.get('introduction', None))
        taskName = str(request.GET.get('taskName', None))
        missonNum = PredictMission.objects.all().count()
        data = str(request.GET.get('data', None))
        model = str(request.GET.get('model', None))
        res = Public.objects.get(id=userName)
        patientName = ''
        for i in res:
            patientName = i.name
        predictMission = PredictMission(id=missonNum + 1, name=taskName, patient_id=userName, patient_name=patientName,
                                        researcherEstablish='否', whetherPublic='否', startTime=datetime.datetime.now(),
                                        state='未完成', description=introduction, data=data, model=model, risk='',
                                        scene=disorder)
        predictMission.save()
        return Response(0)


class getPublicPredictList(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        res = PredictMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            if i.whetherPublic == '是':
                ans.append({'id': i.id, 'name': i.name, 'startTime': i.startTime, 'endTime': i.endTime, 'risk': i.risk,
                            'state': i.state})
        return Response(ans)


class getPublicRecmmendation(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        res = PlanRecommendMission.objects.filter(patient_id=userName)
        ans = []
        for i in res:
            if i.state == '是':
                ans.append({'推荐方案': i.plan})
        return Response(ans)


class getDatasetList(APIView):
    def get(self, request):
        res = Data.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'ownerID': i.ownerID, 'ownerName': i.ownerName, 'time': i.time,
                        'size': i.size, 'scenes': i.scene, 'introduction': i.description})
        return Response(ans)


class uploadDataset(APIView):
    def get(self, request):
        name = str(request.GET.get('name', None))
        introduction = str(request.GET.get('introduction', None))
        scene = str(request.GET.get('scene', None))
        model = str(request.GET.get('model', None))
        datasetNum = Data.objects.all().count()
        dataLoad = request.FILES.get('file')
        size = dataLoad.size
        data = Data(id=datasetNum + 1, name=name, scene=scene, description=introduction, model=model, data=dataLoad,
                    time=datetime.datetime.now(), size=size)
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
            ans.append({'id': i.id, 'name': i.name, 'type': i.type, 'ownerID': i.ownerID, 'ownerName': i.ownerName,
                        'time': datetime.datetime.now(), 'scenes': i.scene, 'data': i.data,
                        'introduction': i.description})
        return Response(ans)


class getPatientsList(APIView):
    def get(self, request):
        res = Public.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'gender': i.gender, 'age': i.age, 'birthdate': i.birthdate,
                        'region': i.region, 'education': i.education, 'phone': i.phone, 'ApoE': i.ApoE, 'MMSE': i.MMSE,
                        'CDR_Global': i.CDR_Global, 'CDR_SOB': i.CDR_SOB, 'ADAS_Cog': i.ADAS_Cog, 'MRI': i.MRI,
                        'PET': i.PET})
        return Response(ans)


class getPatientAssistantTask(APIView):
    def get(self, request):
        patientID = str(request.GET.get('patientID', None))
        res = DiagnosisMission.objects.filter(patient_id=patientID)
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'state': i.state, 'startTime': i.startTime, 'endTime': i.endTime,
                        'introduction': i.description, 'scene': i.scene, 'data': i.data, 'model': i.model,
                        'result': i.result})
        return Response(ans)


class getBoardsList(APIView):
    def get(self, request):
        res = RecordTemplate.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'doctorID': i.ownerID, 'doctorName': i.ownerName, 'time': i.time,
                        'introduction': i.description})
        return Response(ans)


class uploadBoard(APIView):
    def get(self, request):
        userID = str(request.GET.get('userName', None))
        boardName = str(request.GET.get('boardName', None))
        boardScene = str(request.GET.get('boardScene', None))
        boardTime = str(request.GET.get('boardTime', None))
        boardIntroduction = str(request.GET.get('boardIntroduction', None))
        boardData = request.FILES.get('file')
        res = Doctor.objects.get(id=userID)
        userName = ''
        for i in res:
            userName = i.name
        boardNum = RecordTemplate.objects.all().count()
        board = RecordTemplate(id=boardNum + 1, name=boardName, ownerID=userID, ownerName=userName, time=boardTime,
                               scene=boardScene, description=boardIntroduction, data=boardData)
        board.save()
        return Response(0)


class deleteBoard(APIView):
    def get(self, request):
        id = str(request.GET.get('id', None))
        board = RecordTemplate.objects.get(id=id)
        board.delete()
        return Response(0)


class getDiagnosisTaskList(APIView):
    def get(self, request):
        res = DiagnosisMission.objects.all()
        ans = []
        for i in res:
            ans.append(
                {'id': i.id, 'name': i.name, 'patientID': i.patient_id, 'patientName': i.patient_name, 'state': i.state,
                 'notifyResultState': i.whetherPublic, 'startTime': i.startTime, 'endTime': i.endTime,
                 'introduction': i.description, 'scene': i.scene, 'data': i.data, 'model': i.model, 'result': i.result})
        return Response(ans)


class DoctorEstablishDiagnosisTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get('taskName', None))
        taskIntroduction = str(request.GET.get('taskIntroduction', None))
        taskScene = str(request.GET.get('taskScene', None))
        patientID = str(request.GET.get('patientID', None))
        taskData = '1'
        taskModel = '1'
        taskState = '未完成'
        taskNotifyState = '是'
        taskStartTime = datetime.datetime.now()
        taskNum = DiagnosisMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = ''
        for i in res:
            patientName = i.name
        task = DiagnosisMission(id=taskNum + 1, name=taskName, patient_id=patientID, patient_name=patientName,
                                researcherEstablish='否', whetherPublic=taskNotifyState, startTime=taskStartTime,
                                description=taskIntroduction, state=taskState, data=taskData, model=taskModel,
                                result='', scene=taskScene)
        task.save()
        return Response(0)


class DeleteDiagnosisTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get('taskID', None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class updateAssistantNotifyState(APIView):
    def get(self, request):
        taskID = str(request.GET.get('taskID', None))
        notifyResultState = str(request.GET.get('notifyResultState', None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.whetherPublic = notifyResultState
        task.save()
        return Response(0)


class getPredictTaskList(APIView):
    def get(self, request):
        res = PredictMission.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'finishState': i.state, 'patientID': i.patient_id,
                        'patientName': i.patient_name, 'notifyResultState': i.whetherPublic, 'startTime': i.startTime,
                        'endTime': i.endTime, 'introduction': i.description, 'scene': i.scene, 'data': i.data,
                        'model': i.model, 'risk': i.risk})
        return Response(ans)


class DoctorEstablishPredictTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get('taskName', None))
        taskIntroduction = str(request.GET.get('taskIntroduction', None))
        taskScene = str(request.GET.get('taskScene', None))
        patientID = str(request.GET.get('patientID', None))
        taskScene = str(request.GET.get('taskScene', None))
        taskDataset = str(request.GET.get('taskDataset', None))
        taskModel = str(request.GET.get('taskModel', None))
        taskNotifyState = '否'
        taskStartTime = datetime.datetime.now()
        taskState = '未完成'
        patientName = ''
        taskNum = PredictMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        for i in res:
            patientName = i.name
        task = PredictMission(id=taskNum + 1, name=taskName, patient_id=patientID, patient_name=patientName,
                              researcherEstablish='否', whetherPublic=taskNotifyState, startTime=taskStartTime,
                              state=taskState, description=taskIntroduction, data=taskDataset, model=taskModel, risk='',
                              scene=taskScene)
        task.save()


class updatePredictState(APIView):
    def get(self, request):
        taskID = str(request.GET.get('taskID', None))
        notifyPredictState = str(request.GET.get('notifyPredictState', None))
        task = PredictMission.objects.get(id=taskID)
        task.state = notifyPredictState
        task.save()


class getRecommendationTaskList(APIView):
    def get(self, request):
        res = PlanRecommendMission.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'state': i.state, 'notifySchemeState': i.whetherPublic,
                        'time': i.startTime, 'introduction': i.description, 'scene': i.scene, 'patientID': i.patient_id,
                        'patientName': i.patient_name, 'plan': i.plan})
        return Response(ans)


class updateScheme(APIView):
    def get(self, request):
        taskID = str(request.GET.get('taskID', None))
        scheme = str(request.GET.get('scheme', None))
        task = PlanRecommendMission.objects.get(id=taskID)
        task.plan = scheme
        task.save()
        return Response(0)


class updateSchemeState(APIView):
    def get(self, request):
        taskID = str(request.GET.get('taskID', None))
        notifySchemeState = str(request.GET.get('notifySchemeState', None))
        task = PlanRecommendMission.objects.get(id=taskID)
        task.state = notifySchemeState
        task.save()
        return Response(0)


class establishSchemeTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get('taskName', None))
        taskIntroduction = str(request.GET.get('taskIntroduction', None))
        taskScene = str(request.GET.get('taskScene', None))
        patientID = str(request.GET.get('patientID', None))
        taskNotifyState = '否'
        taskStartTime = datetime.datetime.now()
        taskState = '未完成'
        patientName = ''
        taskDataset = str(request.GET.get('taskDataset', None))
        taskModel = str(request.GET.get('taskModel', None))
        taskNum = PlanRecommendMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        for i in res:
            patientName = i.name
        task = PlanRecommendMission(id=taskNum + 1, name=taskName, patient_id=patientID, patient_name=patientName,
                                    researcherEstablish='否', whetherPublic=taskNotifyState, startTime=taskStartTime,
                                    state=taskState, description=taskIntroduction, data=taskDataset, model=taskModel,
                                    plan='', scene=taskScene)
        task.save()
        return Response(0)


class uploadModel(APIView):
    def get(self, request):
        name = str(request.GET.get('name', None))
        introduction = str(request.GET.get('introduction', None))
        scene = str(request.GET.get('scene', None))
        type = str(request.GET.get('type', None))
        data = str(request.GET.get('data', None))
        modelNum = Model.objects.all().count()
        modelLoad = request.FILES.get('file')
        ownerID = str(request.GET.get('ownerID', None))
        ownerName = str(request.GET.get('ownerName', None))
        model = Model(id=modelNum + 1, name=name, scene=scene, description=introduction, ownerID=ownerID,
                      ownerName=ownerName, type=type, data=data, time=datetime.datetime.now(), model=modelLoad)
        model.save()
        return Response(0)


class getModleList(APIView):
    def get(self, request):
        res = Model.objects.all()
        ans = []
        for i in res:
            ans.append({'id': i.id, 'name': i.name, 'type': i.type, 'ownerID': i.ownerID, 'ownerName': i.ownerName,
                        'time': i.time, 'scenes': i.scene, 'data': i.data, 'introduction': i.description})
        return Response(ans)


class deleteModel(APIView):
    def get(self, request):
        id = str(request.GET.get('id', None))
        model = Model.objects.get(id=id)
        model.delete()
        return Response(0)


class getScientistDignosisTaskList(APIView):
    def get(self, request):
        res = DiagnosisMission.objects.all()
        ans = []
        for i in res:
            if i.researcherEstablish == '是':
                ans.append({'id': i.id, 'name': i.name, 'patientID': i.patient_id, 'patientName': i.patient_name,
                            'state': i.state, 'notifyResultState': i.whetherPublic, 'startTime': i.startTime,
                            'endTime': i.endTime, 'introduction': i.description, 'scene': i.scene, 'data': i.data,
                            'model': i.model, 'result': i.result})
        return Response(ans)


class establishScientistDiagnosisTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get('taskName', None))
        taskIntroduction = str(request.GET.get('taskIntroduction', None))
        taskScene = str(request.GET.get('taskScene', None))
        patientID = str(request.GET.get('patientID', None))
        taskData = '1'
        taskModel = '1'
        taskState = '未完成'
        taskNotifyState = '否'
        taskStartTime = datetime.datetime.now()
        taskNum = DiagnosisMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        patientName = ''
        for i in res:
            patientName = i.name
        task = DiagnosisMission(id=taskNum + 1, name=taskName, patient_id=patientID, patient_name=patientName,
                                researcherEstablish='是', whetherPublic=taskNotifyState, startTime=taskStartTime,
                                description=taskIntroduction, state=taskState, data=taskData, model=taskModel,
                                result='', scene=taskScene)
        task.save()
        return Response(0)


class DeleteScientistDiagnosisTask(APIView):
    def get(self, request):
        taskID = str(request.GET.get('taskID', None))
        task = DiagnosisMission.objects.get(id=taskID)
        task.delete()
        return Response(0)


class getScientistPredictTaskList(APIView):
    def get(self, request):
        res = PredictMission.objects.all()
        ans = []
        for i in res:
            if i.researcherEstablish == '是':
                ans.append({'id': i.id, 'name': i.name, 'finishState': i.state, 'patientID': i.patient_id,
                            'patientName': i.patient_name, 'notifyResultState': i.whetherPublic,
                            'startTime': i.startTime, 'endTime': i.endTime, 'introduction': i.description,
                            'scene': i.scene, 'data': i.data, 'model': i.model, 'risk': i.risk})
        return Response(ans)


class ScientistEstablishPredictTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get('taskName', None))
        taskIntroduction = str(request.GET.get('taskIntroduction', None))
        taskScene = str(request.GET.get('taskScene', None))
        patientID = str(request.GET.get('patientID', None))
        taskScene = str(request.GET.get('taskScene', None))
        taskDataset = str(request.GET.get('taskDataset', None))
        taskModel = str(request.GET.get('taskModel', None))
        taskNotifyState = '否'
        taskStartTime = datetime.datetime.now()
        taskState = '未完成'
        patientName = ''
        taskNum = PredictMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        for i in res:
            patientName = i.name
        task = PredictMission(id=taskNum + 1, name=taskName, patient_id=patientID, patient_name=patientName,
                              researcherEstablish='是', whetherPublic=taskNotifyState, startTime=taskStartTime,
                              state=taskState, description=taskIntroduction, data=taskDataset, model=taskModel, risk='',
                              scene=taskScene)
        task.save()


class getScientistRecommendationTaskList(APIView):
    def get(self, request):
        res = PlanRecommendMission.objects.all()
        ans = []
        for i in res:
            if i.researcherEstablish == '是':
                ans.append({'id': i.id, 'name': i.name, 'state': i.state, 'notifySchemeState': i.whetherPublic,
                            'time': i.startTime, 'introduction': i.description, 'scene': i.scene, 'data': i.data,
                            'model': i.model, 'patientID': i.patient_id, 'patientName': i.patient_name, 'plan': i.plan})
        return Response(ans)


class ScientistEstablishSchemeTask(APIView):
    def get(self, request):
        taskName = str(request.GET.get('taskName', None))
        taskIntroduction = str(request.GET.get('taskIntroduction', None))
        taskScene = str(request.GET.get('taskScene', None))
        patientID = str(request.GET.get('patientID', None))
        taskNotifyState = '否'
        taskStartTime = datetime.datetime.now()
        taskState = '未完成'
        patientName = ''
        taskDataset = str(request.GET.get('taskDataset', None))
        taskModel = str(request.GET.get('taskModel', None))
        taskNum = PlanRecommendMission.objects.all().count()
        res = Public.objects.get(id=patientID)
        for i in res:
            patientName = i.name
        task = PlanRecommendMission(id=taskNum + 1, name=taskName, patient_id=patientID, patient_name=patientName,
                                    researcherEstablish='是', whetherPublic=taskNotifyState, startTime=taskStartTime,
                                    state=taskState, description=taskIntroduction, data=taskDataset, model=taskModel,
                                    plan='', scene=taskScene)
        task.save()
        return Response(0)
