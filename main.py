print("Mpikajy")

print("Misafidy ny asa tianao atao:")
print("1. Fanampiana")
print("2. Fanalana")
print("3. Fampitomboana")

choix = int(input("Mifanafatra ny asa tianao (1, 2 na 3): "))

isa_1 = int(input("Ampidiro ny isa voalohany: "))   
isa_2 = int(input("Ampidiro ny isa faharoa: "))

if choix == 1:
    print("Ny vokatry ny fanampiana dia:", isa_1 + isa_2)
elif choix == 2:
    print("Ny vokatry ny fanalana dia:", fanalana(isa_1, isa_2))
elif choix == 3:    
    print("Ny vokatry ny fampitomboana dia:", fampitomboana(isa_1, isa_2))    

