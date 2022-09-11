import pytest

class kunde:
    
    def __init__(self, name, vorname, nr):
        self.name = name
        self.vorname = vorname
        self.nr = nr
        
    def normalisiere(self):
        self.vorname = " ".join(self.vorname.split())
        self.name = self.name.strip()
        
    def kapitalisiere(self):
        self.name = self.name.capitalize()
        self.vorname = " ".join([vorname.capitalize() for vorname in self.vorname.split()])

        
class Test_kunde:
    
    # Arrange 1
    @pytest.fixture
    def kunde1(self):
        """
        Ein Testkunde, der einfach zu viele Whitespaces
        im Nach- und Vornamen hat.
        """
        k = kunde("  brauer ", " julius henry ", 938)
        return k
    
    # Arrange 2
    @pytest.fixture
    def kunde2(self):
        """
        Ein Testkunde, der zusammengesetzte Namen
        und Whitespaces hat.
        """
        k = kunde("  brauer-lüdenmayer ", " julius-henry ", 938)
        return k
        
    def test_kunde_anlegen(self, kunde1):
        # Act1
        
        # Assert1
        assert kunde1.name == "  brauer "
        assert kunde1.vorname == " julius henry "
        assert kunde1.nr == 938

    
    def test_kundenname_normalisieren(self, kunde1):        
        # Act2
        kunde1.normalisiere()
        
        # Assert2
        assert kunde1.name == "brauer"
        assert kunde1.vorname == "julius henry"
        assert kunde1.nr == 938
    
    def test_kundenname_normalisieren_und_kapitalisieren1(self, kunde1):                
        # Act3
        kunde1.normalisiere()
        kunde1.kapitalisiere()
        
        # Assert3
        assert kunde1.name == "Brauer"
        assert kunde1.vorname == "Julius Henry"
        assert kunde1.nr == 938   
        
    def test_kundenname_normalisieren_und_kapitalisieren2(self, kunde2):                
        # Act4
        kunde2.normalisiere()
        kunde2.kapitalisiere()
        
        # Assert4
        assert kunde2.name == "Brauer-lüdenmayer"
        assert kunde2.vorname == "Julius-henry"
        assert kunde2.nr == 938
        