from unit_test import squred

def main():
    test_squ()

def test_squ ():
    try:
        assert squred(2) == 4
    except AssertionError:
        print("even nubers dont work")
        exit       
    try:    
        assert squred(3) == 9
    except AssertionError:
        print("odd numbers dont work")    
        exit
    else:
        print("all is fine")    
    
      
if __name__ == "__main__":
    main()        