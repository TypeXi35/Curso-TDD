import unittest
from unittest import mock
import io

#Commented from previous version
"""
import pathlib
import threading
import queue
"""

from todo.app import TODOApp
from todo.db import BasicDB

#Commented previous version of the code

"""
class TestRegressions(unittest.TestCase):
    def setUp(self):
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()
        
        self.fake_output = lambda txt: self.outputs.put(txt)
        self.fake_input = lambda: self.inputs.get()
        
        self.get_output = lambda: self.outputs.get(timeout=1)
        self.send_input = lambda cmd: self.inputs.put(cmd)
        
    def test_os_release(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            app_thread = threading.Thread(
                    target = TODOApp(
                        io = (self.fake_input, self.fake_output),
                        dbmanager = BasicDB(pathlib.Path(tmpdirname, "db"))
                    ).run,
                    daemon = True
                )
            
            app_thread.start()
            self.get_output()
            
            self.send_input("add buy milk")
            self.send_input('add "Focal Fossa"')
            self.send_input("quit")
            app_thread.join(timeout = 1)
            
            while True:
                try:
                    self.get_output()
                except queue.Empty:
                    break
            
            app_thread = threading.Thread(
                target=TODOApp(io = (self.fake_input, self.fake_output),
                dbmanager = BasicDB(pathlib.Path(tmpdirname, "db"))
                ).run,
                daemon = True
            )
            app_thread.start()
            self.get_output()
            
"""

# Second Version of the code, has the same error

"""

class TestRegressions(unittest.TestCase):
    def test_os_release(self):
        fakefile = io.StringIO()
        fakefile.close = mock.Mock()
        
        app = TODOApp(
            io = (mock.Mock(side_effect=[
                "add buy milk",
                'add install "Focal Fossa"',
                "quit"
            ]), mock.Mock()),
            dbmanager = BasicDB(None, _fileopener = mock.Mock(
                side_effect = [FileNotFoundError, fakefile]
            ))
        )
        app.run()
        
        # Rollback the file. So that the application, restarting,
        # can read the new data that we wrote.
        fakefile.seek(0)
        
        restarted_app = TODOApp(
            io=(mock.Mock(return_value="quit"), mock.Mock()),
            dbmanager=BasicDB(None, _fileopener = mock.Mock(
                return_value=fakefile
            ))
        )
        restarted_app.run()
        
"""

#Third version of the code

class TestRegression(unittest.TestCase):
    def test_os_release(self):
        fakefile = io.StringIO()
        fakefile.close = mock.Mock()
        data = ["buy milk", 'install "Focal Fossa"']
        
        dbmanager = BasicDB(None, _fileopener = mock.Mock(
            return_value = fakefile
        ))
        
        dbmanager.save(data)
        fakefile.seek(0)
        loaded_data = dbmanager.load()
        self.assertEqual(loaded_data, data)