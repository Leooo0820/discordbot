# Discord Bot

---

## 使用到的Python模組：
> os、re、requests、random、discord、bs4、io、pickle

---

## 程式檔案架構及功能說明
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
>>>> 
>>>> 以 south-korea 表示 South Korea
>>>  
> ### discordbot/src/xkcdpic.py
>> 
>> 說明：
>>> 輸入 $xkcd 進入漫畫查詢功能
>>>  
>>> 接著輸入頁數（格式如下述）
>>>> n-m：第 n 則漫畫至第 m 則漫畫（如：3-5）
>>>> x,y,z：第 x 則漫畫、第 y 則漫畫、第 z 則漫畫（如：3,5,11）
>>>> 輸入 r 或 random：隨機一則漫畫
>>>> 
> ### discordbot/src/lottery.py
>> 
>> 說明：
>>> 輸入 $lotto 進入「大樂透」查詢功能
>>>
>>> 步驟一：輸入 6 碼大樂透號碼
>>> 
>>> 步驟二：輸入期別
>>> 
>>> 步驟三：隨意輸入一個字母以繼續
>>> 
>>> 系統將自動對獎，並輸出中獎金額
>>> 
