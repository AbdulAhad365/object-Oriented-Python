class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email
    
    @classmethod
    def create_user(self,name,email):
        if not self.validate_email(email):
            # give an error
            raise ValueError("Invalid email")
        return User(name,email)
u1=User("ahad","quickmailahad@gmail.com")
u2=u1.create_user("ahad","gey@gmail.com")
print(u2.name,u2.email)