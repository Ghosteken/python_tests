from hello import hello

def test_hello():
    assert hello('Nick') == 'hello,Nick'
    
def test_other():
    assert hello() == 'hello,world'    
    