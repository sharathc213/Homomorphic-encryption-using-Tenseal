import tenseal as ts
import json
import base64
import utils

class DataEncryptor:
    def __init__(self, secret_key_file="keys/secret.txt"):
        self.context = ts.context_from(utils.read_data(secret_key_file))

    def encrypt_data(self, salary):
        salary_encrypted = ts.ckks_vector(self.context, [salary])
        serialized_encrypted = base64.b64encode(salary_encrypted.serialize()).decode('utf-8')
        return serialized_encrypted

    def process_data(self, input_json="employee_dataset.json", output_json="output_json.json"):
        with open(input_json, 'r') as file:
            data = json.load(file)

        encrypted_records = []
        for record in data:
            salary = record['Salary']
            record.pop("Salary", None)
            salary_encrypted = self.encrypt_data(salary)
            record['Encrypted Salary'] = salary_encrypted
            encrypted_records.append(record)

        # Write the updated data to a new JSON file
        with open(output_json, 'w') as file:
            json.dump(encrypted_records, file, indent=2)

        print(f'Data with encrypted salaries written to: {output_json}')

# Usage
if __name__ == "__main__":
    encryptor = DataEncryptor()
    encryptor.process_data()
