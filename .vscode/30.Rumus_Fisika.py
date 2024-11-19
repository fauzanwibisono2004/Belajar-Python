## Buatlah 3 rumus fisika dasar dan operasikan rumus tersebut berdasarkan input yang kalian tentukan sendiri
# 1. Hukum Newton 2 :
def Hukum_Newton_2(m,a) :
    ''' Hukum Newton 2 
    Argument :
        m,a : dua variabel untuk menyimpan data massa benda dan percepatan benda
    return :
        F : hasil perhitungan dari perkalian variabel m dan a
    '''
    print('======== Hukum Newton 2 ========')
    F = m*a
    return F

# 2. Hukum Ohm :
def Hukum_Ohm(I,R) :
    ''' Hukum Ohm 
    Argument :
        I,R : dua variabel untuk menyimpan data Arus (I) dan Hambatan (R)
    return :
        V : hasil perhitungan rumus Hukum Ohm dengan mengalikan Arus (I) dengan Hambatan (R)
    '''
    print('======== Hukum OHM ========')
    V = I*R
    return V

# 3. Energi Kinetik :
def Energi_Kinetik(m,v) :
    ''' Energi Kinetik 
    Argument :
        m,v : dua variabel untuk menyimpan data massa benda dan kecepatan benda
    return :
        Ek : hasil perhitungan rumus energi kinetik
    '''
    print('======== Energi Kinetik ========')
    Ek = (1/2)*m*(v**2)
    return Ek