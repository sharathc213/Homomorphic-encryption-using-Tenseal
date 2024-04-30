import tenseal as ts
import utils

class TensealContextManager:
    def __init__(self, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60], global_scale=2**40):
        self.context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=poly_modulus_degree, coeff_mod_bit_sizes=coeff_mod_bit_sizes)
        self.context.generate_galois_keys()
        self.context.global_scale = global_scale

    def save_secret_key(self, filename="keys/secret.txt"):
        secret_context = self.context.serialize(save_secret_key=True)
        utils.write_data(filename, secret_context)

    def save_public_key(self, filename="keys/public.txt"):
        self.context.make_context_public()  # drop the secret_key from the context
        public_context = self.context.serialize()
        utils.write_data(filename, public_context)

# Usage
if __name__ == "__main__":
    manager = TensealContextManager()
    manager.save_secret_key()
    manager.save_public_key()
