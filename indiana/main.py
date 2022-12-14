from time import sleep
from game_engine import GameEngine


def setup_images():
    game_engine = GameEngine()
    game_engine.launch_game(target)

    input("Press any key to continue...")
    for i in range(1, 21):
        image_name = f"images/l{i}.png"
        game_engine._save_image(image_name)
        print(f"Saved image {image_name}")
        sleep(7)


target = "https://www.minijuegosgratis.com/v3/games/games/prod/219431/diamond-rush/index.html?mp_api_as3_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fas3%2Flatest.swf&mp_api_as3_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-as%2F&mp_api_id=1951&mp_api_js_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fjs%2Flatest.js&mp_api_js_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-js%2F&mp_assets=https%3A%2F%2Fs2.minijuegosgratis.com%2F&mp_embed=0&mp_game_id=219431&mp_game_uid=diamond-rush&mp_game_url=https%3A%2F%2Fwww.minijuegos.com%2Fembed%2Fdiamond-rush&mp_int=1&mp_locale=es_ES&mp_player_type=IFRAME&mp_site_https_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_site_name=minijuegos.com&mp_site_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_timezone=America%2FBogota&mp_view_type=&mini_signature=cd6fbd6153154338558c881412712ab8&xdm_e=https%3A%2F%2Fwww.minijuegos.com&xdm_c=default9291&xdm_p=1"


if __name__ == '__main__':
    game_engine = GameEngine()
    game_engine.launch_game(target)

    input("Press any key to continue...")
    playing = True

    while playing:
        path = game_engine.play()
        print(path)
        user_input = input("Press q to quit, any other key to continue: ")
        if user_input == "q":
            playing = False

    game_engine.close_game()
