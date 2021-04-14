
class MultiDBRouter(object):
    def __init__(self):
        self.model_list = ['default', 'userdb']
        
    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.model_list:
            return model._meta.app_label

        return None
    
    def db_for_wirte(self,model,**hints):
        return None
    
    def allow_relation(self,obj1,obj2,**hints):
        return None
    
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        return None
