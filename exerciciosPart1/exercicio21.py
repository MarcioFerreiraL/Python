<<<<<<< HEAD
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
=======
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
>>>>>>> 2971a5e28b248edd4b836abe9eabe7b067b9aa8f
pygame.event.wait()