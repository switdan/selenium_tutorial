from generator_emails import GeneratorEmails

class Gender:
    MALE = 0
    FEMALE = 1

class TestData:
    DATA_EMAIL = GeneratorEmails().generate_email()
    DATA_GENDER = Gender.MALE
    DATA_FIRST_NAME = "Janusz"
    DATA_LAST_NAME = "Kowalski"
    DATA_PASSWORD = "12345678!"
    DATA_DAY_OF_BIRTH = 7
    DATA_DAY_OF_MONTH = 2
    DATA_DAY_OF_YEAR = 1990