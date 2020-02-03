import graphene
import template.schema


class Query(template.schema.Query, graphene.ObjectType):
    pass


class Mutation(template.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
