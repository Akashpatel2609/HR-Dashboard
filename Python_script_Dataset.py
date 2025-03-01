import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import uuid
from faker import Faker

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)
fake = Faker()
Faker.seed(42)

def generate_hr_dataset(num_records=8950):
    """
    Generate a realistic HR dataset with specified attributes and probabilities using Faker.
    
    Args:
        num_records (int): Number of records to generate.
        
    Returns:
        pandas.DataFrame: Generated HR dataset.
    """
    
    # Define states and their major cities
    states_and_cities = {
        'California': ['Los Angeles', 'San Francisco', 'San Diego', 'Sacramento', 'San Jose'],
        'Texas': ['Houston', 'Austin', 'Dallas', 'San Antonio', 'Fort Worth'],
        'New York': ['New York City', 'Buffalo', 'Rochester', 'Syracuse', 'Albany'],
        'Florida': ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee'],
        'Illinois': ['Chicago', 'Springfield', 'Peoria', 'Naperville', 'Rockford'],
        'Pennsylvania': ['Philadelphia', 'Pittsburgh', 'Harrisburg', 'Allentown', 'Erie'],
        'Ohio': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron'],
        'Georgia': ['Atlanta', 'Savannah', 'Augusta', 'Athens', 'Macon'],
        'North Carolina': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem'],
        'Michigan': ['Detroit', 'Grand Rapids', 'Ann Arbor', 'Lansing', 'Flint']
    }
    
    # Define departments with their probabilities
    departments = {
        'Sales': 0.25,
        'Engineering': 0.20,
        'Marketing': 0.15,
        'Finance': 0.12,
        'Human Resources': 0.08,
        'Operations': 0.10,
        'IT': 0.10
    }
    
    # Define job titles by department with probabilities
    job_titles = {
        'Sales': {
            'Sales Representative': 0.45,
            'Sales Manager': 0.25,
            'Account Executive': 0.15,
            'Sales Director': 0.10,
            'VP of Sales': 0.05
        },
        'Engineering': {
            'Software Engineer': 0.40,
            'Senior Software Engineer': 0.25,
            'Engineering Manager': 0.15,
            'QA Engineer': 0.10,
            'Engineering Director': 0.10
        },
        'Marketing': {
            'Marketing Specialist': 0.35,
            'Digital Marketing Manager': 0.25,
            'Content Writer': 0.20,
            'Marketing Director': 0.10,
            'CMO': 0.10
        },
        'Finance': {
            'Financial Analyst': 0.35,
            'Accountant': 0.30,
            'Finance Manager': 0.20,
            'Controller': 0.10,
            'CFO': 0.05
        },
        'Human Resources': {
            'HR Specialist': 0.40,
            'Recruiter': 0.30,
            'HR Manager': 0.20,
            'HR Director': 0.10
        },
        'Operations': {
            'Operations Analyst': 0.30,
            'Project Manager': 0.30,
            'Operations Manager': 0.25,
            'Director of Operations': 0.10,
            'COO': 0.05
        },
        'IT': {
            'IT Support Specialist': 0.30,
            'Systems Administrator': 0.25,
            'Network Engineer': 0.20,
            'IT Manager': 0.15,
            'CTO': 0.10
        }
    }
    
    # Define education levels by job title
    education_mapping = {
        # Sales
        'Sales Representative': ['Bachelor\'s Degree', 'High School', 'Associate\'s Degree'],
        'Sales Manager': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Account Executive': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Sales Director': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'VP of Sales': ['Master\'s Degree', 'Bachelor\'s Degree', 'PhD'],
        
        # Engineering
        'Software Engineer': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Senior Software Engineer': ['Bachelor\'s Degree', 'Master\'s Degree', 'PhD'],
        'Engineering Manager': ['Master\'s Degree', 'Bachelor\'s Degree', 'PhD'],
        'QA Engineer': ['Bachelor\'s Degree', 'Associate\'s Degree'],
        'Engineering Director': ['Master\'s Degree', 'PhD'],
        
        # Marketing
        'Marketing Specialist': ['Bachelor\'s Degree', 'Associate\'s Degree'],
        'Digital Marketing Manager': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Content Writer': ['Bachelor\'s Degree', 'High School', 'Associate\'s Degree'],
        'Marketing Director': ['Master\'s Degree', 'Bachelor\'s Degree'],
        'CMO': ['Master\'s Degree', 'PhD', 'Bachelor\'s Degree'],
        
        # Finance
        'Financial Analyst': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Accountant': ['Bachelor\'s Degree'],
        'Finance Manager': ['Master\'s Degree', 'Bachelor\'s Degree'],
        'Controller': ['Master\'s Degree', 'Bachelor\'s Degree'],
        'CFO': ['Master\'s Degree', 'PhD', 'Bachelor\'s Degree'],
        
        # Human Resources
        'HR Specialist': ['Bachelor\'s Degree', 'Associate\'s Degree'],
        'Recruiter': ['Bachelor\'s Degree', 'Associate\'s Degree'],
        'HR Manager': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'HR Director': ['Master\'s Degree', 'Bachelor\'s Degree'],
        
        # Operations
        'Operations Analyst': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Project Manager': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Operations Manager': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'Director of Operations': ['Master\'s Degree', 'Bachelor\'s Degree'],
        'COO': ['Master\'s Degree', 'PhD', 'Bachelor\'s Degree'],
        
        # IT
        'IT Support Specialist': ['Associate\'s Degree', 'Bachelor\'s Degree', 'High School'],
        'Systems Administrator': ['Bachelor\'s Degree', 'Associate\'s Degree'],
        'Network Engineer': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'IT Manager': ['Bachelor\'s Degree', 'Master\'s Degree'],
        'CTO': ['Master\'s Degree', 'PhD', 'Bachelor\'s Degree']
    }
    
    # Define salary ranges by department and job title
    salary_ranges = {
        'Sales': {
            'Sales Representative': (45000, 65000),
            'Sales Manager': (70000, 95000),
            'Account Executive': (60000, 80000),
            'Sales Director': (100000, 130000),
            'VP of Sales': (140000, 180000)
        },
        'Engineering': {
            'Software Engineer': (80000, 120000),
            'Senior Software Engineer': (110000, 150000),
            'Engineering Manager': (130000, 170000),
            'QA Engineer': (70000, 95000),
            'Engineering Director': (150000, 190000)
        },
        'Marketing': {
            'Marketing Specialist': (50000, 70000),
            'Digital Marketing Manager': (80000, 110000),
            'Content Writer': (45000, 65000),
            'Marketing Director': (120000, 150000),
            'CMO': (170000, 220000)
        },
        'Finance': {
            'Financial Analyst': (65000, 90000),
            'Accountant': (60000, 85000),
            'Finance Manager': (100000, 130000),
            'Controller': (120000, 150000),
            'CFO': (180000, 230000)
        },
        'Human Resources': {
            'HR Specialist': (50000, 70000),
            'Recruiter': (55000, 75000),
            'HR Manager': (90000, 120000),
            'HR Director': (130000, 160000)
        },
        'Operations': {
            'Operations Analyst': (60000, 85000),
            'Project Manager': (80000, 110000),
            'Operations Manager': (100000, 130000),
            'Director of Operations': (140000, 170000),
            'COO': (180000, 230000)
        },
        'IT': {
            'IT Support Specialist': (50000, 70000),
            'Systems Administrator': (70000, 90000),
            'Network Engineer': (80000, 110000),
            'IT Manager': (110000, 140000),
            'CTO': (170000, 220000)
        }
    }
    
    # Define hire date probabilities by year
    hire_year_probs = {
        2015: 0.05,
        2016: 0.06,
        2017: 0.08,
        2018: 0.10,
        2019: 0.12,
        2020: 0.13,
        2021: 0.14,
        2022: 0.13,
        2023: 0.11,
        2024: 0.08
    }
    
    # Define termination date probabilities (for 11.2% of employees)
    term_year_probs = {
        2015: 0.02,
        2016: 0.03,
        2017: 0.04,
        2018: 0.06,
        2019: 0.09,
        2020: 0.13,
        2021: 0.15,
        2022: 0.17,
        2023: 0.18,
        2024: 0.13
    }
    
    # Initialize empty lists for each attribute
    employee_ids = []
    first_names = []
    last_names = []
    genders = []
    states = []
    cities = []
    hire_dates = []
    departments_list = []
    job_titles_list = []
    education_levels = []
    performance_ratings = []
    overtime_list = []
    salaries = []
    birth_dates = []
    termination_dates = []
    adjusted_salaries = []
    
    # Generate data for each record
    for _ in range(num_records):
        # Employee ID (using uuid for uniqueness)
        employee_id = f"EMP{str(uuid.uuid4())[:8].upper()}"
        employee_ids.append(employee_id)
        
        # Gender (46% Female, 54% Male)
        gender = np.random.choice(['Female', 'Male'], p=[0.46, 0.54])
        genders.append(gender)
        
        # First Name and Last Name based on gender
        if gender == 'Female':
            first_name = fake.first_name_female()
        else:
            first_name = fake.first_name_male()
        last_name = fake.last_name()
        
        first_names.append(first_name)
        last_names.append(last_name)
        
        # State and City
        state = random.choice(list(states_and_cities.keys()))
        city = random.choice(states_and_cities[state])
        states.append(state)
        cities.append(city)
        
        # Department
        dept_choices = list(departments.keys())
        dept_probs = list(departments.values())
        department = np.random.choice(dept_choices, p=dept_probs)
        departments_list.append(department)
        
        # Job Title
        job_choices = list(job_titles[department].keys())
        job_probs = list(job_titles[department].values())
        job_title = np.random.choice(job_choices, p=job_probs)
        job_titles_list.append(job_title)
        
        # Education Level based on job title
        education_options = education_mapping[job_title]
        education_level = random.choice(education_options)
        education_levels.append(education_level)
        
        # Hire Date
        hire_year = np.random.choice(
            list(hire_year_probs.keys()),
            p=list(hire_year_probs.values())
        )
        # Generate a random date in the given year
        start_date = datetime(hire_year, 1, 1)
        end_date = datetime(hire_year, 12, 31)
        hire_date = fake.date_between_dates(start_date, end_date)
        hire_dates.append(hire_date)
        
        # Performance Rating
        performance_rating = np.random.choice(
            ['Excellent', 'Good', 'Satisfactory', 'Needs Improvement'],
            p=[0.25, 0.45, 0.20, 0.10]
        )
        performance_ratings.append(performance_rating)
        
        # Overtime
        overtime = np.random.choice(['Yes', 'No'], p=[0.30, 0.70])
        overtime_list.append(overtime)
        
        # Salary based on department and job title
        min_salary, max_salary = salary_ranges[department][job_title]
        salary = round(random.uniform(min_salary, max_salary), -3)  # Round to nearest thousand
        salaries.append(salary)
        
        # Birth Date (based on job title and ensuring consistency with hire date)
        # C-level and director roles typically need more experience
        if any(title in job_title for title in ['VP', 'Director', 'CMO', 'CFO', 'CTO', 'COO']):
            # Age between 35-60 at hire
            min_age_at_hire = 35
            max_age_at_hire = 60
        elif 'Manager' in job_title:
            # Age between 30-55 at hire
            min_age_at_hire = 30
            max_age_at_hire = 55
        elif 'Senior' in job_title:
            # Age between 28-50 at hire
            min_age_at_hire = 28
            max_age_at_hire = 50
        else:
            # Age between 22-45 at hire
            min_age_at_hire = 22
            max_age_at_hire = 45
        
        age_at_hire = random.randint(min_age_at_hire, max_age_at_hire)
        # Calculate birth date based on hire date and age
        birth_date = hire_date - timedelta(days=365 * age_at_hire + random.randint(0, 364))
        birth_dates.append(birth_date)
        
        # Termination Date (11.2% of employees)
        is_terminated = random.random() < 0.112  # 11.2% termination rate
        
        if is_terminated:
            # Ensure termination date is at least 6 months after hire date
            min_term_date = hire_date + timedelta(days=180)
            
            # Check if minimum termination date is beyond 2024
            if min_term_date.year > 2024:
                term_date = None  # No termination if hire date is too recent
            else:
                # Find eligible years for termination
                eligible_years = [year for year in term_year_probs.keys() if year >= min_term_date.year]
                if not eligible_years:
                    term_date = None
                else:
                    # Adjust probabilities for eligible years
                    eligible_probs = [term_year_probs[year] for year in eligible_years]
                    # Normalize probabilities
                    eligible_probs = [p/sum(eligible_probs) for p in eligible_probs]
                    
                    term_year = np.random.choice(eligible_years, p=eligible_probs)
                    
                    # Generate termination date
                    if term_year == min_term_date.year:
                        # If same year as min termination date, use date between min and year end
                        term_date = fake.date_between_dates(min_term_date, datetime(term_year, 12, 31))
                    else:
                        # If different year, use any date in that year
                        term_date = fake.date_between_dates(datetime(term_year, 1, 1), datetime(term_year, 12, 31))
        else:
            term_date = None
        
        termination_dates.append(term_date)
        
        # Adjusted Salary (based on gender, education, and age)
        # Start with base salary
        adjusted = salary
        
        # Apply gender adjustment (subtle pay gap)
        if gender == 'Female':
            adjusted *= 0.97  # 3% less on average
        
        # Education level adjustment
        if education_level == 'PhD':
            adjusted *= 1.08
        elif education_level == 'Master\'s Degree':
            adjusted *= 1.05
        elif education_level == 'Bachelor\'s Degree':
            adjusted *= 1.03
        
        # Age/experience adjustment
        age = (datetime(2024, 1, 1).date() - birth_date).days // 365
        if age >= 50:
            adjusted *= 1.02
        elif age >= 40:
            adjusted *= 1.01
        
        # Round to nearest thousand
        adjusted = round(adjusted, -3)
        adjusted_salaries.append(adjusted)
    
    # Create DataFrame
    df = pd.DataFrame({
        'EmployeeID': employee_ids,
        'FirstName': first_names,
        'LastName': last_names,
        'Gender': genders,
        'State': states,
        'City': cities,
        'HireDate': hire_dates,
        'Department': departments_list,
        'JobTitle': job_titles_list,
        'EducationLevel': education_levels,
        'PerformanceRating': performance_ratings,
        'Overtime': overtime_list,
        'BaseSalary': salaries,
        'BirthDate': birth_dates,
        'TerminationDate': termination_dates,
        'AdjustedSalary': adjusted_salaries
    })
    
    # Format dates as strings
    df['HireDate'] = pd.to_datetime(df['HireDate']).dt.strftime('%Y-%m-%d')
    df['BirthDate'] = pd.to_datetime(df['BirthDate']).dt.strftime('%Y-%m-%d')
    df['TerminationDate'] = df['TerminationDate'].apply(lambda x: x.strftime('%Y-%m-%d') if x is not None else None)
    
    # Calculate additional metrics that might be useful
    today = datetime.now().date()
    reference_date = pd.Timestamp(today)
    df['Age'] = ((reference_date - pd.to_datetime(df['BirthDate'])).dt.days // 365).astype(int)
    
    # Calculate years of service
    term_or_today = df['TerminationDate'].fillna(today.strftime('%Y-%m-%d'))
    df['YearsOfService'] = ((pd.to_datetime(term_or_today) - pd.to_datetime(df['HireDate'])).dt.days // 365).astype(int)
    
    df['IsActive'] = df['TerminationDate'].isnull()
    
    # Add employee emails
    df['Email'] = df.apply(lambda row: f"{row['FirstName'].lower()}.{row['LastName'].lower()}@company.com", axis=1)
    
    # Add phone numbers using faker
    df['PhoneNumber'] = [fake.phone_number() for _ in range(len(df))]
    
    return df

# Generate the dataset
hr_data = generate_hr_dataset(8950)

# Save to CSV
hr_data.to_csv('hr_dataset.csv', index=False)

print(f"HR dataset with {len(hr_data)} records has been generated and saved to 'hr_dataset.csv'")
print("\nDataset Overview:")
print(hr_data.head())
print("\nSummary Statistics:")
print(hr_data.describe(include='all'))

# Additional data quality checks
print("\nGender Distribution:")
print(hr_data['Gender'].value_counts(normalize=True))

print("\nDepartment Distribution:")
print(hr_data['Department'].value_counts(normalize=True))

print("\nEducation Level Distribution:")
print(hr_data['EducationLevel'].value_counts(normalize=True))

print("\nTermination Rate:")
print(f"{(~hr_data['TerminationDate'].isnull()).mean() * 100:.2f}%")