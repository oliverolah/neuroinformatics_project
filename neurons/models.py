from django.db import models
from django.core.validators import MinValueValidator


class NeuronClass(models.Model):
   neuronClassId = models.AutoField(primary_key=True, verbose_name="Class Id")
   className = models.CharField(max_length=10, unique=True, verbose_name="Class Name")
   
   class Meta:
      verbose_name="Neuron Class"
      verbose_name_plural="Neuron Classes"

   def __str__(self):
      return self.className


class Neuron(models.Model):
   neuronId = models.AutoField(primary_key=True, verbose_name="Neuron Id")
   neuronName = models.CharField(max_length=10, unique=True, verbose_name="Neuron Name")
   className = models.ForeignKey("NeuronClass", to_field="className", on_delete=models.SET_NULL, null=True, blank=True, db_column="className", verbose_name="Class Name")
   neuronTypeName = models.ForeignKey("NeuronType", to_field="neuronTypeName", on_delete=models.SET_NULL, null=True, blank=True, db_column="neuronTypeName", verbose_name="Neuron Type Name")
   
   class Meta:
      verbose_name="Neuron"
      verbose_name_plural="Neurons"

   def __str__(self):
      return self.neuronName
   

class NeuronType(models.Model):
   neuronTypeId = models.AutoField(primary_key=True, verbose_name="Neuron Type Id")
   neuronTypeName = models.CharField(max_length=100, unique=True, verbose_name="Neuron Type Name")
   
   class Meta:
      verbose_name="Neuron Type"
      verbose_name_plural="Neuron Types"

   def __str__(self):
      return self.neuronTypeName


class Edge(models.Model):
   edgeId = models.AutoField(primary_key=True, verbose_name="Edge Id")
   edgeTypeName = models.CharField(max_length=10, unique=True, verbose_name="Edge Type Name")
   
   class Meta:
      verbose_name="Edge"
      verbose_name_plural="Edges"

   def __str__(self):
      return self.edgeTypeName


# Conn == connectome
   # neuronSender == n_transporter (send=transport)
   # neuronReceiver == n_receptor (receive=receptor)
class Connectome(models.Model):
   connectomeId = models.AutoField(primary_key=True, verbose_name="Connectome Id")
   neuronSender = models.ForeignKey("Neuron", to_field="neuronName", on_delete=models.CASCADE, default=None, related_name="n_transporter", db_column="neuronSender", verbose_name="Neuron Sender")
   neuronReceiver = models.ForeignKey("Neuron", to_field="neuronName", on_delete=models.CASCADE, default=None, related_name="n_receptor", db_column="neuronReceiver", verbose_name="Neuron Receiver")
   numOfEdges = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name="Number of Edges")
   edgeTypeName = models.ForeignKey("Edge", to_field="edgeTypeName", on_delete=models.SET_NULL, null=True, blank=True, db_column="edgeTypeName", verbose_name="Edge Type Name")
   
   class Meta:
      verbose_name="Connectome"
      verbose_name_plural="Connectomes"

   def __str__(self):
      return f"Connectome {self.connectomeId}"