import commented_eliza
import pytest

def test_ContextSwitchDepressed(): #tests if eliza successfully switched contexts from inbetween.txt to depressed.txt
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I am depressed."
    assert el.respond("I see. Please, tell me about how you've been feeling down.") == "I see. Please, tell me about how you've been feeling down."

def test_DepressedContext(): #tests if eliza successfully realizes that it is in the correct context.
    el = commented_eliza.Eliza()
    el.load('depressed.txt')
    'I am depressed'
    assert el.respond("I already know that you are depressed.") == "I already know that you are depressed."

def test_ContextSwitchAnxious(): #tests if eliza successfully switched contexts from inbetween.txt to anxious.txt
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I am anxious."
    assert el.respond("I see. Tell me about how you've been feeling on edge, please.") == "I see. Tell me about how you've been feeling on edge, please."

def test_AnxiousContext():
    el = commented_eliza.Eliza()
    el.load('anxious.txt')
    'I am anxious'
    assert el.respond("I know that you are anxious. It is going to be okay.") == "I know that you are anxious. It is going to be okay."

def test_ContextSwitchDisorder():
    el = commented_eliza.Eliza()
    el.load('inbetween.txt')
    "I am hungry."
    assert el.respond("I see. Please, tell me about why you've been feeling this way.") == "I see. Please, tell me about why you've been feeling this way."

