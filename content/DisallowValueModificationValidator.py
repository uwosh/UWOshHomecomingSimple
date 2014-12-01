from Products.validation.interfaces.IValidator import IValidator
from zLOG import LOG, INFO, ERROR, WARNING

validatorList = []

class DisallowValueModificationValidator:
    __implements__ = IValidator

    def __init__(self,
                 name='disallowValueModification',
                 title='Disallow value modification validator',
                 description='Fails if the old value of the field is non-empty',
                 errormsg=None):
        self.name = name
        self.title = title or name
        self.description = description
        self.errormsg=errormsg

    def __call__(self, value, *args, **kwargs):
        #LOG ("DisallowValueModificationValidator", INFO, "Yay!  I was called with value = %s, args = %s, kwargs = %s" % (value, args, kwargs))
        instance = kwargs.get('instance', None)
        field    = kwargs.get('field', None)
        kw = {
            'instance':instance,
            'value':value,
            'args':args,
            'kwargs':kwargs,
            }
        if instance and field:
            currentValue = getattr(instance, field.getName())
            if currentValue == '' or value == currentValue:
                return True
            else:
                if self.errormsg:
                    return self.errormsg % kw
                else:
                    #return 'You cannot change the non-empty value of %s. kw = %s' % (field.getName(), kw)
                    return "You cannot change a non-empty value.  Please press the Cancel button below or use your browser's Back button to return to a previous screen."
        else:
            return 'Unable to determine which field is being modified.'
