trabalho_terca = True
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #xor
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

print("Tv_50={}, Tv_32={}, Sorvete={}, Saude={} "
      .format(tv_50, tv_32, sorvete, mais_saude))

#"{}, {}" .format(1, False) 
#substitui o que está dentro da chave pelos argumento de .format, podendo inserir um numero dentro das {} para indicar o indice.
# Exemplo: "{1}, {2}, {0}" .format(1, False, "resultado") vai imprimir: False, resultado = 1