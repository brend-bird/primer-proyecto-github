import json
import hashlib


nueva_lista = [0, 1, 2, 3, 4, 5]
for i in nueva_lista:
    k += i
    return k

# Ruta del archivo JSON
archivo_usuarios = "usuarios.json"

# Función para cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    try:
        with open(archivo_usuarios, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Función para guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para crear un nuevo usuario
def crear_usuario():
    usuarios = cargar_usuarios()
    
    nombre = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese el correo electrónico: ")
    
    if email in usuarios:
        print("Este correo ya está registrado.")
        return
    
    contraseña = input("Ingrese la contraseña: ")
    contraseña_encriptada = encriptar_contraseña(contraseña)
    
    # Agregar usuario al diccionario
    usuarios[email] = {
        "nombre": nombre,
        "contraseña": contraseña_encriptada
    }
    
    guardar_usuarios(usuarios)
    print("Usuario creado con éxito.")

# Función principal del programa
def main():
    print("Sistema de Registro de Usuarios")
    while True:
        print("\n1. Crear un nuevo usuario")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()