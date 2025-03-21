from datetime import datetime, date, time
import re
import uuid
import bcrypt
from Levenshtein import distance as levenshtein_distance


#OutFuctions for query#
#Validation for entry username
def is_valid_username(username):
    return bool(re.match(r"^\w+$", username))

#Validation for entry password
def is_valid_password(password):
    return len(password) >= 12

#bcryp hash password
def hashing_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

#check input password with hasshed_password
def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

#verify document id
def document_id_validation(document):
    if not isinstance(document, str):
        return False

    patron = r"^\d{3}-\d{6}-\d{4}[A-Z]$"
    if re.match(patron, document):
        return True
    else:
        return False

#if not document_id_validation then rewrite it
def rewrite_document_id(document_id):
    if len(document_id) != 14:
        return "Formato inválido"

    document_id = document_id[:-1] + document_id[-1].upper()

    return f"{document_id[:3]}-{document_id[3:9]}-{document_id[9:]}"


def id_validation(id):
    if not isinstance(id, int):
        return False
    else:
        return True

#There are differents students code, sometimes they don't have a middle name or second surname, so the len(student_code) is different    
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

#just verify the phone number's lenght 
def phone_number_validation(phone_number):
    if not isinstance(phone_number, str):
        return False
    
    patron = r"^\d{8}"

    if re.match(patron, phone_number): 
        return True
    else:
        return False
    
def string_input_data_validator(data):
    if not isinstance(data, str) or not data.isalpha():
        if data is None:
            return True
        return False
    return True

def age_validator(age):
    if not isinstance(age, int) or age < 18 or age > 90:
        return False
    return True

#If not phone_number so, rewrite
def rewrite_phone_number(phone_number: str) -> str:
    if len(phone_number) != 8:
        return False
    
    return f"{phone_number[:4]}-{phone_number[4:]}"

#We use code generator for students, this is unique code for the center, is not like the student code use for the nacional register
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

def validate_grade(grade):
    if not isinstance(grade, int) or grade < 0 or grade > 11:
        return False
    
    return True

def validate_and_clean_subject_entry_query(subject):
    if not isinstance(subject, str):
        return False
    
    subject = subject.strip()
    if len(subject) > 50:
        subject = subject[:50]
    
    return subject.upper()

def validate_data_entry_no_repeted(data_entry, existing_data, umbral=2):
    for i in existing_data:
        if levenshtein_distance(data_entry.upper(), i.upper()) <= umbral:
            return False
    return True


#############Specific Edit staff widget fuctions########
def verify_date_edit(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    minimun_date = datetime(1900, 1, 1).date()
    current_date = datetime.today().date()

    if date < minimun_date:
        return False
    
    if date == current_date:
        return False
    
    return True

def calculate_age_edited(date_input):

    if isinstance(date_input, str):
        birthdate = datetime.strptime(date_input, "%Y-%m-%d").date()

    elif isinstance(date_input, date):
        birthdate = date_input
    else:
        raise TypeError("El argumento debe ser una cadena de texto en formato 'YYYY-MM-DD' o un objeto datetime.date")
    
    today = datetime.today().date()
    
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return age

def clear_entry_data(data):
    if not isinstance(data, str):
        return False
    
    return data.strip()

##############Specific Impart time assigned widget########

def verify_start_time(start_time):
    if isinstance (start_time, time):
        if start_time.hour < 7 or start_time.hour > 18:
            return False
        else:
            return True
    
    elif isinstance(start_time, str):
        try:
            start_time = datetime.strptime(start_time, "%H:%M:%S").time()
            if start_time.hour < 7 or start_time.hour > 18:
                return False
            else:
                return True
        except ValueError:
            return False

def verify_end_time(end_time):
    if isinstance (end_time, time):
        if end_time.hour < 7 or end_time.hour > 18:
            return False
        else:
            return True
    
    elif isinstance(end_time, str):
        try:
            end_time = datetime.strptime(end_time, "%H:%M:%S").time()
            if end_time.hour < 7 or end_time.hour > 18:
                return False
            else:
                return True
        except ValueError:
            return False
        
    else:
        return False

def verify_start_end_tiem(start_time, end_time):
    if isinstance(start_time, time) and isinstance(end_time, time):
        if start_time >= end_time:
            return False
        else:
            return True
    
    elif isinstance(start_time, str) and isinstance(end_time, str):
        try:
            start_time = datetime.strptime(start_time, "%H:%M:%S").time()
            end_time = datetime.strptime(end_time, "%H:%M:%S").time()
            if start_time >= end_time:
                return False
            else:
                return True
        except ValueError:
            return False
    else:
        return False