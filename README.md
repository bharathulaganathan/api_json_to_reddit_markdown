# API to Markdown
Name: Bharath | Location: Coimbatore, India | E-mail: bharathulaganathan@gmail.com | GitHub: [bharathulaganathan](https://github.com/bharathulaganathan) | edX : [bharathulaganathan](https://profile.edx.org/u/bharathulaganathan)

## Video Demo:  [YouTube](https://youtu.be/hqFblSJaXnc)

## Description:
This program performs a API get request to Hoyoverse to get the URL for files required to install it's available games. It then formats the response as a JSON. The user can give the name or ID of game of their interest. The program will try to match the user's request with the available games in the API response. It will then format the JSON data to match a markdown format for a reddit post and of the style followed in [this post](https://www.reddit.com/r/GenshinImpact/comments/1fxz9zy/direct_download_links_for_genshin_impact_51/). The program ends after saving formatted data in a file for each game requested.

There is 1 library required to be installed, also specified in requirements.txt:
* requests

## User Inputs:
Both prompts can be left empty.

### 1. API Link
When asked for the API, the user can leave it empty.
```terminal
 API link: 
```
When users give it no input, the default API will be used, else the input will be used for program.
The API can be changed when prompted if the API link is changed in the future.

### 2. Game Name or ID
When prompted for the details of the game the user is looking for
```terminal
 Game name or ID: 
```
The User can either give the name of the game, abbreviated forms of the name, the game's ID or BIZ.
If the user requires the output for all games, user can type "all".
If the user gives and empty response, output will be generated for all available games.

## Output Files:
The output will be in a txt file. The name of the file will correspond to the name of the game, if the game is in pre-download state or not and the version of the game available.
This output can be copied to a reddit post in markdown editor mode to create a [post like this](https://www.reddit.com/r/GenshinImpact/comments/1fxz9zy/direct_download_links_for_genshin_impact_51/).