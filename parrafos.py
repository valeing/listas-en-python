cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc placerat egestas egestas. Morbi malesuada eros sed odio mattis luctus ut quis libero. Nunc tincidunt sapien at congue sodales. Praesent a maximus libero. Proin sed placerat elit, condimentum vulputate nunc. Quisque et sodales nisi. Nulla elementum ex in odio ultrices malesuada. Praesent dictum ante sit amet enim semper scelerisque. Pellentesque eros massa, dapibus at mi eget, ullamcorper aliquet leo. Nulla id lacus id dui convallis dapibus. Aliquam vitae mattis leo. Vivamus elementum, metus elementum eleifend vehicula, magna enim consequat ante, imperdiet blandit elit diam sed urna. Vivamus finibus maximus elit ut laoreet. Aliquam fringilla rhoncus dapibus. Donec in consequat lorem. Sed vestibulum facilisis egestas.

Proin in convallis augue. Vestibulum elementum nibh et urna pellentesque, quis blandit tortor tempor. Vivamus tristique condimentum rutrum. Aliquam at odio facilisis, convallis lorem sit amet, posuere odio. Integer aliquet in felis tristique scelerisque. Duis finibus at velit in eleifend. Integer sed ligula consectetur, sollicitudin nisl at, tempor purus. Curabitur consequat ante nec lorem interdum feugiat. Etiam sagittis ornare ex, vitae tempus purus commodo eget. Curabitur tempor dui nunc, at ultrices ligula condimentum eget. Mauris ac ante viverra, sodales arcu eget, mattis mi. Pellentesque condimentum hendrerit sem. Sed tincidunt bibendum augue a dapibus. Nam quis eleifend magna.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at tellus at. Eget lorem dolor sed viverra ipsum nunc aliquet bibendum. Parturient montes nascetur ridiculus mus. Platea dictumst quisque sagittis purus sit amet. Arcu cursus vitae congue mauris rhoncus aenean vel elit. Ipsum nunc aliquet bibendum enim. Facilisi morbi tempus iaculis urna id volutpat lacus laoreet non. Ullamcorper eget nulla facilisi etiam. Sit amet porttitor eget dolor. Ipsum a arcu cursus vitae congue mauris. Phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam. Posuere morbi leo urna molestie. Eu scelerisque felis imperdiet proin fermentum leo. Condimentum lacinia quis vel eros donec. Nunc mattis enim ut tellus elementum.

In fermentum posuere urna nec tincidunt praesent semper feugiat. Praesent tristique magna sit amet purus gravida. Augue lacus viverra vitae congue eu consequat. Mattis enim ut tellus elementum sagittis vitae et leo duis. Egestas quis ipsum suspendisse ultrices gravida. Sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec. Urna neque viverra justo nec ultrices dui sapien eget. Aenean pharetra magna ac placerat vestibulum lectus mauris ultrices eros. Hendrerit gravida rutrum quisque non. Viverra maecenas accumsan lacus vel facilisis volutpat est velit egestas. Sit amet porttitor eget dolor morbi non arcu. Magna sit amet purus gravida quis. Purus ut faucibus pulvinar elementum. Ultrices tincidunt arcu non sodales. Imperdiet nulla malesuada pellentesque elit eget gravida.

Ut lectus arcu bibendum at. Et sollicitudin ac orci phasellus egestas tellus. Eget est lorem ipsum dolor sit amet. Purus ut faucibus pulvinar elementum integer. Quis eleifend quam adipiscing vitae. Suspendisse in est ante in nibh mauris cursus. Pretium fusce id velit ut tortor pretium. Sollicitudin nibh sit amet commodo nulla facilisi nullam. Eget nullam non nisi est sit amet facilisis magna. Risus commodo viverra maecenas accumsan lacus. Viverra nibh cras pulvinar mattis nunc sed blandit. Et sollicitudin ac orci phasellus egestas. Pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat. Ut diam quam nulla porttitor massa id. Odio euismod lacinia at quis risus sed. Eleifend mi in nulla posuere sollicitudin aliquam.
"""
print(cadenaLarga)

caracteres =['a', 'e','i', 'o','u', ' ', ',','.' ]

# Dada una cadena larga (lorem ipsum de 5 párrafos)
#Presentar un resumen de las estadísticas de los párrafos
#Total de caracteres:
#Total de letras (incluyendo vocales) :
#Total de vocales :
#Total de vocales a :
#Total de vocales e :
#Total de vocales i :
#Total de vocales o :
#Total de vocales u :
#Total de espacios :
#Total de comas :
#Total de palabras :

logitud = len(cadenaLarga)

print(f"La longitud del parrafo" + f" es de : {logitud} caracteres")

int_str = cadenaLarga
res = map(int_str.lower().count, "aeiou")
total=0
for i in ["a","e","i","o","u"]:
    total+=cadenaLarga.count(i)

caracteres = len(cadenaLarga)
caracteres = cadenaLarga.count("a")
print("total de A:",caracteres)

print("[A, E, I , O, U]")
print(list(res))
print("Total de vocales:",total )

palabras = cadenaLarga.split()
total_palabras = len(palabras)
print(f"total de palabras: {total_palabras}")

total_comas = cadenaLarga.count(",")
total_espacios = cadenaLarga.count(" ")

print(f"Total de comas: {total_comas}")
print(f"Total de espacios: {total_espacios}")

puntos = cadenaLarga.split()
total_puntos = len(puntos)
total_puntos=cadenaLarga.count(".")
print(f"total de punto: {total_puntos}")

