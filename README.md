# Telecom Customer Management System

## Project Creation Help
1. **Clone the Repository**: `git clone https://github.com/kedi1992/telecom_system.git`
2. **Navigate to the Project Directory**: `cd telecom-customer-management-system`
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Run Migrations**: `python manage.py migrate`
5. **Start the Development Server**: `python manage.py runserver`

## Endpoints
### 1. Create Customer
- **URL**: `/api/customers/create/`
- **Method**: POST
- **Description**: Register a new customer
- **Body Parameters**:
  - `name`: Customer's name
  - `dob`: Date of birth (YYYY-MM-DD)
  - `email`: Customer's email address
  - `aadhar_number`: Aadhar number (12 digits)
  - `registration_date`: Registration date (YYYY-MM-DD)
  - `assigned_mobile_number`: Assigned mobile number (10 digits)
  - `plan`: Plan ID

### 2. List Customers
- **URL**: `/api/customers/list/`
- **Method**: GET
- **Description**: Display a list of all customers

### 3. Renew Customer Plan
- **URL**: `/api/customers/<customer-id>/renew/`
- **Method**: POST
- **Description**: Renew the plan for a specific customer
- **Body Parameters**:
  - `renewal_date`: Renewal date (YYYY-MM-DD)
  - `plan_status`: Plan status (Active/Inactive)

### 4. Upgrade/Downgrade Customer Plan
- **URL**: `/api/customers/<customer-id>/upgrade-downgrade/`
- **Method**: POST
- **Description**: Upgrade or downgrade the plan for a specific customer
- **Body Parameters**:
  - `existing_plan_name`: Existing plan name
  - `new_plan_name`: New plan name
  - `new_plan_cost`: New plan cost
  - `new_plan_validity`: New plan validity
  - `new_plan_status`: New plan status

## Test Cases
1. **Test case 1**: Add a new customer and verify that the server returns a status code 201 (Created).
2. **Test case 2**: Retrieve the list of customers and ensure that the server returns a status code 200 (OK).
3. **Test case 3**: Renew the plan for an existing customer and verify that the renewal date and plan status are updated accordingly.
4. **Test case 4**: Upgrade or downgrade the plan for a customer and verify that the plan details including cost, validity, and status are updated correctly.

