from django.contrib import admin
from .models import NeuronClass, Neuron, Edge, Connectome


# Import 'neuron network' database tables/models
admin.site.register(NeuronClass)
admin.site.register(Neuron)
admin.site.register(Edge)
admin.site.register(Connectome)