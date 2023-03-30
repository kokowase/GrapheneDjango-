from django.test import TestCase
import pytest
from pytest import raises
from graphene_django import DjangoObjectType
import json
import graphene
from .schema import Query,schema
from .models import Profile, Category
from django.test import Client
from graphene_django.utils.testing import GraphQLTestCase, graphql_query
# Create your tests here.

class mytest(GraphQLTestCase):
  
    def setUp(self):
        self.schema = graphene.Schema()
        category = Category.objects.create(name='Manager')
        Profile.objects.create(username='kokowase',first_name='kokowaseso',last_name='yekti',category=category)
    def test_some_query(self):
        response = self.query(
            """
            query{
             profile { 
                id
                username
                firstName
                lastName
                category{
                    id
                }
            }
            }
            """
        )
        
        content =json.loads(response.content)
        
        self.assertResponseNoErrors(response)
        self.assertEqual(content['data']['profile'][0]['username'], 'kokowase')

