from django.db import models


class NeuronClass(models.Model):
   neuronClassId = models.AutoField(primary_key=True)
   className = models.CharField(max_length=10)
   
   class Meta:
      verbose_name="Neuron Class"
      verbose_name_plural="Neuron Classes"


class Neuron(models.Model):
   neuronId = models.AutoField(primary_key=True)
   neuronName = models.CharField(max_length=10)
   neuronClassId = models.ForeignKey("NeuronClass", to_field="neuronClassId", on_delete=models.CASCADE)
   
   class Meta:
      verbose_name="Neuron"
      verbose_name_plural="Neurons"


class Edge(models.Model):
   neuronEdgeId = models.AutoField(primary_key=True)
   neuronEdgeType = models.CharField(max_length=10)
   
   class Meta:
      verbose_name="Edge"
      verbose_name_plural="Edges"


# Conn == connectome
   # neuronSender == n_transporter (send=transport)
   # neuronReceiver == n_receptor (receive=receptor)
class Connectome(models.Model):
   neuronConnId = models.AutoField(primary_key=True)
   neuronSender = models.ForeignKey("Neuron", to_field="neuronId", on_delete=models.SET_NULL, null=True, related_name="n_transporter")
   neuronReceiver = models.ForeignKey("Neuron", to_field="neuronId", on_delete=models.SET_NULL, null=True, related_name="n_receptor")
   neuronConnNum = models.IntegerField(default=1)
   neuronEdgeId = models.ForeignKey("Edge", to_field="neuronEdgeId", on_delete=models.SET_NULL, null=True)
   
   class Meta:
      verbose_name="Connectome"
      verbose_name_plural="Connectomes"