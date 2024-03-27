from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Plan
from .serializers import PlanSerializer


@csrf_exempt
def create_plan(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = PlanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def list_plans(request):
    if request.method == 'GET':
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return JsonResponse(serializer.data, safe=False)
