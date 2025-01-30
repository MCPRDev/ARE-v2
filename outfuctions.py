from datetime import datetime
import re

def document_id_validation(document):
    patron = r"^\d{3}-\d{6}-\d{4}[A-Z]$"
    if re.match(patron, document):
        return True
    else:
        return False


def phone_number_validation(phone_number):
    patron = r"^\d{4}-\d{4}"
    if re.match(patron, phone_number):
        return True
    else:
        return False
