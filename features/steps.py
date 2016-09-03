from lettuce import *
from selenium import webdriver


@before.each_scenario
def setup_some_scenario(scenario):
    world.driver = webdriver.Firefox()

@after.each_scenario
def setup_some_scenario(scenario):
    world.driver.close()

@step(u'Given I visit Google')
def given_i_visit_google(step):
    world.driver.get("http://www.google.com")

@step(u'Then I see title Google')
def then_i_see_title_google(step):
    assert "Google" in world.driver.title
