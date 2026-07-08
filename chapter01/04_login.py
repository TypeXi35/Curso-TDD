import unittest

class Authentication:
    USERS = [{"username": "user1", "password": "pwd1"}]
    
    def login(self, username, password):
        """
        Checks if the user and password exists if it does returns the user
        """
        user = self.fetch_user(username);
        if not user and user["password"] != password:
            return None
        return user
            
    def fetch_user(self, username):
        """
        Checks if user exists
        """
        for user in self.USERS:
            if user["username"] == username:
                return user;
            else:
                return None
            
class Authorization:
    """
    Class that controls the Authorization of the user
    """
    PERMISSIONS = [{"user": "user1",
                    "permissions": {"create", "edit", "delete"}}]
    def can(self, user, action):
        """
        Method that returns a boolean value if a user is or is not able to perform a certain action
        """
        for u in self.PERMISSIONS:
            if u["user"] == user["username"]:
                return action in u["permissions"]
            else:
                return False
            
            
class TestAuthentication(unittest.TestCase):
    """
    Class that test the Authentication class
    """
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        resp = auth.login("testuser", "testpass")
        assert resp == {"username": "testuser", "password": "testpass"}
        
    
class TestAuthorization(unittest.TestCase):
    """
    Class that tests the Authorization class
    """
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [{
            "user": "testuser",
            "permissions": {"create"}
        }]
        resp = authz.can({"username": "testuser"}, "create")
        
        assert resp is True
        
class TestAuthorizeAuthenticateUser(unittest.TestCase):
    """
    Class that tests the complete Login and authorize flow
    """
    def test_auth(self):
        auth = Authentication()
        authz = Authorization()
        
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]
        
        u = auth.login("testuser", "test_pass")
        resp = authz.can(u,"create")
        assert resp is True
        
if __name__ == "__main__":
    unittest.main()