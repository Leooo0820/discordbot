# Discord Bot

## 程式檔案架構
> ### discordbot/src/guess.py 猜數字遊戲（俗稱幾A幾B小遊戲）
>> 
>> 說明：
>>> 輸入「$guess」以開始遊戲
>>> 
>>> 至多可猜30次，每次輸入一個四位數（各位數字不重複），系統將回傳＿A＿B
>>>
> ### discordbot/src/todo_list.py 待辦清單（包含四種功能）
>> 
>> 說明：
>>> 「新增清單」：輸入 $add [date] [label] [item]  (如：＄add 08/20 shopping pizza)
>>> 
>>> 「刪除清單」：輸入 $done [date] [label] [item]  (如：＄done 08/20 shopping pizza)
>>> 
>>> 「依照label顯示清單」：輸入 $show [label] （如：＄show shopping）
>>> 
>>> 「刪除清單，適用於想重新規劃清單者」：輸入 $clear
>>>
> ### discordbot/src/ranking.py 查詢 YouTube 排名
>> 
>> 說明：
>>> 輸入 $rank [dimension] [country] [period] 以開始查詢
>>> 
>>> 如：$rank most-watched worldwide daily
>>>
>>> 特殊輸入參數：
>>>> 以 united 取代 USA
>>>> 以 south-korea 表示 South Korea
>>>  
> ### discordbot/src/xkcdpic.py
>> 
>> 說明：
>> 
> ### discordbot/src/lottery.py
