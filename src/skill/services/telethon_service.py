import requests

from src.skill.models.general_models import Contact, Conversation
from src.skill.utils.constants import Constants


class TelethonService(object):
    """
    Communicates with my server.
    """
    contacts_url = 'https://www.lorenzhofmannw.com/telexa/api/contacts/'
    account_url = 'https://www.lorenzhofmannw.com/telexa/api/accounts/'

    def __init__(self):
        pass

    def get_conversations(self):
        conversations = []

        conversations.append(Conversation("Tom", ["Hey man how is it going? <break time='100ms'/>",
                                                  "I am chillin here <break time='100ms'/>",
                                                  "This is the last message <break time='350ms'/>"]))  # longer break here
        conversations.append(
            Conversation("Tennis and Golf",
                         [
                             "Rainer wrote: Rafa is awesome <break time='100ms'/> He is literally the greated player on sand that ever existed <break time='200ms'/>",
                             "Thomas wrote: Definitely true <break time='350ms'/>"], True))
        conversations.append(Conversation("Sophia", ["Yo dude <break time='350ms'/>"]))
        conversations.append(Conversation("Some Bot", ["Yo dude <break time='350ms'/>"]))

        return conversations

    def get_potential_contacts(self, fist_name):
        potential_contacts = []

        potential_contacts.append(Contact("Lorenz"))
        potential_contacts.append(Contact("Gianni"))
        potential_contacts.append(Contact("Rainer"))
        return potential_contacts

    def create_authorization_header(self):
        """
        Authorization header constructed as in docs:
        https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html#step-5-testing-restricted-access
        :return: Dictionary with the header.
        """
        auth_string = "Bearer " + Constants.ACCESS_TOKEN
        headers = {'Authorization': auth_string}

        return headers

    def execute_request(self, url):
        headers = self.create_authorization_header()

        r = requests.get(url, headers=headers)

        if r.ok:
            return r
        else:
            # some error
            print(r)
            return r.status_code
