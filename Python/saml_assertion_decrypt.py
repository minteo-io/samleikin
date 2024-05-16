from lxml import etree
import xmlsec

# Path to the file where you want to read
in_file_path = "./saml.xml"

# Path to the file where you want to write the string
out_file_path = "./saml_out.xml"

# Path to the file where you want to read the private key
private_key_file = "key.pem"

# --------------------------------------------

# Load the SAML response XML
xml_tree = etree.parse(in_file_path)

# Extract the EncryptedAssertion node
namespaces = {
    "assertion": "urn:oasis:names:tc:SAML:2.0:assertion",
    "xmlenc": "http://www.w3.org/2001/04/xmlenc#"
}
encrypted_assertion = xml_tree.find(".//assertion:EncryptedAssertion", namespaces)
if encrypted_assertion is None:
    raise ValueError("EncryptedAssertion not found in the SAML response.")

# Load the private key
keys_manager = xmlsec.KeysManager()
key = xmlsec.Key.from_file(private_key_file, xmlsec.KeyFormat.PEM, None)
keys_manager.add_key(key)

# Create a Decryption Context
decryptor = xmlsec.EncryptionContext(keys_manager)

# Find the EncryptedData node
enc_data = encrypted_assertion.find(".//xmlenc:EncryptedData", namespaces)
if enc_data is None:
    raise ValueError("EncryptedData not found within the EncryptedAssertion.")
 
# Decrypt the EncryptedData node
decrypted_data = decryptor.decrypt(enc_data)

decrypted_data_str = etree.tostring(decrypted_data, pretty_print=True, encoding="unicode")

# Open the file in write mode ("w") and write the string to it
with open(out_file_path, "w") as file:
    file.write(decrypted_data_str)
