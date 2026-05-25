import pygame
# 1. Inicializa o módulo pygame
pygame.init()
# 2. Inicializa o mixer de áudio
pygame.mixer.init()
# 3. Carrega o arquivo MP3 (substitua 'sua_musica.mp3' pelo caminho do seu arquivo)
pygame.mixer.music.load('ex_audio021.MP3')
# 4. Executa o método para tocar a música
pygame.mixer.music.play()
# 5. Mantém o programa aberto enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
#pygame.event.wait()