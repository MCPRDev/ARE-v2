from datetime import datetime
import re
import uuid

def document_id_validation(document):
    if not isinstance(document, str):
        return False

    patron = r"^\d{3}-\d{6}-\d{4}[A-Z]$"
    if re.match(patron, document):
        return True
    else:
        return False

def id_validation(id):
    if not isinstance(id, int):
        return False
    else:
        return True
    
def student_code_validation(student_code):
    if not isinstance(student_code, str):
        return False
    
    match len(student_code):
        case 19:
            patron = r"^[A-Z]{4}-\d{6}-\d{7}$"
        case 18:
            patron = r"^[A-Z]{3}-\d{6}-\d{7}$"
        case 17:
            patron = r"^[A-Z]{2}-\d{6}-\d{7}$"
        case _:
            return False
    
    return re.match(patron, student_code) is not None

def phone_number_validation(phone_number):
    patron = r"^\d{4}-\d{4}"
    if re.match(patron, phone_number): 
        return True
    else:
        return False

def code_center_generator(student_code, student_total):
    try:
        first_code_part = student_code.split('-')[0]
        register_time = datetime.now().strftime('%d%m%y%H%M%S')
        unique_id = str(int(uuid.uuid4().int) % (10**8))
        student_center_code = f"{first_code_part}-{register_time}-{student_total}-{unique_id}"
        return student_center_code
    except Exception as e:
        print(f"Error generating code center: {e}")
        return None

def validate_date(date):
    if not isinstance(date, str):
        return False
    
    patron = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(patron, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    else:
        return False