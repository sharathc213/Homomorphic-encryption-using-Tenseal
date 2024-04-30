import tenseal as ts
import utils
import json
import base64

class DataProcessor:
    def __init__(self, public_key_file="keys/public.txt"):
        self.context = ts.context_from(utils.read_data(public_key_file))

    def encrypt_salary(self, salary):
        salary_encrypted = ts.lazy_ckks_vector_from(salary)
        salary_encrypted.link_context(self.context)
        return salary_encrypted

    def encrypt_bonus(self, bonus):
        bonus_encrypted = ts.plain_tensor([bonus])
        return bonus_encrypted

    def process_data(self, input_json="output_json.json", output_json="updated_encrypted_json.json", bonus=600):
        with open(input_json, 'r') as file:
            data = json.load(file)

        bonus_encrypted = self.encrypt_bonus(bonus)

        encrypted_records = []
        for record in data:
            salary = ts.lazy_ckks_vector_from(base64.b64decode(record['Encrypted Salary']))
            record.pop("Encrypted Salary", None)
            salary.link_context(self.context)
            salary_new_encrypted = salary + bonus_encrypted
            record['Encrypted Salary with Bonus'] = base64.b64encode(salary_new_encrypted.serialize()).decode('utf-8')
            encrypted_records.append(record)

        # Write the updated data to a new JSON file
        with open(output_json, 'w') as file:
            json.dump(encrypted_records, file, indent=2)

        print(f'Data with encrypted salaries and bonus written to: {output_json}')

# Usage
if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_data()
