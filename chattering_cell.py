import izhikevich_cells as izh

class chCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        
        #Define any parameters that need to be changed
        self.celltype='Chattering' # Regular spiking
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=50     
        
myCell = chCell(4000)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)
        