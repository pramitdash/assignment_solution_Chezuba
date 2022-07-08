try:
    from app import app
    import unittest

except Exception as e:
    print("Some library are missing: {}". format(e))

class FlaskTest(unittest.TestCase):

    #check for response 200
    def test_index1(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08-04")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #check the content return
    def test_index_content1(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08-04")
        print(response.content_type)
        self.assertEqual(response.content_type, "application/json")

    #check for data return
    def test_index_data1(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08-04")
        self.assertTrue(b'count' in response.data)

    #check for response 200
    def test_index2(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #check the content return
    def test_index_content2(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015")
        print(response.content_type)
        self.assertEqual(response.content_type, "application/json")

    #check for data return
    def test_index_data2(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015")
        self.assertTrue(b'count' in response.data)

    
    #check for response 200
    def test_index3(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #check the content return
    def test_index_content3(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08")
        print(response.content_type)
        self.assertEqual(response.content_type, "application/json")

    #check for data return
    def test_index_data3(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08")
        self.assertTrue(b'count' in response.data)

    
     #check for response 200
    def test_index5(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08-01 00:03")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #check the content return
    def test_index_content5(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08-01 00:03")
        print(response.content_type)
        self.assertEqual(response.content_type, "application/json")

    #check for data return
    def test_index_data5(self):
        tester = app.test_client(self)
        response = tester.get("/1/queries/count/2015-08-01 00:03")
        self.assertTrue(b'count' in response.data)
    

if __name__ == "__main__":
    unittest.main()