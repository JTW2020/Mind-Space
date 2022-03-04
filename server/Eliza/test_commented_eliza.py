import commented_eliza
import pytest

def test_ContextSwitchDepressed(): #tests if eliza successfully switched contexts from inbetween.txt to depressed.txt
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I am depressed."
    assert el.respond("I see. Please, tell me about how you've been feeling down.") == "I see. Please, tell me about how you've been feeling down."

def test_DepressedContext(): #tests if eliza successfully realizes that it is in the depressed context.
    el = commented_eliza.Eliza()
    el.load('depressed.txt')
    'I am depressed'
    assert el.respond("I already know that you are depressed.") == "I already know that you are depressed."

def test_ContextSwitchAnxious(): #tests if eliza successfully switched contexts from inbetween.txt to anxious.txt
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I am anxious."
    assert el.respond("I see. Tell me about how you've been feeling on edge, please.") == "I see. Tell me about how you've been feeling on edge, please."

def test_AnxiousContext(): # tests if eliza is sucessfully referencing the anxious context
    el = commented_eliza.Eliza()
    el.load('anxious.txt')
    'I am anxious'
    assert el.respond("I know that you are anxious. Is anything contributing to why you feel (2)?") == "I know that you are anxious. Is anything contributing to why you feel (2)?"

def test_ContextSwitchDisorder(): #tests if eliza successfully switched contexts from inbetween.txt to disorder.txt via string matching.
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I think I have a Disorder."
    assert el.respond("I see. Please, tell me about why you've been feeling this way.") == "I see. Please, tell me about why you've been feeling this way."

#def test_DisordeContext():     Cannot test disorder context because there is no unique response given when keyword is recieved from user input that triggers the context confirmation
 #   el = commented_eliza.Eliza()
  #  el.load('disorder.txt')
  #  assert el.respond()

def test_ContextSwitchAnger(): #tests if eliza successfully switched contexts from inbetween.txt to anger.txt via string matching.
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I am angry"
    assert el.respond("Understood. Please tell me about how you've been having your temper challenged.") == "Understood. Please tell me about how you've been having your temper challenged."

def test_AngerContext(): #confirms if eliza recognizes it is using the anger context via string matching.
    el = commented_eliza.Eliza()
    el.load('anger.txt')
    "I am angry"
    assert el.respond("we will not talk about your anger") == "we will not talk about your anger"

def test_ElizaExit(): #tests if eliza exits correctly via string matching.
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    'goodbye'
    assert el.respond("Goodbye.  Thank you for talking to me.") == "Goodbye.  Thank you for talking to me."
