# test_app.py - unit tests run by Jenkins (bonus: tests in the build)
import io
import unittest
from contextlib import redirect_stdout

import app


class TestApp(unittest.TestCase):
    def test_main_prints_hello(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            app.main()
        self.assertEqual(buf.getvalue().strip(), "Hello, Jenkins!")


if __name__ == "__main__":
    unittest.main()
