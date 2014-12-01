from Products.validation.interfaces.IValidator import IValidator
from zLOG import LOG, INFO, ERROR, WARNING

validatorList = []

class isEmailUWOshValidator:
    __implements__ = IValidator

    def __init__(self,
                 name='isEmailUWOsh',
                 title='allow only @uwosh.edu email address',
                 description='',
                 errormsg=None):
        self.name = name
        self.title = title or name
        self.description = description
        self.errormsg=errormsg

    def __call__(self, value, *args, **kwargs):
        #LOG ("isEmailUWOshValidator", INFO, "Yay!  I was called with value = %s, args = %s, kwargs = %s" % (value, args, kwargs))
        instance = kwargs.get('instance', None)
        field    = kwargs.get('field', None)
        kw = {
            'instance':instance,
            'value':value,
            'args':args,
            'kwargs':kwargs,
            }
        if instance and field:
            if value.find('@uwosh.edu') <> -1:
                return True
            else:
                if self.errormsg:
                    return self.errormsg % kw
                else:
                    return "Email address must be in the @uwosh.edu domain"
        else:
            return 'Unable to determine which field is being modified.'
