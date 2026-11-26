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

def test_hit_makes_barrier_shorter():
    d = Barrier(40, 60)
    d.hit()
    assert d.rect.height == 30

def test_other_barrier_untouched():
    e = Barrier(25, 80)
    f = Barrier(55, 30)
    f.hit()
    assert e.health == 4
    assert e.rect.height == 40


