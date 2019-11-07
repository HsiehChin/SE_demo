import unittest
import ReplyMessage as reply

class testReply(unittest.TestCase):
    def test_init_helloWorld(self):
        self.assertEqual(reply.helloWorld(), "hello world!")

    def test_init_goodMorning(self):
        self.assertEqual(reply.goodMorning(), "how are you?")

    def test_init_howAreYou(self):
        self.assertEqual(reply.howAreYou(), "I am fine!")

if __name__ == '__main__':
    unittest.main()