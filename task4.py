class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print(f'Я - {self.login}. Могу просматривать содержимое')

class Moderator(User):
    def __init__(self, login, password, group_id):
        super().__init__(login, password)
        self.group_id = group_id
    def view(self):
        print(f'Я - {self.login}. Могу просматривать содержимое')
    def redact(self):
        print(f'Я - {self.login}. Могу редактировать содержимое')

us = User('User', '1111')
mod = Moderator('Moderator', '2222', '6789787')
us.view() # Я - User. Могу просматривать содержимое
mod.view() # Я - Moderator. Могу просматривать содержимое
mod.redact() # Я - Moderator. Могу редактировать содержимое