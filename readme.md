# Generate Qr images
```python
def run():
    while True:
        option = 1
        if option == 1:
                get_qrCode:str =  input("Ingresar url para crear qr code: ")
                img_name = input("Ingrese el nombre de la imagen: ")
                option = int(input("Salir - 0 | Continuar - 1: "))

                img = qrcode.make(get_qrCode)
                img.save(f"./imgs/{img_name}.png")
        else:
            break


if __name__ == "__main__":
     run()
```