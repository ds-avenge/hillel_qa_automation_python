class CarsController:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def get_cars(self, sort_by=None, limit=None):
        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        return self.session.get(
            f"{self.base_url}/cars",
            params=params
        )
