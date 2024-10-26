from hello import hello

def test1():
    assert hello('Nick') == 'hello,Nick'
    
def arggument():
    assert hello() == 'hello,world'    