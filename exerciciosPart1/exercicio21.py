import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        print("Reproduzindo música...")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print("Erro ao reproduzir música:", e)

    pygame.mixer.music.stop()
    pygame.quit()
play_music('musics/A.mp3')
input()
pygame.event.wait()