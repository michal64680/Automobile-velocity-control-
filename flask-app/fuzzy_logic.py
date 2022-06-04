from simpful import *



# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
S_1 = FuzzySet(function=Triangular_MF(a=-2000, b=-2000, c=-40), term="v_v_minus")
S_2 = FuzzySet(function=Triangular_MF(a=-50, b=-15, c=-5), term="v_minus")
S_3 = FuzzySet(function=Triangular_MF(a=-10, b=-3, c=-0.4), term="minus")
S_4 = FuzzySet(function=Triangular_MF(a=-0.8, b=0, c=0.8), term="zero")
S_5 = FuzzySet(function=Triangular_MF(a=0.4, b=3, c=10), term="plus")
S_6 = FuzzySet(function=Triangular_MF(a=5, b=15, c=50), term="v_plus")
S_7 = FuzzySet(function=Triangular_MF(a=40, b=2000, c=2000), term="v_v_plus")
FS.add_linguistic_variable("Error", LinguisticVariable([S_1, S_2, S_3, S_4, S_5, S_6, S_7], concept="Error value", universe_of_discourse=[-2000,2000]))

S_1 = FuzzySet(function=Triangular_MF(a=-30000, b=-30000, c=-4000), term="v_v_small")
S_2 = FuzzySet(function=Triangular_MF(a=-5000, b=-2000, c=-450), term="v_small")
S_3 = FuzzySet(function=Triangular_MF(a=-800, b=-450, c=-50), term="small")
S_4 = FuzzySet(function=Triangular_MF(a=-100, b=0, c=100), term="zero")
S_5 = FuzzySet(function=Triangular_MF(a=50, b=2000, c=6000), term="big")
S_6 = FuzzySet(function=Triangular_MF(a=4000, b=9000, c=17500), term="v_big")
S_7 = FuzzySet(function=Triangular_MF(a=14000, b=100000, c=100000), term="v_v_big")
FS.add_linguistic_variable("Drag", LinguisticVariable([S_1, S_2, S_3, S_4, S_5, S_6, S_7], concept="Drag value", universe_of_discourse=[-30000,100000]))

# Define output fuzzy sets and linguistic variable
T_1 = FuzzySet(function=Triangular_MF(a=-50, b=-50, c=-37), term="minus50")
T_2 = FuzzySet(function=Triangular_MF(a=-42, b=-35, c=-27), term="minus40")
T_3 = FuzzySet(function=Triangular_MF(a=-32, b=-25, c=-17), term="minus30")
T_4 = FuzzySet(function=Triangular_MF(a=-22, b=-15, c=-7), term="minus20")
T_5 = FuzzySet(function=Triangular_MF(a=-12, b=-5, c=3), term="minus10")
T_6 = FuzzySet(function=Triangular_MF(a=-2, b=5, c=13), term="zero")
T_7 = FuzzySet(function=Triangular_MF(a=8, b=15, c=23), term="plus10")
T_8 = FuzzySet(function=Triangular_MF(a=18, b=25, c=33), term="plus20")
T_9 = FuzzySet(function=Triangular_MF(a=28, b=35, c=43), term="plus30")
T_10 = FuzzySet(function=Triangular_MF(a=38, b=45, c=53), term="plus40")
T_11 = FuzzySet(function=Triangular_MF(a=48, b=55, c=63), term="plus50")
T_12 = FuzzySet(function=Triangular_MF(a=58, b=65, c=73), term="plus60")
T_13 = FuzzySet(function=Triangular_MF(a=68, b=75, c=83), term="plus70")
T_14 = FuzzySet(function=Triangular_MF(a=78, b=85, c=93), term="plus80")
T_15 = FuzzySet(function=Triangular_MF(a=88, b=100, c=100), term="plus90")
FS.add_linguistic_variable("Pedal", LinguisticVariable([T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9, T_10, T_11, T_12, T_13, T_14, T_15], universe_of_discourse=[-50,100]))

# Define fuzzy rules
R1 = """IF ((Error IS v_v_minus) AND (Drag IS v_v_small)) 
        OR ((Error IS v_v_minus) AND (Drag IS v_small))
        THEN (Pedal IS minus50)"""
