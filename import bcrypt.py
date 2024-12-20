import bcrypt

class PasswordManager:
    def __init__(self):
        pass

    def hash_password(self, password):
        # Generar una sal
        salt = bcrypt.gensalt()
        # Crear el hash con la contraseña y la sal
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def check_password(self, hashed_password, user_password):
        # Verificar la contraseña
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

# Ejemplo de uso
if __name__ == "__main__":
    password_manager = PasswordManager()
    
    password = "Nolose01"
    hashed_password = password_manager.hash_password(password)
    print(f"Hash generado: {hashed_password}")
    
    user_input = "Nolose01"
    if password_manager.check_password(hashed_password, user_input):
        print("¡La contraseña es correcta!")
    else:
        print("La contraseña es incorrecta.")
