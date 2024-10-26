from hello import hello

def test_hello():
    assert hello('Nick') == 'hello,Nick'
    
def test_other():
    for name in ['bull','will','clark']:
        assert hello(name) == 'hello,world'    
    