import tenseal as ts
import utils
import json
import base64

class DataDecryptor:
    def __init__(self, secret_key_file="keys/secret.txt"):
        self.context = ts.context_from(utils.read_data(secret_key_file))

    def decrypt_salary(self, encrypted_salary):
        salary = ts.lazy_ckks_vector_from(base64.b64decode(encrypted_salary))
        salary.link_context(self.context)
        return round(salary.decrypt()[0], 2)

    def decrypt_data(self, input_json="updated_encrypted_json.json", output_json="updated_encrypted_json_final.json"):
        with open(input_json, 'r') as file:
            data = json.load(file)

        decrypted_records = []
        for record in data:
            encrypted_salary = record['Encrypted Salary with Bonus']
            record.pop("Encrypted Salary with Bonus", None)
            salary_decrypted = self.decrypt_salary(encrypted_salary)
            record['Final Salary'] = salary_decrypted
            decrypted_records.append(record)

        # Write the updated data to a new JSON file
        with open(output_json, 'w') as file:
            json.dump(decrypted_records, file, indent=2)

        print(f'Data with decrypted salaries written to: {output_json}')

# Usage
if __name__ == "__main__":
    decryptor = DataDecryptor()
    decryptor.decrypt_data()
