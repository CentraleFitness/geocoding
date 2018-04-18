
class Gym(object):
    """Instance of gym to be stored in the ES cluster"""

    def __init__(self, *args, **kwargs):
        self.id_gym = args[0]
        self.id_owner = args[1]
        self.address = {
            'street': args[2],
            'zip': args[3],
            'city': args[4],
            'country': args[5]
            }
        self.location = {
            'lat': args[6],
            'lon': args[7]
            }
        return super().__init__()

    def body_data(self) -> dict:
        return {
            'id_gym': self.id_gym,
            'id_owner': self.id_owner,
            'address': self.address,
            'location': self.location
            }
