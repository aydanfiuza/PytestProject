from appUserFunctions import *
from appPasswordFunctions import *
from appMessageFunctions import *

def test_appUsers():
    assert True == checkUpper('Aydan')
    assert False == checkUpper('aydan')

    assert True == checkSpace('Aydan')
    assert False == checkSpace('Ay dan')

    assert True == checkSpecial('Aydan')
    assert False == checkSpecial('Aydan!')

    assert True == checkLenght('Aydan')
    assert False == checkLenght('RichardAydanFiuzaOst22879764902817')

def test_appPassword():
    assert True == checkLenghtPsw('Soulindo02!')
    assert False == checkLenghtPsw('a1234')

    assert True == checkSpecialPsw('Soulindo02!')
    assert False == checkSpecialPsw('a1234')

    assert False == checkNumberPsw('Soulindo!')
    assert True == checkNumberPsw('a1234')

    assert True == checkUpperPsw('Soulindo02!')
    assert False == checkUpperPsw('a1234')

    assert False == checkLowerPsw('SOULINDO02!')
    assert True == checkLowerPsw('a1234')

def test_appMessage():
    assert True == checkLenghtMsg('Eu sou legal.')
    assert False == checkLenghtMsg('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce malesuada, sapien nec commodo congue, lectus augue viverra metus, vel euismod ipsum justo eu mi.')

    assert True == checkLenghtMsg('Eu gosto de pizza.')
    assert False == checkLenghtMsg('Nulla facilisi. Praesent volutpat augue sit amet diam varius, in ultricies justo tristique. Fusce pharetra nisi at est sagittis, nec elementum ipsum maximus.')

    assert True == checkLenghtMsg('A vida é curta e bela, aproveite cada momento.')
    assert False == checkLenghtMsg('O sucesso é a soma de pequenos esforços repetidos dia após dia. Não pare nunca de persistir e tentar.')

    assert True == checkLenghtMsg('A vida é agora, aproveite o momento.')
    assert False == checkLenghtMsg('Acredite em si mesmo e em seu potencial. Seja paciente, persistente e trabalhe duro. Grandes coisas levam tempo e esforço, mas a recompensa será incrível.')