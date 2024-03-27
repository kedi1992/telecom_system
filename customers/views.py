from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.decorators import api_view

from plans.models import Plan
from .models import Customer, Renewal
from .serializers import CustomerSerializer
from django.http import JsonResponse
from .models import Customer, Renewal
from datetime import datetime


# @csrf_exempt
def create_customer(request):
    # return JsonResponse({"data": 123}, status=202)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def create_customer_info(requets):
    return JsonResponse({"data": "test"}, status=202)


def list_customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)


def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer does not exist'}, status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    # Handle other HTTP methods if necessary
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def renew_customer_plan(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer does not exist'}, status=404)

    if request.method == 'POST':
        data = json.loads(request.body)
        renewal_date_str = data.get('renewal_date')
        plan_status = data.get('plan_status')
        try:
            renewal_date = datetime.strptime(renewal_date_str, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid renewal date format. Expected format: YYYY-MM-DD'}, status=400)
        # Validate plan status
        if plan_status not in ['Active', 'Inactive']:
            return JsonResponse({'error': 'Invalid plan status. Must be either "Active" or "Inactive"'}, status=400)
        # Get or create Renewal object for the customer
        renewal, created = Renewal.objects.get_or_create(customer=customer)
        # Update renewal date and plan status
        renewal.renewal_date = renewal_date
        renewal.plan_status = plan_status
        renewal.save()
        return JsonResponse({'success': 'Customer plan renewed successfully'})

    elif request.method == 'GET':
        return JsonResponse({'error': 'GET method not allowed'}, status=405)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def upgrade_downgrade_customer_plan(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer does not exist'}, status=404)

    if request.method == 'POST':
        data = json.loads(request.body)  # Assuming plan upgrade/downgrade data is sent via POST request

        # Extract plan upgrade/downgrade data from the request
        existing_plan_name = data.get('existing_plan_name')
        new_plan_name = data.get('new_plan_name')
        new_plan_cost = data.get('new_plan_cost')
        new_plan_validity = data.get('new_plan_validity')
        new_plan_status = data.get('new_plan_status')

        # Validate that existing plan name matches customer's current plan
        if existing_plan_name != customer.plan.name:
            print("customer.plan.name :: ", customer.plan.name)
            print("existing_plan_name :: ", existing_plan_name)
            return JsonResponse({'error': 'Existing plan name does not match customer\'s current plan'}, status=400)

        print("plna name matched")
        # Validate that new plan name is different from existing plan name
        if new_plan_name == existing_plan_name:
            return JsonResponse({'error': 'New plan name must be different from existing plan name'}, status=400)

        # Validate new plan cost and validity (assuming they are numeric fields)
        if not (new_plan_cost.isdigit() and new_plan_validity.isdigit()):
            return JsonResponse({'error': 'New plan cost and validity must be numeric'}, status=400)

        # Update customer's plan details
        customer.plan.name = new_plan_name
        customer.plan.cost = int(new_plan_cost)
        customer.plan.validity = int(new_plan_validity)
        customer.plan.status = new_plan_status
        customer.save()

        return JsonResponse({'success': 'Customer plan upgraded/downgraded successfully'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)