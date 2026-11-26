from barrier import Barrier 

def test_one_hit ():
    b = Barrier (40,65)
    b.hit ()
    assert b.health == 3

def test_last_hit ():
    a = Barrier (50,70)
    a.hit  ()
    a.hit  ()
    a.hit  ()
    a.hit  ()
    assert a.alive == False

def test_hit_after_destroyed():
    c = Barrier (80,120)
    c.hit ()
    c.hit ()
    c.hit ()
    c.hit ()
    c.hit ()
    assert c.health == 0
    assert c.rect.height == 0

