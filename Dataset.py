from faker import Faker
import random
import json

class EmployeeDatasetGenerator:
    def __init__(self, num_records=10):
        self.fake = Faker()
        self.num_records = num_records
        self.data = []

    def generate_data(self):
        for _ in range(self.num_records):
            name = self.fake.name()
            salary = round(random.uniform(40000, 120000), 2)
            self.data.append({'EmployeeName': name, 'Salary': salary})

    def write_to_json(self, filename='employee_dataset.json'):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f'Dataset with {self.num_records} records created successfully: {filename}')

# Usage
if __name__ == "__main__":
    generator = EmployeeDatasetGenerator(num_records=10)
    generator.generate_data()
    generator.write_to_json()
