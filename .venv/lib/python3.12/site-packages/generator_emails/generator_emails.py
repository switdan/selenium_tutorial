import random
import string

from generator_names import GeneratorNames


class GeneratorEmails:
    """
    A class for generating unique email addresses.

    Attributes:
        public_domains (list): A list of public email domains.
        anonymous_domains (list): A list of anonymous and temporary email domains.
        history (list): A list storing generated email addresses.
        save_history (bool): A flag indicating whether to save generated emails in history.
    """
    
    public_domains = [
        "gmail.com",
        "googlemail.com",
        "outlook.com",
        "hotmail.com",
        "live.com",
        "msn.com",
        "yahoo.com",
        "ymail.com",
        "rocketmail.com",
        "icloud.com",
        "me.com",
        "mac.com",
        "mail.com",
        "proton.me",
        "protonmail.com",
        "zoho.com",
        "zoho.eu",
        "gmx.com",
        "gmx.net",
        "gmx.de",
        "yandex.ru",
        "yandex.com",
        "yandex.ua",
        "yandex.kz",
        "yandex.by",
        "rambler.ru",
        "autorambler.ru",
        "lenta.ru",
        "myrambler.ru",
        "ro.ru",
        "r0.ru",
        "mail.ru",
        "bk.ru",
        "inbox.ru",
        "list.ru",
        "aol.com",
        "aim.com",
        "tutanota.com",
        "tuta.io",
        "tutanota.de",
        "fastmail.com",
        "hushmail.com"
    ]

    # Анонимные и временные почтовые домены
    anonymous_domains = [
        "guerrillamail.com",
        "sharklasers.com",
        "grr.la",
        "mailinator.com",
        "maildrop.cc",
        "temp-mail.org",
        "tempail.com",
        "moakt.com",
        "10minutemail.com",
        "dispostable.com",
        "yopmail.com",
        "anonaddy.com",
        "privaterelay.appleid.com",
        "simplelogin.io",
        "burnermail.io",
        "duck.com",
        "getnada.com",
        "mail.tm",
        "mytemp.email",
        "fakeinbox.com",
        "spambog.com",
        "trashmail.com",
        "throwawaymail.com",
        "mailnesia.com",
        "inboxalias.com"
    ]

    def __init__(self, save_history=True):
        """
        Initializes the GeneratorEmails instance.

        Args:
            save_history (bool, optional): Whether to save generated emails in history. Defaults to True.
        """
        self.history = []
        self.save_history = save_history
    
    def __repr__(self):
        """
        Returns a string representation of the GeneratorEmails instance.

        Returns:
            str: A formatted string describing the instance.
        """
        return f"GeneratorEmails: save_history={self.save_history}, history_size={len(self.history)}"
    
    def generate_email(self, range_len=(10, 18), domain='gmail.com', keywords=None):
        """
        Generates a unique email address.

        Args:
            range_len (tuple, optional): A tuple specifying the min and max length of the username. Defaults to (10, 18).
            domain (str or list, optional): The email domain or a list of domains to choose from. Defaults to 'gmail.com'.
            keywords (str or list, optional): A keyword or list of keywords to include in the username. Defaults to None.

        Raises:
            ValueError: If range_len does not contain exactly two values.

        Returns:
            str: A generated email address.
        """
        if len(range_len) != 2:
            raise ValueError(f'Not supported value for range_len: {range_len}')
        if range_len[0] < 7:
            range_len = (7, range_len[-1])
        if range_len[-1] < 7:
            range_len = (range_len[0], 7)
        
        if isinstance(domain, list):
            domain = random.choice(domain)
        if domain == 'random':
            domain = random.choice(self.public_domains)
        if domain == 'anonim':
            domain = random.choice(self.anonymous_domains)

        if keywords is None:
            keyword = GeneratorNames(format='{lastname}').generate_name()
        else:
            if isinstance(keywords, list):
                keyword = random.choice(keywords)
            else:
                keyword = keywords
        length = random.randint(*range_len)
        char_pool = string.ascii_lowercase + string.digits

        remaining_length = length - len(keyword)
        username_parts = list(keyword)
        for _ in range(remaining_length):
            insert_pos = random.randint(0, len(username_parts))
            username_parts.insert(insert_pos, random.choice(char_pool))
        
        username = ''.join(username_parts)
        email = f"{username}@{domain}"

        if email not in self.history:
            if self.save_history:
                self.history.append(email)
            return email
        else:
            return self.generate_email(range_len=range_len, domain=domain, keywords=keywords)


def check_class():
    """
    A function to test the GeneratorEmails class.

    Generates and prints three email addresses, then prints the history of generated emails.
    """
    generator = GeneratorEmails()
    for i in range(3):
        print(generator.generate_email(range_len=(9, 11), keywords='Vasya239'))
    print(generator.history)


if __name__ == '__main__':
    check_class()