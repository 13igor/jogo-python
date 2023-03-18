times = ('Flamengo', 'Palmeiras', 'Santos', 'Gremio')
excluir = input("Qual time você deseja excluir? ")
times = list(times)
times.remove(excluir)
times = tuple(times)


print(times)
