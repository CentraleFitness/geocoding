
class Gym(object):
    """Instance of gym to be stored in the ES cluster"""

    def __init__(self, *args, **kwargs):
        self.id_gym = args[0]
        self.id_owner = args[1]
        self.name = args[2]
        self.address = {
            'street': args[3],
            'zip': args[4],
            'city': args[5],
            'country': args[6]
            }
        self.location = {
            'lat': args[7],
            'lon': args[8]
            }
        return super().__init__()

    def body_data(self) -> dict:
        return {
            'id_gym': self.id_gym,
            'id_owner': self.id_owner,
            'name': self.name,
            'address': self.address,
            'location': self.location
            }
