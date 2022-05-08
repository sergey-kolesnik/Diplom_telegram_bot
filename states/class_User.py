class User:
    data_user_in_class = dict()
    """Класс User, каждому пользователю присваивается класс
    user_name - имя: str
    city_user - город: str
    hotels_count - количество отелей: int
    chat_id - id чата: int
    mode - режим который выбрал user: str
    photo - режим отправки фото:str
     total_data_hotel - найденная база отелей: list[dict]
     price_range - диапазон цен: list[str]
     distanse_range - диапазон расстояния: list[str]"""
    def __init__(self, user_id):
        self.user_name = None
        self.city_user = None
        self.hotels_count = None
        self.chat_id = None
        self.mode = None
        self.photo = None
        self.total_data_hotel = None
        self.price_range = None
        self.distance_range = None
        User.add_user(user_id, self)

    @staticmethod
    def get_user(user_id: int):
        # TODO каждому методу пишем докстринги
        if User.data_user_in_class.get(user_id) is None:
            new_user = User(user_id)
            return new_user
        return User.data_user_in_class.get(user_id)

    @classmethod
    def add_user(cls, user_id, user):
        cls.data_user_in_class[user_id] = user
