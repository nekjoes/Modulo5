from django.core.exceptions import ValidationError

def validarInter(value):
   if value < 0:
        raise ValidationError(
            '%(value)s no aceptado en Hrs o Jornales',
            params={'value': value}
        )


def validarJornal(value):
   if value > 8:
        raise ValidationError(
            '%(value)s Jornales de solo 8hrs',
            params={'value': value}
        )