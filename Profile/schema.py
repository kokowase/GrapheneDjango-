import graphene
from graphene_django import DjangoObjectType
from Profile.models import Category,Profile
from graphene_django.filter import DjangoFilterConnectionField


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id","username","first_name","last_name","category")

class Query(graphene.ObjectType):
    profile = graphene.List(ProfileType)


    def resolve_profile(self, info):
        return Profile.objects.all()
    
class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(root, info, name):
        category = Category(name=name)
        category.save()

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)