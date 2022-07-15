from functions.warmup import haversine,hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0
    assert type(hello_world())==str

def test_distance():
    assert round(haversine(48.865,2.380,48.235,2.393),2)==70.01
