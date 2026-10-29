import time
import pyautogui


def capturar_posicao_mouse(segundos_espera: int = 5) -> None:
    # Aguarda o usuário posicionar o cursor sobre o elemento desejado na tela
    print(f"Posicione o mouse no local desejado em até {segundos_espera} segundos...")
    time.sleep(segundos_espera)
    posicao = pyautogui.position()
    print(f"Posição capturada: x={posicao.x}, y={posicao.y}")


if __name__ == "__main__":
    capturar_posicao_mouse()
