from alumnoss import *

alu1 = Alumno("Jax", 202032434)
alu2 = Alumno("Pomni", 202345462)
alu3 = Alumno("Ragatha", 200483475)
alu4 = Alumno("Gangle", 20228234534)
alu5 = Alumno("Zooble", 202267094)

alu1.agregar_calificacion(6)
alu1.agregar_calificacion(7)
alu1.agregar_calificacion(7)

alu2.agregar_calificacion(10)
alu2.agregar_calificacion(8)
alu2.agregar_calificacion(9)
alu2.agregar_calificacion(10)

alu3.agregar_calificacion(8)
alu3.agregar_calificacion(7)
alu3.agregar_calificacion(7)
alu3.agregar_calificacion(8)
alu3.agregar_calificacion(9)

alu4.agregar_calificacion(8)
alu4.agregar_calificacion(8)
alu4.agregar_calificacion(9)
alu4.agregar_calificacion(8)
alu4.agregar_calificacion(7)

alu5.agregar_calificacion(8)
alu5.agregar_calificacion(9)
alu5.agregar_calificacion(9)
alu5.agregar_calificacion(10)
alu5.agregar_calificacion(8)

print(f"El/la alumn@ {alu1.nombre} tiene promedio de: {alu1.calcular_promedio(): .2f} y está {alu1.estado_final()}")
print(f"El/la alumn@ {alu2.nombre} tiene promedio de: {alu2.calcular_promedio(): .2f} y está {alu2.estado_final()}")
print(f"El/la alumn@ {alu3.nombre} tiene promedio de: {alu3.calcular_promedio(): .2f} y está {alu3.estado_final()}")
print(f"El/la alumn@ {alu4.nombre} tiene promedio de: {alu4.calcular_promedio(): .2f} y está {alu4.estado_final()}")
print(f"El/la alumn@ {alu5.nombre} tiene promedio de: {alu5.calcular_promedio(): .2f} y está {alu5.estado_final()}")


grupo1=Grupo("Progra")
grupo1.agregar_alumno(alu1)
grupo1.agregar_alumno(alu2)
grupo1.agregar_alumno(alu3)
grupo1.agregar_alumno(alu4)
grupo1.agregar_alumno(alu5)
print(grupo1.mostrar_promedio())
print(grupo1.mejor_alumno())