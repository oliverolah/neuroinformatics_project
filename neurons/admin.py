from django.contrib import admin
from .models import NeuronClass, Neuron, Edge, Connectome, NeuronType


# Import 'neuron network' database tables/models
@admin.register(NeuronClass)
class NeuronClassAdmin(admin.ModelAdmin):
   list_display = ('neuronClassId', 'className')
   ordering = ('neuronClassId',)
   search_fields = ('neuronClassId', 'className')


@admin.register(Neuron)
class NeuronAdmin(admin.ModelAdmin):
   list_display = ('neuronId', 'neuronName', 'neuronTypeName', 'className')
   ordering = ('neuronId',)
   search_fields = ('neuronId', 'neuronName', 'neuronTypeName')
   

@admin.register(NeuronType)
class NeuronTypeAdmin(admin.ModelAdmin):
   list_display = ('neuronTypeId', 'neuronTypeName')
   ordering = ('neuronTypeId',)
   search_fields = ('neuronTypeId', 'neuronTypeName')


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
   list_display = ('edgeId', 'edgeTypeName')
   ordering = ('edgeId',)


@admin.register(Connectome)
class ConnectomeAdmin(admin.ModelAdmin):
   list_display = ('connectomeId', 'neuronSender', 'neuronReceiver','numOfEdges', 'edgeTypeName')
   ordering = ('connectomeId',)
   search_fields = ('connectomeId', 'neuronSender__exact', 'neuronReceiver__exact')
   