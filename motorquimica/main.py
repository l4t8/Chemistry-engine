#This code was made by l4t8

class atom:

    def __init__(self,name,proton,neutron,electron,oxi,num):
        
        self.name = name
        self.proton = proton
        self.neutron = neutron
        self.electron = electron
        self.oxi = oxi
        self.num = num

    def setoxi(self,oxi):        
        self.oxi = input("New oxidation number")

    def setnum(self,num):
        self.num = input("New number of atoms")

    def __add__(self,other):
        if type(self).__name__ and type(other).__name__ == nonmetal:
            print("Work in progress")
        else:
            







#atom nonmetal class, including negoxi as negative oxidation number
class nonmetal(atom):
    
    def __init__(self,name,proton,neutron,electron,oxi,negoxi,num):
        super().__init__(name,proton,neutron,electron,oxi,num)
        self.negoxi = negoxi

    def setnegoxi(self,negoxi):        
        self.negoxi = input("New negative oxidation number")

    def setfirstatom(self,name,electron,oxi,negoxi):
        self.name = name






class noblegas(atom):
    
    def __init__(self,name,proton,neutron,electron,oxi,num):
        super().__init__(name,proton,neutron,electron,oxi,num)
        #Thought this ones couldnt mix, well they can




class metal(atom):
    def __init__(self,name,proton,neutron,electron,num):
        super().__init__(name,proton,neutron,electron,num)
        #some serious big stuff ought to be done here


class metalloid(metal):
    def __init__(self,name,proton,neutron,electron,num):
        super().__init__(name,proton,neutron,electron,num)
        #Dont know what is a metalloid lol

#hydrogen is going to be nonmetal for simplification purposes

def main():
    result = Hydrogen + Lithium
    return result




