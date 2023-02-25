class Control:
    _tv='';
    def enlazar(self,televisor):
        self._tv=televisor
        self._tv._control=self
        
    def getTV(self):
        return self._tv;
    def setTV(self,tv):
        self._tv=tv
    