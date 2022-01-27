class DefaultAdminAuthRouter:
   
   route_app_labels = {'auth', 'contenttypes', 'admin', 'session', }

   def db_for_read(self, model, **hints):
      if model._meta.app_label in self.route_app_labels:
         return 'default'
      return None

   def db_for_write(self, model, **hints):
      if model._meta.app_label in self.route_app_labels:
         return 'default'
      return None

   def allow_relation(self, obj1, obj2, **hints):
      if (
         obj1._meta.app_label in self.route_app_labels or
         obj2._meta.app_label in self.route_app_labels
      ):
         return True
      return None

   def allow_migrate(self, db, app_label, model_name=None, **hints):
      if app_label in self.route_app_labels:
         return db == 'default'
      return None


class NeuronsRouter:
   route_app_labels = {'neurons'}

   def db_for_read(self, model, **hints):
      if model._meta.app_label in self.route_app_labels:
         return 'neurons_db'
      return None

   def db_for_write(self, model, **hints):
      if model._meta.app_label in self.route_app_labels:
         return 'neurons_db'
      return None
   
   def allow_relation(self, obj1, obj2, **hints):
      if (
         obj1._meta.app_label in self.route_app_labels or
         obj2._meta.app_label in self.route_app_labels
      ):
         return True
      return None

   def allow_migrate(self, db, app_label, model_name=None, **hints):
      if app_label in self.route_app_labels:
         return db == 'neurons_db'
      return None


class SubmitDataRouter:
   route_app_labels = {'submitdata'}

   def db_for_read(self, model, **hints):
      if model._meta.app_label in self.route_app_labels:
         return 'submitdata_db'
      return None

   def db_for_write(self, model, **hints):
      if model._meta.app_label in self.route_app_labels:
         return 'submitdata_db'
      return None

   def allow_migrate(self, db, app_label, model_name=None, **hints):
      if app_label in self.route_app_labels:
         return db == 'submitdata_db'
      return None