Hydrogen = metal("H",1,1,1,(1),(-1),0)
Helium = noblegas("He", 2, 2, 2,(2),0)
Lithium = metal("Li",3,3,3,(),(),0)
Beryllium = metal("Be",4,4,4,(),(),0)
Boron = nonmetal("B",5,5,5,(),(),0)
Carbon = nonmetal("C",6,6,6,(),(),0)
Nitrogen = nonmetal("N",7,7,7,(),(),0)
Oxygen = nonmetal("O",8,8,8,(),(),0)
Fluorine = nonmetal("F",9,9,9,(),(),0)
Neon = nonmetal("Ne",10,10,10,(),(),0)
Sodium = nonmetal("Na",11,11,11,(),(),0)
Magnesium = nonmetal("Mg",12,12,12,(),(),0)
Aluminum = nonmetal("Al",13,13,13,(),(),0)
Silicon = nonmetal("Si",14,14,14,(),(),0)
Phosphorus = nonmetal("P",15,15,15,(),(),0)
Sulfur = nonmetal("S",16,16,16,(),(),0)
Chlorine = nonmetal("Cl",17,17,17,(),(),0)
Argon = nonmetal("Ar",18,18,18,(),(),0)
Potassium = nonmetal("K",19,19,19,(),(),0)
Calcium = nonmetal("Ca",20,20,20,(),(),0)
Scandium = nonmetal("Sc",21,21,21,(),(),0)
Titanium = nonmetal("Ti",22,22,22,(),(),0)
Vanadium = nonmetal("V",23,23,23,(),(),0)
Chromium = nonmetal("Cr",24,24,24,(),(),0)
Manganese = nonmetal("Mn",25,25,25,(),(),0)
Iron = nonmetal("Fe",26,26,26,(),(),0)
Cobalt = nonmetal("Co",27,27,27,(),(),0)
Nickel = nonmetal("Ni",28,28,28,(),(),0)
Copper = nonmetal("Cu",29,29,29,(),(),0)
Zinc = nonmetal("Zn",30,30,30,(),(),0)
Gallium = nonmetal("Ga",31,31,31,(),(),0)
Germanium = nonmetal("Ge",32,32,32,(),(),0)
Arsenic = nonmetal("As",33,33,33,(),(),0)
Selenium = nonmetal("Se",34,34,34,(),(),0)
Bromine = nonmetal("Br",35,35,35,(),(),0)
Krypton = nonmetal("Kr",36,36,36,(),(),0)
Rubidium = nonmetal("Rb",37,37,37,(),(),0)
Strontium = nonmetal("Sr",38,38,38,(),(),0)
Yttrium = nonmetal("Y",39,39,39,(),(),0)
Zirconium = nonmetal("Zr",40,40,40,(),(),0)
Niobium = nonmetal("Nb",41,41,41,(),(),0)
Molybdenum = nonmetal("Mo",42,42,42,(),(),0)
Technetium = nonmetal("Tc",43,43,43,(),(),0)
Ruthenium = nonmetal("Ru",44,44,44,(),(),0)
Rhodium = nonmetal("Rh",45,45,45,(),(),0)
Palladium = nonmetal("Pd",46,46,46,(),(),0)
Silver = nonmetal("Ag",47,47,47,(),(),0)
Cadmium = nonmetal("Cd",48,48,48,(),(),0)
Indium = nonmetal("In",49,49,49,(),(),0)
Tin = nonmetal("Sn",50,50,50,(),(),0)
Antimony = nonmetal("Sb",51,51,51,(),(),0)
Tellurium = nonmetal("Te",52,52,52,(),(),0)
Iodine = nonmetal("I",53,53,53,(),(),0)
Xenon = nonmetal("Xe",54,54,54,(),(),0)
Cesium = nonmetal("Cs",55,55,55,(),(),0)
Barium = nonmetal("Ba",56,56,56,(),(),0)
Lanthanum = nonmetal("La",57,57,57,(),(),0)
Cerium = nonmetal("Ce",58,58,58,(),(),0)
Praseodymium = nonmetal("Pr",59,59,59,(),(),0)
Neodymium = nonmetal("Nd",60,60,60,(),(),0)
Promethium = nonmetal("Pm",61,61,61,(),(),0)
Samarium = nonmetal("Sm",62,62,62,(),(),0)
Europium = nonmetal("Eu",63,63,63,(),(),0)
Gadolinium = nonmetal("Gd",64,64,64,(),(),0)
Terbium = nonmetal("Tb",65,65,65,(),(),0)
Dysprosium = nonmetal("Dy",66,66,66,(),(),0)
Holmium = nonmetal("Ho",67,67,67,(),(),0)
Erbium = nonmetal("Er",68,68,68,(),(),0)
Thulium = nonmetal("Tm",69,69,69,(),(),0)
Ytterbium = nonmetal("Yb",70,70,70,(),(),0)
Lutetium = nonmetal("Lu",71,71,71,(),(),0)
Hafnium = nonmetal("Hf",72,72,72,(),(),0)
Tantalum = nonmetal("Ta",73,73,73,(),(),0)
Wolfram = nonmetal("W",74,74,74,(),(),0)
Rhenium = nonmetal("Re",75,75,75,(),(),0)
Osmium = nonmetal("Os",76,76,76,(),(),0)
Iridium = nonmetal("Ir",77,77,77,(),(),0)
Platinum = nonmetal("Pt",78,78,78,(),(),0)
Gold = nonmetal("Au",79,79,79,(),(),0)
Mercury = nonmetal("Hg",80,80,80,(),(),0)
Thallium = nonmetal("Tl",81,81,81,(),(),0)
Lead = nonmetal("Pb",82,82,82,(),(),0)
Bismuth = nonmetal("Bi",83,83,83,(),(),0)
Polonium = nonmetal("Po",84,84,84,(),(),0)
Astatine = nonmetal("At",85,85,85,(),(),0)
Radon = nonmetal("Rn",86,86,86,(),(),0)
Francium = nonmetal("Fr",87,87,87,(),(),0)
Radium = nonmetal("Ra",88,88,88,(),(),0)
Actinium = nonmetal("Ac",89,89,89,(),(),0)
Thorium = nonmetal("Th",90,90,90,(),(),0)
Protactinium = nonmetal("Pa",91,91,91,(),(),0)
Uranium = nonmetal("U",92,92,92,(),(),0)
Neptunium = nonmetal("Np",93,93,93,(),(),0)
Plutonium = nonmetal("Pu",94,94,94,(),(),0)
Americium = nonmetal("Am",95,95,95,(),(),0)
Curium = nonmetal("Cm",96,96,96,(),(),0)
Berkelium = nonmetal("Bk",97,97,97,(),(),0)
Californium = nonmetal("Cf",98,98,98,(),(),0)
Einsteinium = nonmetal("Es",99,99,99,(),(),0)
Fermium = nonmetal("Fm",100,100,100,(),(),0)
Mendelevium = nonmetal("Md",101,101,101,(),(),0)
Nobelium = nonmetal("No",102,102,102,(),(),0)
Lawrencium = nonmetal("Lr",103,103,103,(),(),0)
Rutherfordium = nonmetal("Rf",104,104,104,(),(),0)
Dubnium = nonmetal("Db",105,105,105,(),(),0)
Seaborgium = nonmetal("Sg",106,106,106,(),(),0)
Bohrium = nonmetal("Bh",107,107,107,(),(),0)
Hassium = nonmetal("Hs",108,108,108,(),(),0)
Meitnerium = nonmetal("Mt",109,109,109,(),(),0)
Darmstadtium = nonmetal("Ds",110,110,110,(),(),0)
Roentgenium = nonmetal("Rg",111,111,111,(),(),0)
Copernicium = nonmetal("Cn",112,112,112,(),(),0)
Nihonium = nonmetal("Nh",113,113,113,(),(),0)
Flerovium = nonmetal("Fl",114,114,114,(),(),0)
Moscovium = nonmetal("Mc",115,115,115,(),(),0)
Livermorium = nonmetal("Lv",116,116,116,(),(),0)
Tennessine = nonmetal("Ts",117,117,117,(),(),0)

print(main())