# from flask import session, redirect, url_for
# from functools import wraps

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         try:
#             if session.get("user_id") is None:
#                 print("🔒 Usuario no autenticado, redireccionando a login")
#                 return redirect(url_for("users.login"))
#         except Exception as e:
#             print(f"❌ Error en decorador login_required: {e}")
#             return "Error interno en autenticación", 500
#         return f(*args, **kwargs)
#     return decorated_function


from flask import session, redirect, url_for

def login_required(f):
    def decorated_function(*args, **kwargs):
        try:
            if session.get("user_id") is None:
                print("Usuario no Authenticado")
                return redirect(url_for("users.login"))
        except Exception as e:
            print(f"Error en decorador:{e}")
            return "Error interno en authenticacion",500
        return f(*args, **kwargs) # -> f("hernan", "varillas", talla=170)
    
    # decorated_function.__name__ = f.__name__
    # decorated_function.__doc__ = f.__doc__
    return decorated_function 


# @decorador
# def function(nombre):
#     print("Hola " + nombre)
    
    
# @decorado
# def funtion(nombre, appelidoo)
    
# decorador(function)(nombre):
#     print("step 1")
#     result = function()
#     print("step 2")
#     reteurn result

# decorador(function)(nombre)

# @decorador
# mifuncion(nombre)

# resultado = decorador(mifuncion)
# resultado(nombre)


# def funtion(nombre, apellido, edad=10, peso=70, talla=170):
#     pass

# funtion(nombre="Hernan", apellido="varillas")
# function("hernan", "varillas", talla=170)

# args = ["hernan", "varillas"]
# kwargs = {"talla": 170}
# parameters = {
#     "nombre": "Hernan",
#     "apellido": "VArillas",
#     "talla": 170
# }

# parameters = ["Hernan", "Varillas", 32]

# funtion(**parameters)
# funtion(*parameters)

# wname = ["Hernan", "Varillas"]
# name = {
#     "edad": 32,
#     "peso": 100,
#     "talla": 169
# }

# funtion(*wname, **name)

# mifuncion(nombre, talla, *args, **kwargs):
#     print(args)
#     print(kwargs)
    
# mifuncion("jose", "uno]", 20, 20, talla=170, edad=32)
# # [ "uno"...]
# {edad: 32}