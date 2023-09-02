def validar_categoria(categoria_usuario):
    if categoria_usuario.upper() in categorias:
        print("Categoria Válida!")
    else:
        print("Categoria Inválida!!")

categorias = ("A","B","C","D","E")

categoria_digitada = input("Digite a categoria da CNH: ")

validar_categoria(categoria_digitada)