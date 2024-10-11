import requests
import sys
import re


key_words = [
    {"proper": "Zenless Zone Zero", "game": "zenlesszonezero",
     "key": ["zzz", "zenless", "zone", "zero", "zenless zone zero",]},
    {"proper": "Honkai: Star Rail", "game": "starrail",
     "key": ["honkai", "sr", "hsr", "honkai star rail", "star rail",]},
    {"proper": "Genshin Impact", "game": "genshinimpact",
     "key": ["genshin", "impact", "gi", "genshin impact",]},
]


def main():
    # Recoding the API link to be used from the User
    api_link = input("API link: ")
    if not(api_link):
        api_link = ("https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/"
                    "api/getGamePackages?launcher_id=VYTpXlbWo8")

    # Try to get the response from the given API as a request
    try:
        response_api = requests.get(api_link)
    except:
        sys.exit("Exception while requesting API")

    # Try to convert the response into a JSON
    try:
        response_json = response_api.json()
    except:
        sys.exit("Exception while converting the request into a JSON")
    
    # Checking if the API JSON is OK
    if response_json["message"] != "OK" or response_json.get("data") == None:
        sys.exit("JSON not OK")

    # Getting user input for game name, id, biz or key
    user_game = input("Game name or ID: ").strip().lower()

    # Creating a list of game name, their id and biz for a list of games
    game_id_biz = match_game(key_words, response_json)

    game_details = []

    # Finding the game name, id and biz for the user input using a function
    if user_game == "all" or user_game == "":
        game_details = game_id_biz
    elif not(find_game(user_game, key_words, game_id_biz)):
        sys.exit("Couldn't find the game")
    else:
        game_details.append(find_game(user_game, key_words, game_id_biz))

    # Finding the matching games to be converted and stored
    for game in game_details:
        ver = ""
        type = "main"
        loc = response_json["data"]["game_packages"][game["index"]]
        if loc["pre_download"]["major"]:
            type = "pre_download"
            ver = loc["pre_download"]["major"]["version"]
        else:
            ver = loc["main"]["major"]["version"]
        with open(f"reddit_{game["game"]}_{ver}_{type}.txt", "w") as r_file:
            r_file.write(str(pre_download_check(loc)))

    # End of main()


# Creating a list of game details from expected game names using API JSON
def match_game(games, json):
    game_id_biz = []
    for game in games:
        for i, game_index in enumerate(json["data"]["game_packages"]):
            if re.search(game["game"], str(game_index), re.IGNORECASE):
                game_id_biz.append({
                    "index": i,
                    "proper": game["proper"],
                    "game": game["game"],
                    "id": game_index["game"]["id"],
                    "biz": game_index["game"]["biz"]
                })
    return game_id_biz


# Recording the details of the user's game choice if it matches the keys
def find_game(user_input, key_words, games):
    for game in games:
        if user_input in (game["game"], game["id"].lower(), game["biz"]):
            return game
    for key_word in key_words:
        if user_input in key_word["key"]:
            for game in games:
                if key_word["game"] == game["game"]:
                    return game
    return False


# Checking if pre-download is available
def pre_download_check(game_location):
    if game_location["pre_download"]["major"]:
        return reddit_dict(game_location["pre_download"])
    else:
        return reddit_dict(game_location["main"])


# Returning a string of reddit markdown formatted details for each game
def reddit_dict(game_location):
    c_v = game_location["major"]["version"]
    lang_key = {
        "en-us": "English",
        "ja-jp": "Japanese",
        "ko-kr": "Korean",
        "zh-cn": "Chinese",
        "zh-tw": "Taiwanese",
    }
    major_txt = ""
    patches_text = []
    for _ in game_location["patches"]:
        patches_text.append("")
    lc = game_location["major"]
    major_txt += (f"\n.\n\n**{lc["version"]} Complete Game** "
                  f"for **Fresh Install**:\n")
    major_txt += f"\nGame Files in {len(lc["game_pkgs"])} Parts:\n"
    for game_part in lc["game_pkgs"]:
        major_txt += f"\n[Game Part {int(game_part["url"][-3:])}]"
        major_txt += f"({game_part["url"]}) "
        major_txt += f">!md5: {game_part["md5"]}!<\n"
    major_txt += f"\nVoice-over Languages:\n"
    for lang in sorted(lc["audio_pkgs"], key=lambda x: x["language"]):
        major_txt += f"\n[{lang_key[lang["language"]]}]({lang["url"]}) "
        major_txt += f">!md5: {lang["md5"]}!<\n"
    lc = game_location["patches"]
    for i, ver in enumerate(lc):
        patches_text[i] += (f"\n.\n\n**Update** Package "
                            f"for **{ver["version"]}** Users:\n")
        patches_text[i] += (f"\n[Game Update]({ver["game_pkgs"][0]["url"]}) "
                            f">!md5: {ver["game_pkgs"][0]["md5"]}!<\n")
        for lang in sorted(ver["audio_pkgs"], key=lambda x: x["language"]):
            patches_text[i] += (f"\n[{lang_key[lang["language"]]} "
                                f"Voice-over Update]({lang["url"]}) "
                                f">!md5: {lang["md5"]}!<\n")
    final_text = ""
    final_text += patches_text[0]
    final_text += major_txt
    for patch in patches_text[1:]:
        final_text += patch
    final_text += "\n.\n"
    return final_text


if __name__ == "__main__":
    main()