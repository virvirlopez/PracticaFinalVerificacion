from lettuce import *
from Casino import Casino
from nose.tools import assert_true

@step(u'My name is ([^\s]+) and my money is ([^\s]+)')
def addUser(step, name, money):
    world.name = name
    world.money = money

@step(u'I create my user')
def createUser(step):
    casino = Casino()
    casino.ayadir_jugador(world.name, world.money)

@step(u'The user exist')
def exitsUser(step):
    casino = Casino()
    print world.name
    casino.obtener_creditos(world.name)

