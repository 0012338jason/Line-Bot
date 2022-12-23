# TOC Project 2022
## LineBot

## Environment
* Python 2.7
* ngrok
   * Map localhost:8000 to https domain
## Tech
* Web Crawling : 
  * 利用爬蟲的方式，抓取ATP官網資訊
* Multi User
  * 支援多人使用

## Finite State Machine
![fsm](https://github.com/0012338jason/Line-Bot/blob/main/fsm.png)
### State
1. `user` : 使用者加入時，輸入`ranking`、`players`、`tournament`、`headtohead`後便可以開始使用功能
2. `ranking`: 輸入一個1-100的數字(代表排名)，即可到下一個狀態`getranking`。
   1. 進入`getranking`後根據你輸入的數字告訴你排名為此數字的人是誰
   
3. `players`: 輸入一個字串(球員名字)，即可到下一個狀態`getplayername`。
   1. 進入`getplayername`後根據你輸入的名字告訴你此球員的基本資料
4. `tournaments`: 輸入一個數字(1-12)，即可到下一個狀態`gettournaments`。
   1. 進入`gettournaments`後根據你輸入的數字告訴你該月有甚麼比賽
5. `headtohead`: 輸入一個字串(形式: player1 vs player2)，即可到下一個狀態`getheadtohead`。
   1. 進入`getheadtohead`告訴你player1和player2的對戰戰績


## Reference
[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)

[ngrok](https://blog.techbridge.cc/2018/05/24/ngrok/)