R2 = """IF ((Error IS v_v_minus) AND (Drag IS small)) 
        OR ((Error IS v_v_minus) AND (Drag IS zero))
        OR ((Error IS v_minus) AND (Drag IS v_v_small))
        OR ((Error IS v_minus) AND (Drag IS v_small))
        THEN (Pedal IS minus40)"""
R3 = """IF ((Error IS v_v_minus) AND (Drag IS big)) 
        OR ((Error IS v_v_minus) AND (Drag IS v_big))
        OR ((Error IS v_minus) AND (Drag IS small))
        OR ((Error IS v_minus) AND (Drag IS zero))
        OR ((Error IS minus) AND (Drag IS v_v_small))
        THEN (Pedal IS minus30)"""
R4 = """IF ((Error IS v_v_minus) AND (Drag IS v_v_big)) 
        OR ((Error IS v_minus) AND (Drag IS big))
        OR ((Error IS v_minus) AND (Drag IS v_big))
        OR ((Error IS v_minus) AND (Drag IS v_v_big))
        OR ((Error IS minus) AND (Drag IS v_small))
        OR ((Error IS minus) AND (Drag IS small))
        OR ((Error IS minus) AND (Drag IS zero))
        THEN (Pedal IS minus20)"""
R5 = """IF ((Error IS minus) AND (Drag IS big)) 
        OR ((Error IS minus) AND (Drag IS v_big))
        OR ((Error IS minus) AND (Drag IS v_v_big ))
        THEN (Pedal IS minus10)"""
R6 = """IF ((Error IS zero) AND (Drag IS v_v_small)) 
        OR ((Error IS zero) AND (Drag IS v_small))
        OR ((Error IS zero) AND (Drag IS small))
        THEN (Pedal IS zero)"""
R7 = """IF ((Error IS zero) AND (Drag IS zero)) 
        OR ((Error IS zero) AND (Drag IS big))
        OR ((Error IS zero) AND (Drag IS v_big))
        OR ((Error IS plus) AND (Drag IS v_v_small))
        THEN (Pedal IS plus10)"""
R8 = """IF ((Error IS zero) AND (Drag IS v_v_big)) 
        OR ((Error IS plus) AND (Drag IS v_small))
        OR ((Error IS plus) AND (Drag IS small))
        THEN (Pedal IS plus20)"""
R9 = "IF (Error IS plus) AND (Drag IS zero) THEN (Pedal IS plus30)"
R10 = """IF ((Error IS plus) AND (Drag IS big)) 
         OR ((Error IS plus) AND (Drag IS v_big))
         THEN (Pedal IS plus40)"""
R11 = """IF ((Error IS plus) AND (Drag IS v_v_big)) 
         OR ((Error IS v_plus) AND (Drag IS v_v_small))
         OR ((Error IS v_plus) AND (Drag IS v_small))
         THEN (Pedal IS plus50)"""
R12 = """IF ((Error IS plus) AND (Drag IS v_v_big)) 
         OR ((Error IS v_plus) AND (Drag IS zero))
         THEN (Pedal IS plus60)"""
R13 = """IF ((Error IS v_plus) AND (Drag IS big))
         OR ((Error IS v_plus) AND (Drag IS v_big))
         OR ((Error IS v_v_plus) AND (Drag IS v_v_small))
         THEN (Pedal IS plus70)"""
R14 = """IF ((Error IS v_v_plus) AND (Drag IS v_small))
         OR ((Error IS v_v_plus) AND (Drag IS small))
         OR ((Error IS v_v_plus) AND (Drag IS zero))
         THEN (Pedal IS plus80)"""
R15 = """IF ((Error IS v_plus) AND (Drag IS v_v_big))
         OR ((Error IS v_v_plus) AND (Drag IS big))
         OR ((Error IS v_v_plus) AND (Drag IS v_big))
         OR ((Error IS v_v_plus) AND (Drag IS v_v_big))
         THEN (Pedal IS plus90)"""
FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15])
#FS.set_variable("Error", 55)
# Set antecedents values
def set_get_fuzzy_variables(error, drag):
    #print(error)
    #print(drag)
    FS.set_variable("Error", error)
    FS.set_variable("Drag", drag)
    u_dict = FS.Mamdani_inference(terms=["Pedal"])
    #print(u_dict['Pedal'])
    return u_dict['Pedal']

# Perform Mamdani inference and print output