import random
import os


class GeneratorNames:
    """
    A class to generate random names based on predefined lists of first and last names.
    Supports both Russian and English names with gender differentiation.
    """
    with open(os.path.dirname(__file__) + '/data_names/russia/male_firstnames.txt') as file:
        russian_male_firstnames = file.read().splitlines()
    with open(os.path.dirname(__file__) + '/data_names/russia/female_firstnames.txt') as file:
        russian_female_firstnames = file.read().splitlines()
    with open(os.path.dirname(__file__) + '/data_names/russia/lastnames.txt') as file:
        russian_lastnames = file.read().splitlines()
    
    with open(os.path.dirname(__file__) + '/data_names/usa/male_firstnames.txt') as file:
        usa_male_firstnames = file.read().splitlines()
    with open(os.path.dirname(__file__) + '/data_names/usa/female_firstnames.txt') as file:
        usa_female_firstnames = file.read().splitlines()
    with open(os.path.dirname(__file__) + '/data_names/usa/lastnames.txt') as file:
        usa_lastnames = file.read().splitlines()
    
    data = {
        'ru': {
            'male_firstnames': russian_male_firstnames,
            'female_firstnames': russian_female_firstnames,
            'lastnames': russian_lastnames,
        },

        'en': {
            'male_firstnames': usa_male_firstnames,
            'female_firstnames': usa_female_firstnames,
            'lastnames': usa_lastnames,
        }
    }

    def __init__(self, save_history: bool = True, format: str = '{firstname} {lastname}'):
        """
        Initializes the GeneratorNames instance.

        :param save_history: Whether to save generated names in history.
        :param format: The format in which names are generated. It should be a string containing
                       placeholders `{firstname}` and `{lastname}`, which will be replaced with
                       the generated first and last names. If set to 'dict', the function will
                       return a dictionary with 'firstname' and 'lastname' keys instead.
        """
        self.format = format
        self.history = []
        self.save_history = save_history
    
    def __repr__(self):
        """
        Returns a string representation of the GeneratorNames instance.

        :return: A string containing save_history status and history size.
        """
        return f"GeneratorNames: save_history={self.save_history}, history_size={len(self.history)}"
    
    def generate_name(self, language: str = 'en', gender: str = 'male'):
        """
        Generates a random name based on the specified language and gender.

        :param language: The language of the name ('en' for English, 'ru' for Russian).
                         Must be one of ['en', 'ru']. If an unsupported language is provided,
                         a ValueError is raised.
        :param gender: The gender of the name ('male' or 'female'). Must be one of ['male', 'female'].
                       If an unsupported gender is provided, a ValueError is raised.
        :return: A randomly generated name in the specified format. If `format` is 'dict', a dictionary
                 with 'firstname' and 'lastname' keys is returned. Otherwise, the name is formatted
                 using the provided string format.
        :raises ValueError: If an unsupported language or gender is provided.
        """
        if language not in ['en', 'ru']:
            raise ValueError(f'Unsupported language: {language}')
        if gender not in ['male', 'female']:
            raise ValueError(f'Unsupported gender: {gender}')
        
        firstname = random.choice(self.data[language][f'{gender}_firstnames'])
        lastname = random.choice(self.data[language]['lastnames'])

        if language == 'ru' and gender == 'female':
            lastname += 'a'
        
        if self.format == 'dict':
            return {
                'firstname': firstname,
                'lastname': lastname
            }
        else:
            return self.format.format(firstname=firstname, lastname=lastname)


def check_class():
    """
    Tests the GeneratorNames class by generating and printing random names.
    """
    generator = GeneratorNames()
    random_russian_name = generator.generate_name(language='ru')
    print(f'Random Russian male name: {random_russian_name}')

    random_russian_female_name = generator.generate_name(language='ru', gender='female')
    print(f'Random Russian female name: {random_russian_female_name}')

    random_eng_name = generator.generate_name()
    print(f'Random English male name: {random_eng_name}')
    

if __name__ == '__main__':
    check_class()
