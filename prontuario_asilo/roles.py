from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_funcionarios': True,
        'cadastrar_paciente': True,
    }

class Funcionario(AbstractUserRole):
    available_permissions = {
        'cadastrar_paciente': True,
    }
        