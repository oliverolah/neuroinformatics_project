from django.db import models
from django.core.validators import MinValueValidator


class NeuronClass(models.Model):
   neuronClassId = models.AutoField(primary_key=True)
   className = models.CharField(max_length=10, unique=True)
   
   class Meta:
      verbose_name="Neuron Class"
      verbose_name_plural="Neuron Classes"

   def __str__(self):
      return self.className


class Neuron(models.Model):
   neuronId = models.AutoField(primary_key=True)
   neuronName = models.CharField(max_length=10, unique=True)
   neuronClassId = models.ForeignKey("NeuronClass", to_field="neuronClassId", on_delete=models.SET_NULL, null=True, blank=True, db_column="neuronClassId")
   
   class Meta:
      verbose_name="Neuron"
      verbose_name_plural="Neurons"

   def __str__(self):
      return self.neuronName


class Edge(models.Model):
   neuronEdgeId = models.AutoField(primary_key=True)
   neuronEdgeType = models.CharField(max_length=10, unique=True)
   
   class Meta:
      verbose_name="Edge"
      verbose_name_plural="Edges"

   def __str__(self):
      return self.neuronEdgeType


# Conn == connectome
   # neuronSender == n_transporter (send=transport)
   # neuronReceiver == n_receptor (receive=receptor)
class Connectome(models.Model):
   neuronConnId = models.AutoField(primary_key=True)
   neuronSender = models.ForeignKey("Neuron", to_field="neuronId", on_delete=models.CASCADE, related_name="n_transporter", db_column="neuronSender")
   neuronReceiver = models.ForeignKey("Neuron", to_field="neuronId", on_delete=models.CASCADE, related_name="n_receptor", db_column="neuronReceiver")
   neuronConnNum = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
   neuronEdgeId = models.ForeignKey("Edge", to_field="neuronEdgeId", on_delete=models.SET_NULL, null=True, blank=True, db_column="neuronEdgeId")
   
   class Meta:
      verbose_name="Connectome"
      verbose_name_plural="Connectomes"

   def __str__(self):
      return f"Connectome {self.neuronConnId}"