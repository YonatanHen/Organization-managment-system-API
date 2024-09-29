import unittest

from services.organization_service import *
from services.endpoint_service import *
from services.user_service import *
from models import Base
from DB.psql_connection import engine

class TestApplication(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        This method creates a new DB session.
        """
        Base.metadata.create_all(bind=engine)
    
    @classmethod
    def tearDownClass(cls):
        """
        This method drops the whole data we have inserted into the DB for testing purposes.
        """
        Base.metadata.drop_all(bind=engine)
        
        
    def test_1_create_organization(self):
        """
        This function tests the creation of a organization object.
        """
        organization1=create_organization("A")
        self.assertEqual(organization1['name'], "A")
        
        organization2=create_organization("B")
        self.assertNotEqual(organization1['id'], organization2['id'])
                
        with self.assertRaises(ValueError) as err:
                create_organization("A")
        self.assertIn(str(err.exception), "Organization 'A' already exists.")
    
    
    def test_2_update_organization(self):
        """
        This function tests the updating of a organization object.
        """
        organization = create_organization("Old-Name")
        updated_organization = update_organization(organization['id'], "C")
        self.assertEqual(updated_organization['name'], "C")
        
        organization2 = create_organization("D")

        with self.assertRaises(ValueError) as err:
            update_organization(organization2['id'], "C")
        self.assertIn(str(err.exception), "Organization 'C' already exists.")
    
    
    def test_3_delete_organization(self):
        """
        This function tests the deletion of a organization object.
        """
        #Delete the first organization created in 'test_create_organization'
        organization = create_organization("Org to delete")
        deleted_organization = delete_organization(organization['id'])
        self.assertEqual(deleted_organization['name'],'Org to delete')
        
        with self.assertRaises(ValueError) as err:
            delete_organization(999)
        self.assertIn(str(err.exception), "No organization with id #999 was found")
    
    def test_4_create_and_get_endpoint(self):
        """
        This function tests the creation of an endpoint object.
        """
        create_organization("E")

        endpoint1 = create_endpoint("/1", '6', None)
        self.assertEqual(endpoint1['id'],1)
        self.assertEqual(endpoint1['name'],'/1')
        self.assertEqual(endpoint1['organization_id'],6)
        
        endpoint2 = create_endpoint("/2", None, "E")
        self.assertEqual(endpoint2['id'],2)
        self.assertEqual(endpoint2['name'],'/2')
        self.assertNotEqual(endpoint2['organization_id'],2)
        
        self.assertEqual(len(get_endpoints_list_from_organization(6)), 2)

        
    def test_5_create_and_get_user(self):
        """
        This function tests the creation of a user object.
        """
        create_organization("F")
        create_endpoint("/3", 6, None)
        user=create_user("A", 3)
        
        self.assertEqual(user['id'],1)
        self.assertEqual(user['name'],'A')
        self.assertEqual(user['organization_id'],6)
        self.assertEqual(get_endpoint_by_user_id(1)['id'],3)
        self.assertNotEqual(get_organization_by_user_id(1)['id'],1)
        self.assertEqual(get_user_from_endpoint(1,3)['name'],"A")
        self.assertEqual(get_user_from_organization(1,6)['name'],'A')
        
        with self.assertRaises(ValueError) as err:
            self.assertEqual(get_user_from_endpoint(1,6)['name'],"A")
        self.assertIn(str(err.exception), "No user with id #1 in endpoint #6 was found or not exists.")
        
        
if __name__ == '__main__':
    unittest.main()