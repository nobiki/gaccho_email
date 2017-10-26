from Article import Article

class Email(Article):
    def color_pair(self):
        return {"text":"WHITE", "back":"BLUE"}

    def get(self):
        return [
                ("Email", "2017-10-19 10:00:00", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ("Email", "2017-10-19 10:00:01", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ("Email", "2017-10-19 10:00:02", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ("Email", "2017-10-19 10:00:03", "投稿者名", "***さん

 お疲れ様です。***です。

おにぎりは、元のキャビネットに戻しておきました。


 以上、宜しくお願い致します。

> ***様
> 
 > 
 > お疲れ様です。
> 
 > 
 > 会議中でしたので、机の上におにぎりを置いておきました
> 
 > 
 > 後ほど、ご査収方、よろしくお願いいたします
> 
 > "),
                ("Email", "2017-10-19 10:00:04", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ("Email", "2017-10-19 10:00:05", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ("Email", "2017-10-19 10:00:09", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ("Email", "2017-10-19 10:00:06", "投稿者名", "てきすとてきすとてきすとてきすと"),
                ]
